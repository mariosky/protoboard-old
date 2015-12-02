# -*- coding: utf-8 -*-
__author__ = 'mariosky'


if __name__ == "__main__":
    import os
    from django.core.wsgi import get_wsgi_application

    print "####### DJANGO SETTINGS"

    os.environ['DJANGO_SETTINGS_MODULE'] = "protoboard.settings"
    application = get_wsgi_application()

import json
from activitytree.models import LearningStyleInventory, LearningActivity, Course, UserLearningActivity
from django.contrib.auth.models import User
from activitytree.interaction_handler import SimpleSequencing


LearningActivity.objects.all().delete()


j = r"""[{"id":"4ef42fb0-8733-4e3e-8ce5-e69c83bdf489","order":0,"children":[{"id":"7b8bfd64-f69e-406d-a60f-d5df6abd5a25","order":0,"children":[],"learning_activity":{"name":"El secuenciado simple","heading":"1. Secuenciado simple","secondary_text":"","description":"Protoboard utiliza reglas para el secuenciado de actividades de aprendizaje. Aquí se explica de que se trata. De hecho hay una regla que estipula que no puedes visitar la actividad siguiente hasta ver esta.","image":"https://s3.amazonaws.com/learning-python/IntroVideo.png","slug":"","uri":"/activity/SecuenciadoSimple","lom":null,"pre_condition_rule":null,"choice_exit":true,"rollup_rule":"completed IF All completed","attempt_limit":100,"rollup_progress":true,"available_from":null,"available_until":null,"is_container":false,"is_visible":true}},{"id":"3f395aa0-68e8-4a97-87f5-609cc407171a","order":1,"children":[{"id":"75779703-613d-4978-87dd-08746f7ada7b","order":0,"children":[],"learning_activity":{"name":"Video","heading":"Ejemplo de Video","secondary_text":"","description":"Ejemplo de video, al llegar a los 15 segundos se salta a la siguiente actividad.","image":"","slug":"","uri":"/activity/video/intro","lom":null,"pre_condition_rule":null,"choice_exit":true,"rollup_rule":"completed IF All completed","attempt_limit":"100","rollup_progress":true,"available_from":null,"available_until":null,"is_container":false,"is_visible":true}},{"id":"b97d66fe-937a-4e92-81be-37cb4bb521ed","order":1,"children":[],"learning_activity":{"name":"Quiz","heading":"Ejemplo de un Quiz","secondary_text":"","description":"Máximo 4 intentos.","image":"","slug":"","uri":"/test/demo","lom":null,"pre_condition_rule":null,"choice_exit":false,"rollup_rule":"completed IF All completed","attempt_limit":"4","rollup_progress":true,"available_from":null,"available_until":null,"is_container":false,"is_visible":true}}],"learning_activity":{"name":"Recursos","heading":"2. Recursos","secondary_text":"Contenedor","description":"Este es un contenedor con varias actividades, estará deshabilitado hasta que visites la actividad Secuenciado Simple.","image":"","slug":"","uri":"/activity/Recursos","lom":null,"pre_condition_rule":"if get_attr('/activity/SecuenciadoSimple','progress_status') == 'completed':\n    activity['pre_condition'] = ''\nelse:\n    activity['pre_condition'] = 'disabled'\n","choice_exit":true,"rollup_rule":"completed IF All completed","attempt_limit":100,"rollup_progress":true,"available_from":null,"available_until":null,"is_container":true,"is_visible":true}},{"id":"97e3a6a1-380f-44e9-ba2c-42fc719d6973","order":2,"children":[{"id":"3b0b8f13-a27c-4842-9e64-5d52fa18075d","order":0,"children":[],"learning_activity":{"name":"JavaScript","heading":"JavaScript","secondary_text":"","description":"Es un lenguaje de programación interpretado, dialecto del estándar ECMAScript. Se define como orientado a objetos,3 basado en prototipos, imperativo, débilmente tipado y dinámico","image":"","slug":"","uri":"/program/js/1","lom":null,"pre_condition_rule":null,"choice_exit":false,"rollup_rule":"completed IF All completed","attempt_limit":"3","rollup_progress":true,"available_from":null,"available_until":null,"is_container":false,"is_visible":true}},{"id":"3125d726-75d4-4f09-8e13-a3cbc3e029b5","order":1,"children":[],"learning_activity":{"name":"Java","heading":"Java","secondary_text":"","description":"Su intención es permitir que los desarrolladores de aplicaciones escriban el programa una vez y lo ejecuten en cualquier dispositivo","image":"","slug":"","uri":"/program/java/1","lom":null,"pre_condition_rule":null,"choice_exit":true,"rollup_rule":"completed IF All completed","attempt_limit":100,"rollup_progress":true,"available_from":null,"available_until":null,"is_container":false,"is_visible":true}}],"learning_activity":{"name":"Ejercicios de Programación","heading":"3. Ejercicios","secondary_text":"Contenedor","description":"Ejemplos de los distintos lenguajes de programación, con los que se pueden hacer ejercicios","image":"","slug":"","uri":"/activity/97e3a6a1-380f-44e9-ba2c-42fc719d6973","lom":null,"pre_condition_rule":null,"choice_exit":true,"rollup_rule":"completed IF Any completed","attempt_limit":100,"rollup_progress":true,"available_from":null,"available_until":null,"is_container":true,"is_visible":true}}],"learning_activity":{"name":"Protoboard 101","heading":"","secondary_text":"","description":"<p> Este es un curso de ejemplo para mostrar la funcionalidad de <code>protoboard</code>.\n        Se muestran los tipos de ejercicios y recursos que se pueden utilizar para crear cursos de programación. </p>","image":"","slug":"","uri":"/activity/demo","lom":null,"pre_condition_rule":null,"choice_exit":true,"rollup_rule":"completed IF All completed","attempt_limit":100,"rollup_progress":true,"available_from":null,"available_until":null,"is_container":true,"is_visible":true}}]"""


curso = json.loads(j)[0]


def traverse(activity, parent=None, root=None):


    print activity['learning_activity']['name'],parent



    learning_activity = LearningActivity(
        parent = parent or None,
        root   = root or None,
        name = activity['learning_activity']['name'],
        slug = activity['learning_activity']['slug'],
        uri = activity['learning_activity']['uri'],
        lom = activity['learning_activity']['lom'] or "",
        secondary_text=activity['learning_activity']['secondary_text'],
        attempt_limit=activity['learning_activity']['attempt_limit'] ,
        available_until=activity['learning_activity']['available_until'] ,
        available_from =activity['learning_activity']['available_from'],
        heading=activity['learning_activity']['heading'],
        description =activity['learning_activity']['description'],
        image = activity['learning_activity']['image'],
        pre_condition_rule =activity['learning_activity']['pre_condition_rule'] or "",
        rollup_rule  =activity['learning_activity']['rollup_rule'],
        is_container = activity['learning_activity']['is_container'],
        is_visible = activity['learning_activity']['is_visible'],
        order_in_container = activity['order'],
        choice_exit = activity['learning_activity']['choice_exit'],
        rollup_progress= activity['learning_activity']['rollup_progress'])

    learning_activity.save()

    # Si es raiz es curso
    if root is None:
        root = learning_activity
        curso = Course(short_description=activity['learning_activity']['description'], root=root)
        curso.save()



    if 'children' in activity:
        if activity['children']:
            for child in activity['children']:
                traverse(child, learning_activity, root)
    else:
        pass



traverse(curso)