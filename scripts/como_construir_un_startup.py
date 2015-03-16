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


PPP = LearningActivity( name = 'Como construir un startup', slug = 'como_construir_un_startup',
    uri = "/activity/startup",
    heading="Como construir un startup",
    secondary_text = "Tutorial",
    description = """Este tutorial te brinda los conocimientos para que inicies tu propia startup, en particular se centra en
        explicarnos el como desarrollar el Buissiness Model Camvas""",
    image = "https://s3.amazonaws.com/learning-python/python-logo.png",

    parent = None,
    root   = None,

    choice_exit = False,

    rollup_rule  = "satisfied IF All satisfied",

    is_container = True,
    is_visible = True,
    )