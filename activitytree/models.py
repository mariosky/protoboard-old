from django.db import models
from django.contrib.auth.models import User
from FIS import Text_Verbal
# Create your models here.


###
# MODELS
###
class LearningStyleInventory(models.Model):
    visual = models.PositiveSmallIntegerField()
    verbal = models.PositiveSmallIntegerField()
    aural = models.PositiveSmallIntegerField()
    physical = models.PositiveSmallIntegerField()
    logical = models.PositiveSmallIntegerField()
    social = models.PositiveSmallIntegerField()
    solitary = models.PositiveSmallIntegerField()
    user = models.OneToOneField(User, unique=True)
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, unique=True)



class LearningActivity(models.Model):
    """ Esta clase implementa los nodos del arbol de actividades """
    name = models.CharField(max_length=128)
    slug = models.SlugField(blank=True)
    
    uri = models.URLField(blank=True)
    lom = models.URLField(blank=True)
    
    parent = models.ForeignKey(to ='LearningActivity',null=True,related_name = 'children')
    root   = models.ForeignKey(to ='LearningActivity',null=True)
    
    pre_condition_rule  = models.TextField(blank=True)
    post_condition_rule = models.TextField(blank=True)
    
    flow = models.BooleanField(default=True)
    forward_only = models.BooleanField(default=False)
    choice = models.BooleanField(default=True)
    
    match_rule = models.TextField(blank=True)
    filter_rule = models.TextField(blank=True)
    rollup_rule  = models.TextField(blank=True)
    
    rollup_objective = models.BooleanField(default=True)
    rollup_progress = models.BooleanField(default=True)
        
    attempt_limit = models.PositiveSmallIntegerField(null=True)
    duration_limit = models.PositiveSmallIntegerField(null=True) 
    available_from = models.DateTimeField(null=True)
    available_until = models.DateTimeField(null=True)
    
    is_container = models.BooleanField()
    is_visible = models.BooleanField(default=True)
    order_in_container = models.PositiveIntegerField(default=0)


    def get_children(self, recursive = False):
        l=[]
        for r in self.children.order_by('order_in_container'):
            l.append(r)          
            if recursive:
                l.extend(r.get_children(True))
        return l
    
    def is_leaf(self):
        if self.is_container:
            return False
        else:
            return True

    def get_root(self):
        if self.root:
            return self.root
        else:
            return self
        
    def __unicode__(self):
        return self.name
        

