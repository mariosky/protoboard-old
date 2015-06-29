# -*- coding: utf-8 -*-
__author__ = 'mario'



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
        <p> Ya deberías saber programación básica en algún lenguaje de programación. Este curso es en C# </p>"""


cursoPOO = Course(short_description=description, root=POO)
cursoPOO.save()


content = LearningActivity( name = 'Contenido', slug = 'Contenido',
    uri = "/activity/Contenido",
#   lom =
    parent = POO, root  = POO,
    heading="Introducción a la P.O.O.",
    description = "Aprenderás cuales son las caracteristicas del paradigma.",
    image = "https://s3.amazonaws.com/learning-python/IntroVideo.png",

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,

    match_rule = "",
    filter_rule = "",

    rollup_rule  = "satisfied IF Any satisfied",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = True,
    order_in_container = 1
    )
content.save()

preliminar = LearningActivity( name = 'Comentario Preliminar', slug = 'Preliminar',
    uri = "/activity/Preliminar",
#   lom =
    parent = POO, root   = POO,
    heading="¿Qué es Orientado a Objetos?",
    description = "Aprenderás cuales son las caracteristicas del paradigma.",
    image = "https://s3.amazonaws.com/learning-python/IntroVideo.png",


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


program_1 = LearningActivity( name = 'Imprime Hola', slug = 'E1',
    uri = "/program/POO/1",

    heading="La Clase Producto",
    description = "Escribe tu primera clase",
    image = "https://s3.amazonaws.com/learning-python/images.png",



    parent = content, root  = POO,
    pre_condition_rule = "",
    post_condition_rule = "",

    choice_exit = False,
    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 0
    )
program_1.save()


