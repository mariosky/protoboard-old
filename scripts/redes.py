# -*- coding: utf-8 -*-
__author__ = 'mariosky'


if __name__ == "__main__":
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")
    import django
    from django.conf import settings
    django.setup()


from activitytree.models import LearningActivity, Course
LearningActivity.objects.all().delete()

Redes = LearningActivity( name = 'Redes', slug = 'Redes',
    uri = "/activity/Redes",
    heading=u"Redes y transmisión de datos",
    secondary_text = "Tutorial",
    description = u"En este trabajo explicamos como se emplean las capas para una presentacón de multiples dispositivos.",
    image = "https://s3.amazonaws.com/learning-python/python-logo.png",

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
    is_visible = False,
    order_in_container = 0
    )

Redes.save()
description= u"""
          <p> En este trabajo explicamos como se emplean las capas para una presentacón de multiples dispositivos.</p>
            """


curso = Course(short_description=description, root=Redes)
curso.save()

actividad1 = LearningActivity(
    name = 'Actividad 1', slug = 'A1',
    uri = '/activity/actividad1',
    parent = Redes, root  = Redes,

    choice_exit = False,

    pre_condition_rule = "",

    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,
    attempt_limit=3,

    is_container = False,
    is_visible = False,
    order_in_container = 1
    )
actividad1.save()


actividad2 = LearningActivity(
    name = 'Actividad 2', slug = 'A2',
    uri = '/activity/actividad2',
    parent = Redes, root  = Redes,

    choice_exit = False,

    pre_condition_rule = "",

    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,
    attempt_limit=3,

    is_container = False,
    is_visible = False,
    order_in_container = 2
    )
actividad2.save()

actividad3 = LearningActivity(
    name = 'Actividad 3', slug = 'A3',
    uri = '/activity/actividad3',
    parent = Redes, root  = Redes,

    choice_exit = False,

    pre_condition_rule = "",

    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,
    attempt_limit=3,

    is_container = False,
    is_visible = False,
    order_in_container = 3
    )
actividad3.save()

actividad4 = LearningActivity(
    name = 'Actividad 4', slug = 'A4',
    uri = '/activity/actividad4',
    parent = Redes, root  = Redes,

    choice_exit = False,

    pre_condition_rule = "",

    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,
    attempt_limit=3,

    is_container = False,
    is_visible = False,
    order_in_container = 4
    )
actividad4.save()

actividad5 = LearningActivity(
    name = 'Actividad 5', slug = 'A5',
    uri = '/activity/actividad5',
    parent = Redes, root  = Redes,

    choice_exit = False,

    pre_condition_rule = "",

    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,
    attempt_limit=3,

    is_container = False,
    is_visible = False,
    order_in_container = 5
    )
actividad5.save()

actividad6 = LearningActivity(
    name = 'Actividad 6', slug = 'A6',
    uri = '/activity/actividad6',
    parent = Redes, root  = Redes,

    choice_exit = False,

    pre_condition_rule = "",

    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,
    attempt_limit=3,

    is_container = False,
    is_visible = False,
    order_in_container = 6
    )
actividad6.save()


