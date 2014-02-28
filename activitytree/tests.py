__author__ = 'mario'

import unittest
from django.contrib.auth.models import User
from models import UserProfile
from models import LearningStyleInventory
from models import LearningActivity
from models import UserLearningActivity
from models import ActivityTree
from interaction_handler import SimpleSequencing

from models import LearningActivity

class LeearningActivityTestCase(unittest.TestCase):

    def setUp(self):
        LearningActivity.objects.all().delete()
        self.unit = LearningActivity( name = 'Unit', slug = 'Unit',
        uri = "/activity/Unit",
    #    lom =
        parent = None,
        root   = None,

        pre_condition_rule = "",
        post_condition_rule = "",

        flow = True,
        forward_only = True,
        choice = False,

        match_rule = "",
        filter_rule = "",

        rollup_rule  = "satisfied IF All satisfied",
        rollup_objective = True,
        rollup_progress = True,
    #   attempt_limit =
    #   duration_limit =
    #   available_from =
    #   available_until =
        is_container = True,
        is_visible = True,
        order_in_container = 0
        )
        self.unit.save()

        self.pretest = LearningActivity( name = 'Pretest', slug = 'Pretest',
        uri = "/test/Pretest",
    #   lom = ,
        parent = self.unit, root  = self.unit,

        pre_condition_rule = """if self.num_attempts == 0 :
                      self.pre_condition = 'stopForwardTraversal' """,
        post_condition_rule = "",

        flow = True,
        forward_only = True,
        choice = False,

        match_rule = "",
        filter_rule = "",

        rollup_rule  = "",
        rollup_objective = True,
        rollup_progress = True,
    #   attempt_limit =
    #   duration_limit =
    #   available_from =
    #   available_until =
        is_container = False,
        is_visible = True,
        order_in_container = 0
        )
        self.pretest.save()

        self.content = LearningActivity( name = 'Content', slug = 'Content',
        uri = "/activity/Content",
    #   lom =
        parent = self.unit, root   = self.unit,

        pre_condition_rule = "",
        post_condition_rule = "",

        flow = True,
        forward_only = True,
        choice = False,

        match_rule = "",
        filter_rule = "",

        rollup_rule  = "satisfied IF All satisfied",
        rollup_objective = True,
        rollup_progress = True,
    #   attempt_limit =
    #   duration_limit =
    #   available_from =
    #   available_until =
        is_container = True,
        is_visible = True,
        order_in_container = 1
        )
        self.content.save()

        self.remediation = LearningActivity( name = 'Remediation', slug = 'Remediation',
        uri = "/activity/Remediation",
    #   lom =
        parent = self.content, root   = self.unit,

        pre_condition_rule = """if self.get_objective_measure('Pretest')  > 4:
                          self.pre_condition = 'skip' """,
        post_condition_rule = "",

        flow = True,
        forward_only = True,
        choice = False,

        match_rule = "",
        filter_rule = "",

        rollup_rule  = "",
        rollup_objective = True,
        rollup_progress = True,
    #   attempt_limit =
    #   duration_limit =
    #   available_from =
    #   available_until =
        is_container = False,
        is_visible = True,
        order_in_container = 0
        )
        self.remediation.save()

        self.general = LearningActivity( name = 'General', slug = 'General',
        uri = "/activity/General",
    #    lom =
        parent = self.content, root  = self.unit,

        pre_condition_rule = """if self.get_objective_measure('Pretest')  > 9:
                           self.pre_condition = 'skip' """,
        post_condition_rule = "",

        flow = True,
        forward_only = True,
        choice = False,

        match_rule = "",
        filter_rule = "",

        rollup_rule  = "",
        rollup_objective = True,
        rollup_progress = True,
    #   attempt_limit =
    #   duration_limit =
    #   available_from =
    #   available_until =
        is_container = False,
        is_visible = True,
        order_in_container = 1
        )
        self.general.save()

        self.advanced = LearningActivity( name = 'Advanced', slug = 'Advanced',
        uri = "/activity/Advanced",
    #    lom =
        parent = self.content, root   = self.unit,

        pre_condition_rule = """if self.get_objective_measure('Pretest')  < 7:
                          self.pre_condition = 'skip' """,
        post_condition_rule = "",

        flow = True,
        forward_only = True,
        choice = False,

        match_rule = "",
        filter_rule = "",
        rollup_rule  = "",

        rollup_objective = True,
        rollup_progress = True,
    #   attempt_limit =
    #   duration_limit =
    #   available_from =
    #   available_until =
        is_container = False,
        is_visible = True,
        order_in_container = 2
        )
        self.advanced.save()

        User.objects.filter(username='john').delete()
        User.objects.filter(username='paul').delete()


        self.j = User.objects.create_user('john', 'lennon@thebeatles.com', '1234')
        self.j.is_active = True
        self.j.save()

        self.p = User.objects.create_user('paul', 'paul@thebeatles.com', '1234')
        self.p.is_active = True
        self.p.save()

        self.lsj=LearningStyleInventory(visual=12,verbal=11,aural=15,physical=9,logical=11,
                                  social=9, solitary=10, user = self.j)
        self.lsj.save()

        self.lsp=LearningStyleInventory(visual=12,verbal=11,aural=20,physical=9,logical=11,
                                  social=9, solitary=7, user = self.p)
        self.lsp.save()

    

    def testSimpleSequencing(self):
        self.s = SimpleSequencing()
        self.s.assignActivityTree(self.j,self.unit)
        self.s.assignActivityTree(self.p,self.unit)

        #self.self.assertEqual(self.lion.speak(), 'The lion says "roar"')
        #self.self.assertEqual(self.cat.speak(), 'The cat says "meow"')
