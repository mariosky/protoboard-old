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
Demo = LearningActivity( name = 'Protoboard 101', slug = 'Demo',
    uri = "/activity/demo",
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

Demo.save()
description= u"""
        <p> Este es un curso de ejemplo para mostrar la funcionalidad de <code>protoboard</code>.
        Se muestran los tipos de ejercicios y recursos que se pueden utilizar para crear cursos de programación. </p>"""


cursoDemo = Course(short_description=description, root=Demo)
cursoDemo.save()



preliminar = LearningActivity( name = 'El secuenciado simple', slug = 'Preliminar',
    uri = "/activity/SecuenciadoSimple",
#   lom =
    parent = Demo, root   = Demo,
    heading="Secuenciado simple",
    description = u"""Protoboard utiliza reglas para el secuenciado de actividades de aprendizaje. Aquí se explica de que se trata. De hecho hay unas reglas que estipulan que no puedes continuar si no visitas esta actividad. """,
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


recursos = LearningActivity( name = 'Recursos', slug = 'Recursos',
    uri = "/activity/Recursos",
#   lom =
    parent = Demo, root  = Demo,
    heading="Recursos",
    secondary_text = "Contenedor",
    description = u"""Este es un contenedor con varias actividades, estará deshabilitado hasta que visites la actividad Secuenciado Simple.""",

    pre_condition_rule = """
if get_attr('/activity/SecuenciadoSimple','objective_status') == 'satisfied':
    activity['pre_condition'] = ''
else:
    activity['pre_condition'] = 'disabled'
""",
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,


    rollup_rule  = "satisfied IF All satisfied",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = True,
    order_in_container = 1
    )
recursos.save()


video = LearningActivity( name = 'Video', slug = '',
    uri = "/activity/video/intro",
#   lom =
    parent = recursos, root  = Demo,
    heading="Ejemplo de Video",
    description = u"""Ejemplo de video, al llegar a los 15 segundos se salta a la siguiente actividad.""",

    pre_condition_rule = "",
    post_condition_rule = "",

    is_container = False,
    is_visible = True,
    order_in_container = 0
    )
video.save()

test = LearningActivity( name = 'Quiz', slug = '',
    uri = "/test/demo",
#   lom =
    parent = recursos, root  = Demo,
    heading="Ejemplo de un Quiz",
    description = u"""Máximo 4 intentos.""",

    pre_condition_rule = "",
    post_condition_rule = "",
    attempt_limit=4,
    is_container = False,
    is_visible = True,
    order_in_container = 1
    )
test.save()


programas = LearningActivity( name = 'Ejercicios de Programación', slug = '',
    uri = "/activity/Ejercicios",
#   lom =
    parent = Demo, root  = Demo,
    heading="Ejercicios",
    secondary_text = "Contenedor",
    description = u"""Ejemplos de los distintos lenguajes de programación, con los que se pueden hacer ejercicios""",

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,


    rollup_rule  = "satisfied IF All satisfied",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = True,
    order_in_container = 2
    )
programas.save()


csharp = LearningActivity( name = 'CSharp', slug = '',
    uri = "/program/csharp/1",
#   lom =
    parent = programas, root  = Demo,
    heading="C#",
    description = u"""C# es un lenguaje de programación orientado a objetos desarrollado y estandarizado por Microsoft como parte de su plataforma .NET""",
    choice_exit = False,
    pre_condition_rule = "",
    post_condition_rule = "",
    attempt_limit=4,
    is_container = False,
    is_visible = True,
    order_in_container = 1
    )
csharp.save()

javascript = LearningActivity( name = 'Javascript', slug = '',
    uri = "/program/js/1",
#   lom =
    parent = programas, root  = Demo,
    heading="javascript",
    description = u"""es un lenguaje de programación interpretado, dialecto del estándar ECMAScript. Se define como orientado a objetos,3 basado en prototipos, imperativo, débilmente tipado y dinámico.""",
    choice_exit = False,
    pre_condition_rule = "",
    post_condition_rule = "",
    attempt_limit=4,
    is_container = False,
    is_visible = True,
    order_in_container = 1
    )
javascript.save()


Java = LearningActivity( name = 'Java', slug = '',
    uri = "/program/java/1",
#   lom =
    parent = programas, root  = Demo,
    heading="Java",
    description = u"""Su intención es permitir que los desarrolladores de aplicaciones escriban el programa una vez y lo ejecuten en cualquier dispositivo""",
    choice_exit = False,
    pre_condition_rule = "",
    post_condition_rule = "",
    attempt_limit=4,
    is_container = False,
    is_visible = True,
    order_in_container = 1
    )
Java.save()


JQuery= LearningActivity( name = 'jQuery', slug = '',
    uri = "/program/js/2",
#   lom =
    parent = programas, root  = Demo,
    heading="jQuery",
    description = u"""jQuery es una biblioteca de JavaScript, creada inicialmente por John Resig, que permite simplificar la manera de interactuar con los documentos HTML, manipular el árbol DOM, manejar eventos, desarrollar animaciones y agregar interacción con la técnica AJAX a páginas web.""",
    choice_exit = False,
    pre_condition_rule = "",
    post_condition_rule = "",
    attempt_limit=4,
    is_container = False,
    is_visible = True,
    order_in_container = 1
    )
JQuery.save()

Py = LearningActivity( name = 'Python', slug = '',
    uri = "/program/suma/3",
#   lom =
    parent = programas, root  = Demo,
    heading="Python",
    description = u"""Es un lenguaje interpretado, usa tipado dinámico y es multiplataforma.""",
    choice_exit = False,
    pre_condition_rule = "",
    post_condition_rule = "",
    attempt_limit=4,
    is_container = False,
    is_visible = True,
    order_in_container = 1
    )
Py.save()
