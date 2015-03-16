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
    is_visible = True
)
intro.save()

