__author__ = 'mario'


import psycopg2
from psycopg2.extras import DictCursor
import datetime
import xml.etree.ElementTree as ET
import functools

def bench(func=None, name=None):
    """
    Decorator used for benchmark execution of arbitrary function.
    """
    if func is None:
        return functools.partial(bench, name=name)

    def _wrapper(*args, **kwargs):
        t = datetime.datetime.now()
        result = func(*args, **kwargs)

        delta = (datetime.datetime.now() - t).total_seconds() * 1000.0
        print("[{}] Elapsed time: {} msecs.".format(name, delta))
        return result
    return _wrapper


@bench(name="to_xml")
def nav_to_xml(node=None, s="", root=None):
    open_tag_template = '<item activity = "%s"  uri = "%s"   identifier = "%s" is_current = "%s" is_container  = "%s" pre_condition = "%s"  recomended_value = "%s" objective_status ="%s" objective_measure ="%s" is_visible ="%s" heading ="%s" secondary_text="%s" description="%s" image ="%s" num_attempts="%s" attempt_limit="%s">'
    single_tag_template = open_tag_template[:-1]+'/>'
    if node is None:
        node = root
    vals = (node.learning_activity.id, node.learning_activity.uri, node.learning_activity.name, node.is_current,
            node.learning_activity.is_container, node.pre_condition,
            node.recommendation_value,
            node.objective_status, node.objective_measure,node.learning_activity.is_visible,
            node.learning_activity.heading,node.learning_activity.secondary_text,node.learning_activity.description,node.learning_activity.image,
            node.num_attempts,node.learning_activity.attempt_limit)
    if len(node.children) > 0:

        s += open_tag_template % vals
        for child in node.children:
            s += nav_to_xml(node=child)
        s += '</item>'
        return s
    else:
        s += single_tag_template % vals
        return s



def _get_children(id,recs):
    return [v for k,v in recs.items() if id == v["parent_id"] ]

def xml_row(row):
    str_dict = {}
    for k,v in row.items():
        str_dict[k]=unicode(v)
    return str_dict

#if get_attr('/activity/PB','num_attempts') > 0:


pre ="""
if activity['num_attempts'] == 0 :
    activity['pre_condition'] = 'stopForwardTraversal'
else:
    activity['pre_condition'] = ''
"""

#@bench(name="SQL_NAV")
def _get_nav(id,recs,xml_tree=None):
    if recs[id]["parent_id"] is None:
        xml_tree = ET.Element("item")
        xml_tree.attrib = xml_row(recs[id])

    children = _get_children(id,recs)
    if children:
        for activity in children:
            print activity['pre_condition_rule']

            exec(pre)
            #print activity['pre_condition']

            _get_nav(activity['id'],recs,ET.SubElement(xml_tree,'item',xml_row(activity)))
    else:
        pass
        #ET.SubElement(xml_tree,'item',{'name':recs[id]['name']})



    return xml_tree



@bench(name="recursive")
def get_nav( ula):
    #print "get_nav call",ula
    #If nodes is None we are at root
    if ula.learning_activity.parent is None:
        #Refresh root in case it was changed elsewhere
        ula = UserLearningActivity.objects.get(id=ula.id)
        ula.children = []
    #Get children activities
    children = ula.get_children(recursive=False)
    if children:
        #Process child nodes-*
        for child in children:
            child.children = []
            child.eval_pre_condition_rule()

            #IF Parent ForwardOnly is True, disable if already tried
            #print child.learning_activity.uri, child.pre_condition
            if child.pre_condition == 'stopForwardTraversal':
                ula.children.append(child)
                return ula
            elif child.pre_condition == 'skip':
                pass
            elif ula.learning_activity.forward_only and child.num_attempts > 0:
                child.pre_condition = 'disabled'
                ula.children.append(get_nav(child))
            else:
                # disabled, hidden are still returned
                ula.children.append(get_nav(child))

        return ula
    else:

        #no more nodes to process return nodes
        ula.children = []
        return ula