from decimal import Decimal
class UserLearningActivity(models.Model):
    user = models.ForeignKey(User)
    learning_activity = models.ForeignKey(to ='LearningActivity')
    pre_condition = models.CharField(max_length=32,default = "",blank=True)
    recommendation_value = models.PositiveSmallIntegerField(null=True, default = None)
    progress_status = models.CharField(max_length=16,default = "incomplete",blank=True)
    objective_status = models.CharField(max_length=16,default = "notSatisfied",blank=True)
    objective_measure = models.FloatField( null=True, default = None)
    last_visited = models.DateTimeField(null=True,default = None)
    num_attempts = models.PositiveSmallIntegerField(default=0)
    suspended = models.BooleanField(default=False)
    accumulated_time = models.DecimalField(null=True, decimal_places = 2, max_digits = 3,default = Decimal('0.0'))
    is_current = models.BooleanField(default=False)
    user_rating = models.PositiveSmallIntegerField(null=True,default = None)
    comments = models.TextField(blank=True, default = "")
    
    class Meta:
        unique_together = ("user", "learning_activity")

    def __unicode__(self):
        return self.user.username + ":" + self.learning_activity.name
    
    def eval_pre_condition_rule(self):
        self.pre_condition = ""
        if  self.learning_activity.pre_condition_rule != "":
            exec(self.learning_activity.pre_condition_rule)
            super(UserLearningActivity, self).save()



    def get_objective_measure(self,activity_name):   ###      REVISAR
        activity = UserLearningActivity.objects.select_related('user','learning_activity').filter(user = self.user,
            learning_activity = LearningActivity.objects.filter(name=activity_name))
        if activity[0] is None or activity[0].objective_measure is None:
            return 0
        else:
            return activity[0].objective_measure
            
    def get_children(self, recursive = False):
        l=[]
        for r in UserLearningActivity.objects.filter(learning_activity__parent=self.learning_activity,user=self.user).order_by('learning_activity__order_in_container'):
            l.append(r)          
            if recursive:
                l.extend(r.get_children(True))
        return l
    
    def parse_rollup_rule(self, r):
        """ Rollup Rule:
          (notSatisfied | satisfied | completed | incomplete ) 
             IF ( (All|Any|None) | ( (AT LEAST) (number) (PERCENT | COUNT) ) ) 
               (notSatisfied |satisfied | completed | incomplete )
        """
        rule = {}
        
        status_values = ['notSatisfied', 'satisfied', 'completed' , 'incomplete']
        quantifiers = ['All','Any','None']
        functions = ['PERCENT','COUNT']
        rule_list = r.split()
        
        if rule_list[0] not in status_values:  
            return None #raise Exception: expecting a status value
        elif rule_list[0] in status_values[0:2]:
            rule['status_type'] = 'objective'
        else:
            rule['status_type'] = 'progress'
        rule['consequent_status'] = rule_list[0]
        
        if rule_list[1] != 'IF':
            return None #raise Exception: expecting a status value
        
        if rule_list[2] in quantifiers:
            rule['rule_type'] = 'quantifier'
            rule['quantifier'] =  rule_list[2]
        elif rule_list[2] == 'AT' and rule_list[3] == 'LEAST':
            rule['rule_type'] = 'at_least'
        else:
            return None #raise Exception: expecting a status value
        
        if rule['rule_type']=='quantifier':
            if rule_list[3] in status_values:
                rule['antecedent_status'] =  rule_list[3]   
                return rule
            else:
                return None
        elif  rule['rule_type']=='at_least':
            try:
                rule['number'] = float( rule_list[4])
            except ValueError:
                return None
            if rule_list[5] in functions:
                rule['function_value'] =  rule_list[5]
            else: 
                return None
            
            if rule_list[6]  in status_values: 
                rule['antecedent_status'] =  rule_list[6]   
                return rule
            else:
                return None
        else:
            return None #raise Exception: expecting a status value
    
    def eval_rollup_rule(self, r):
        try:
            rule = self.parse_rollup_rule(r)
        except:
           pass
        
        
        from django.db import connection, transaction
        cursor = connection.cursor()
        
        query =  """SELECT count(*) as count, (  SELECT count(*) 
                                                FROM activitytree_ula_vw 
                                                WHERE parent_id = %s 
                                                AND user_id = %s 
                                                AND rollup_%s = TRUE ) as total
                    FROM   activitytree_ula_vw U
                    WHERE  parent_id = %s 
                    AND user_id = %s AND ( %s_status = '%s' OR pre_condition = 'skip') AND rollup_%s = TRUE """  %  (self.learning_activity.id, 
                             self.user.id, rule['status_type'], self.learning_activity.id, self.user.id,
                            rule['status_type'], rule['antecedent_status'],rule['status_type'] )

        cursor.execute(query)
        r = cursor.fetchone()
        count , total = r
        
        if rule['rule_type'] == 'quantifier':
            if rule['quantifier'] == 'All':
                if count == total:
                    consequent_status = rule['consequent_status']
                else:
                    return None
            elif rule['quantifier'] == 'Any':
                if count > 0:
                    consequent_status = rule['consequent_status']
                else:
                    return None
            elif rule['quantifier'] == 'None':
                if count == 0:
                    consequent_status = rule['consequent_status']
                else:
                    return None
        elif rule['rule_type'] == 'at_least':
            if rule['function_value'] == 'COUNT':
                if count >= rule['number']:
                    consequent_status = rule['consequent_status']
                else:
                    return None
            if rule['function_value'] == 'PERCENT':
                if total > 0:
                    if rule['number'] >= count/total:
                        consequent_status = rule['consequent_status']
                    else:
                        return None
                else:
                    return None
        
        if rule['status_type'] == 'objective':
            self.objective_status = consequent_status
        elif rule['status_type'] == 'progress':
            self.progress_status = consequent_status
        else:
            return None
        super(UserLearningActivity, self).save()
        
    def rollup_rules(self):
        ##Until root
            if self.learning_activity.rollup_rule:
                self.eval_rollup_rule(self.learning_activity.rollup_rule)
            if self.learning_activity.parent != None:
                parent = UserLearningActivity.objects.filter(learning_activity=self.learning_activity.parent,user=self.user)[0]
                parent.rollup_rules()     
  
class ActivityTree(models.Model):
    user = models.ForeignKey(User)
    root_activity = models.ForeignKey(to ='LearningActivity',related_name = 'activity_tree')
    current_activity =  models.ForeignKey(to ='UserLearningActivity',related_name = 'current_in', null = True ,default=None)
    short_description = models.TextField()
    class Meta:
        unique_together = ("user", "root_activity")        
            
            
            
            
            
            
            
            
            
            
            
            
            
            