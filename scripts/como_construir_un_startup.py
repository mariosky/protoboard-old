# -*- coding: utf-8 -*-

##
##
##  Example of a Learning Activity Tree
##
##

__author__ = 'mario'

if __name__ == "__main__":
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")
    import django
    from django.conf import settings
    django.setup()

from activitytree.models import LearningStyleInventory, LearningActivity, Course, UserLearningActivity

LearningActivity.objects.all().delete()

startup = LearningActivity( name = 'Como construir un startup', slug = 'como_construir_un_startup',
    uri = "/activity/startup",
    heading="Como construir un startup",
    secondary_text = "Tutorial",
    description = """Este tutorial te brinda los conocimientos para que inicies tu propia startup, en particular se centra en
        explicarnos el como desarrollar el Buissiness Model Camvas""",

    image = "https://s3.amazonaws.com/learning-python/python-logo.png",

    parent = None,
    root   = None,

    choice_exit = False,
    is_container = True,
    order_in_container = 0
)

startup.save()
description= u"""
          <p> Como Construir un Startup</p>
"""


cursoStartUP = Course(short_description=description, root=startup)
cursoStartUP.save()



intro = LearningActivity( name = 'Lo que ahora sabemos',
    uri = "/activity/startup/lo-que-ahora-sabemos",
    parent = startup, root  = startup,
    heading="Lo que ahora sabemos",
    description = "Las reglas que se aplican a las empresas son muy diferentes a los startups.",
    image = "https://s3.amazonaws.com/learning-python/python-logo.png",
    secondary_text = "Lección 1",
    is_container = True,
    is_visible = True,
    order_in_container = 0

)
intro.save()

tema_1_1 = LearningActivity( name = 'Lo que ahora sabemos', slug = '',
    uri = '/activity/video/lo-que-ahora-sabemos',
    lom = '/activity/video/lo-que-ahora-sabemos',

    heading="Lo que ahora sabemos",
    description = "¿En qué son distintas las startups y la empresas?",
    image = "https://s3.amazonaws.com/learning-python/IntroVideo.png",

    parent = intro, root  = startup,
    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 0
    )
tema_1_1.save()


bmc = LearningActivity( name = 'El Lienzo del Modelo de Negocio',
    uri = "/activity/startup/business-model-canvas",
    parent = startup, root  = startup,
    heading="El Lienzo del Modelo de Negocio",
    description = "Un lenguaje común para describir, visualizar, evaluar y modificar modelos de negocio.",
    image = "https://s3.amazonaws.com/learning-python/python-logo.png",
    secondary_text = "Lección 2",
    is_container = True,
    is_visible = True,
    order_in_container = 1
)
bmc.save()

customer = LearningActivity( name = 'El Desarrollo del Cliente',
    uri = "/activity/startup/customer-development",
    parent = startup, root  = startup,
    heading="El Desarrollo del Cliente",
    description = "Sabemos lo que el cliente necesita.. Ni cerca, debemos salir del edificio para entenderlo.",
    image = "https://s3.amazonaws.com/learning-python/python-logo.png",
    secondary_text = "Lección 3",
    is_container = True,
    is_visible = True,
    order_in_container = 2
)
customer.save()