#@bench(name="sql")
def sql():
    cur = con.cursor(cursor_factory=DictCursor)
    query= """
WITH RECURSIVE nodes_cte AS (
SELECT 	n.id, n.parent_id, n.name, n.id::TEXT AS path,
		n.heading, n.secondary_text, n.description, n.image, n.slug, n.uri, n.lom, n.root_id,
		n.pre_condition_rule, n.post_condition_rule, n.flow, n.forward_only, n.choice,
		n.choice_exit, n.attempt_limit, n.available_from,
		n.available_until, n.is_container, n.is_visible, n.order_in_container
FROM activitytree_learningactivity AS n
WHERE n.parent_id = 1
	UNION ALL
SELECT 	c.id, c.parent_id, c.name, c.id::TEXT AS path,
		c.heading, c.secondary_text, c.description, c.image, c.slug, c.uri, c.lom, c.root_id,
		c.pre_condition_rule, c.post_condition_rule, c.flow, c.forward_only, c.choice,
		c.choice_exit, c.attempt_limit, c.available_from,
		c.available_until, c.is_container, c.is_visible, c.order_in_container
FROM nodes_cte AS p, activitytree_learningactivity AS c
WHERE c.parent_id = p.id
)
(
SELECT  la.id, parent_id, name, ''as path,
		heading, secondary_text, description, image, slug, uri, lom, root_id,
		pre_condition_rule, post_condition_rule, flow, forward_only, choice,
		choice_exit, attempt_limit, available_from,
		available_until, is_container, is_visible, order_in_container,
		pre_condition, recommendation_value, progress_status, objective_status,
        objective_measure, last_visited, num_attempts, is_current

FROM activitytree_learningactivity la, activitytree_userlearningactivity ula

WHERE la.id = 1
	AND la.id = ula.learning_activity_id
	AND ula.user_id = 2

UNION ALL
SELECT  nd.id, parent_id, name,path,
		heading, secondary_text, description, image, slug, uri, lom, root_id,
		pre_condition_rule, post_condition_rule, flow, forward_only, choice,
		choice_exit, attempt_limit, available_from,
		available_until, is_container, is_visible, order_in_container,
		pre_condition, recommendation_value, progress_status, objective_status,
        objective_measure, last_visited, num_attempts, is_current

FROM nodes_cte AS nd, activitytree_userlearningactivity ula
WHERE
	   nd.id = ula.learning_activity_id
	   AND ula.user_id = 2


ORDER BY path ASC

);"""

    cur.execute(query)


    recs = cur.fetchall()
    records = {}
    for record in recs:
        records[record["id"]] = dict(record)
    return records


if __name__ == "__main__":
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")
    import django
    from django.conf import settings
    django.setup()


    print "####### DJANGO SETTINGS"


con = psycopg2.connect(database=settings.DATABASES['default']['NAME'],user=settings.DATABASES['default']['USER'],
                       host=settings.DATABASES['default']['HOST'],password=settings.DATABASES['default']['PASSWORD'],
                       )
print con
from activitytree.models import LearningStyleInventory, LearningActivity, Course, UserLearningActivity
from activitytree.interaction_handler import SimpleSequencing
from django.contrib.auth.models import User

mario =  User.objects.all()[1]
print mario.id

la = LearningActivity.objects.get(uri="/activity/secuencias")
ula =  la.userlearningactivity_set.get(user=mario)

print ula
print ula.learning_activity.parent.userlearningactivity_set.get(user=mario)


#root= UserLearningActivity.objects.filter(learning_activity__uri = "/activity/PB" ,user = User.objects.filter(username=mario.username)[0] )[0]

#n = get_nav(root)
#s = nav_to_xml(root=n)

#print s
recs = sql()

xml = _get_nav(1,recs)
#ET.dump(xml)







