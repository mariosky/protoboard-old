# -*- coding: utf-8 -*-
__author__ = 'mariosky'


if __name__ == "__main__":
    import os
    from django.core.wsgi import get_wsgi_application

    print "####### DJANGO SETTINGS"

    os.environ['DJANGO_SETTINGS_MODULE'] = "protoboard.settings"
    application = get_wsgi_application()


from activitytree.models import LearningStyleInventory, LearningActivity, Course, UserLearningActivity
from django.contrib.auth.models import User
from activitytree.interaction_handler import SimpleSequencing

LearningActivity.objects.all().delete()


POO = LearningActivity( name = 'Prog OO en C#', slug = 'POO',
    uri = "/activity/POO",
    parent = None,
    root   = None,

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,

    rollup_rule  = "satisfied IF All satisfied",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 0
    )

POO.save()
description= u"""
        <p> Que no te intimiden las palabras <code>class</code> , <code>abstract</code> , <code>override</code> o te dé miedo eso del
        <strong> polimorfismo </strong> o te emociones con la <strong> herencia múltiple</strong>.</p>
        <p> Ya deberías saber programación básica en algún lenguaje de programación. </p>"""


cursoPOO = Course(short_description=description, root=POO)
cursoPOO.save()


content = LearningActivity( name = 'Unidad 2', slug = 'U2',
    uri = "/activity/POO/U2",
#   lom =
    parent = POO, root  = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,

    match_rule = "",
    filter_rule = "",

    rollup_rule  = "satisfied IF All satisfied",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = True,
    order_in_container = 2
    )
content.save()

preliminar = LearningActivity( name = 'Comentario Preliminar', slug = 'Preliminar',
    uri = "/activity/Preliminar",
#   lom =
    parent = content, root   = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,
    order_in_container = 0
    )
preliminar.save()



program_1 = LearningActivity( name = 'Ejercicio 1', slug = 'E1',
    uri = "/program/1",
#   lom =
    parent = content, root  = POO,

#   pre_condition_rule = """self.recommendation_value = Text_Verbal.eval(self.user.learningstyleinventory.verbal,self.user.learningstyleinventory.visual)"""  ,

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,

    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = True,    order_in_container = 1
    )
program_1.save()

program_2 = LearningActivity( name = 'Ejercicio 2', slug = 'E2',
    uri = "/program/2",
   parent = content, root  = POO,


    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,

    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = True,    order_in_container = 2
    )
program_2.save()



