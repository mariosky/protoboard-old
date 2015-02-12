# -*- coding: utf-8 -*-

##
##
##  Example of a Learning Activity Tree
##
##



if __name__ == "__main__":
    import os
    print "####### DJANGO SETTINGS"
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")






from activitytree.models import LearningStyleInventory, LearningActivity, Course, UserLearningActivity
from django.contrib.auth.models import User
from activitytree.interaction_handler import SimpleSequencing



LearningActivity.objects.all().delete()


PPP = LearningActivity( name = 'Python Básico', slug = 'PB',
    uri = "/activity/PB",
    heading="Python Básico",
    secondary_text = "",
    description = "Tutorial del lenguaje Python, orientado a principiantes.",
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
    is_visible = True,
    order_in_container = 0
    )

PPP.save()
description= u"""
          <p> Curso de Python básico, ¡Aprende desde cero!</p>
            <p><code>print "hola mundo"</code></p>
          <p> Python es utilizado por la  Nasa, Google, Instagram y por su puesto protoboard.org</p>
"""


cursoPPP = Course(short_description=description, root=PPP)
cursoPPP.save()

pretest = LearningActivity( name = 'Experiencia Programando', slug = 'Pretest',
    uri = '/survey/EP',
    parent = PPP, root  = PPP,

    heading="¿Que experiencia tienes programando?",
    secondary_text = "Encuesta",
    description = "Antes de empezar, dinos algo sobre tu experiencia en programación",
    image = "https://s3.amazonaws.com/learning-python/survey.jpg",

    choice_exit = False,

    pre_condition_rule = """
if self.objective_status == 'notSatisfied' :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = 'disabled'""",

    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,
    order_in_container = 0
    )
pretest.save()


intro = LearningActivity( name = 'Introducción', slug = 'Intro',
    uri = "/activity/introduccion",
#   lom =
    parent = PPP, root  = PPP,
    heading="Introducción al lenguaje",
    description = "Vemos las principales características del lenguaje y hacemos los primeros ejercicios.",
    image = "https://s3.amazonaws.com/learning-python/python-logo.png",
    secondary_text = "Unidad I",
#   pre_condition_rule = """self.recommendation_value = Text_Verbal.eval(self.user.learningstyleinventory.verbal,self.user.learningstyleinventory.visual)"""  ,
    pre_condition_rule = ""  ,
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
intro.save()


secuencias = LearningActivity( name = 'Secuencias', slug = 'Intro',
    uri = "/activity/secuencias",
#   lom =
    image = "https://s3.amazonaws.com/learning-python/sequence.jpg",
    heading="Objetos Tipo Secuencia",
    description = "Aprenderás a utilizar las Listas, Tuplas y Cadenas",

    parent = PPP, root  = PPP,

#    pre_condition_rule = """self.recommendation_value = Text_Verbal.eval(self.user.learningstyleinventory.verbal,self.user.learningstyleinventory.visual)"""  ,
    pre_condition_rule = ""  ,
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
secuencias.save()


tema_1 = LearningActivity( name = 'Introduccion', slug = 'Intro',
    uri = '/activity/video/intro',
    parent = intro, root  = PPP,
    pre_condition_rule = "",
    post_condition_rule = "",
    heading="Introducción al Lenguaje Python",
    description = "Aprenderás cuales son las caracteristicas del lenguaje.",
    image = "https://s3.amazonaws.com/learning-python/IntroVideo.jpg",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 0
    )
tema_1.save()

tema_2 = LearningActivity( name = 'Ejercicios Basados en Pruebas', slug = 'Ejercicios',
    uri = '/activity/video/ejercicios_basados_en_pruebas',
    parent = intro, root  = PPP,
    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 1
    )
tema_2.save()

tema_3 = LearningActivity( name = 'Ejemplo de Ejercicios', slug = 'Ejemplo',
    uri = '/activity/video/ejemplo_ejercicio',
    parent = intro, root  = PPP,
    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 2
    )
tema_3.save()


EjerciciosIntro = LearningActivity( name = 'Ejercicios', slug = 'Ejercicios',
    uri = "/activity/EjerciciosIntro",
    parent = intro,
    root   = PPP,

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,

    rollup_rule  = "satisfied IF All satisfied",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 3
    )
EjerciciosIntro.save()

program_1 = LearningActivity( name = 'Imprime Hola', slug = 'E1',
    uri = "/program/PPP/1",
    parent = EjerciciosIntro, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 3
    )
program_1.save()


program_2 = LearningActivity( name = '¿Es par?', slug = 'E2',
    uri = "/program/PPP/2",
    parent = EjerciciosIntro, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 5
    )
program_2.save()

program_3 = LearningActivity( name = 'Suma dos números', slug = 'E3',
    uri = "/program/PPP/3",
    parent = EjerciciosIntro, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 7
    )
program_3.save()


program_4 = LearningActivity( name = 'distancia()', slug = 'E4',
    uri = "/program/PPP/4",
    parent = EjerciciosIntro, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 9
    )
program_4.save()


program_5 = LearningActivity( name = 'mayor()', slug = 'E5',
    uri = "/program/PPP/5",
    parent = EjerciciosIntro, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 11
    )
program_5.save()

secuencias_1 = LearningActivity( name = 'Video', slug = 'Intro',
    uri = '/activity/video/secuencias',
    parent = secuencias, root  = PPP,
    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,
    order_in_container = 0
    )
secuencias_1.save()

EjerciciosSec = LearningActivity( name = 'Ejercicios', slug = 'Ejercicios',
    uri = "/activity/EjerciciosSec",
    parent = secuencias,
    root   = PPP,

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,

    rollup_rule  = "satisfied IF All satisfied",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 3
    )
EjerciciosSec.save()


program_6 = LearningActivity( name = 'Dame una lista', slug = 'E6',
    uri = "/program/PPP/6",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 8
    )
program_6.save()


program_7 = LearningActivity( name = 'Dame una tupla', slug = 'E7',
    uri = "/program/PPP/7",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 10
    )
program_7.save()

program_8 = LearningActivity( name = 'Solo una tajada', slug = 'E8',
    uri = "/program/PPP/8",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 12
    )

program_8.save()

program_9 = LearningActivity( name = 'Solo una tajadita', slug = 'E9',
    uri = "/program/PPP/9",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 14
    )
program_9.save()

program_10 = LearningActivity( name = '¡Pura Acción!', slug = 'E10',
    uri = "/program/PPP/10",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 16
    )
program_10.save()

program_11 = LearningActivity( name = 'Mutantes', slug = 'E10',
    uri = "/program/PPP/11",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 18
    )
program_11.save()

program_12 = LearningActivity( name = 'Ordena la Lista', slug = 'E10',
    uri = "/program/PPP/12",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 20
    )
program_12.save()


program_13 = LearningActivity( name ='Producto punto' , slug = 'E10',
    uri = "/program/PPP/13",
    parent = EjerciciosSec, root  = PPP,
    pre_condition_rule = """
if self.num_attempts == 0 :
    self.pre_condition = 'stopForwardTraversal'
else:
    self.pre_condition = ''""",
    post_condition_rule = "",

    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,    order_in_container = 22
    )
program_13.save()



User.objects.filter(username='ana').delete()
User.objects.filter(username='paul').delete()

j = User.objects.create_user('ana', 'lennon@thebeatles.com', '1234')
j.is_active = True
j.save()

p = User.objects.create_user('paul', 'paul@thebeatles.com', '1234')
p.is_active = True
p.save()

lsj=LearningStyleInventory(visual=12,verbal=11,aural=15,physical=9,logical=11,
                          social=9, solitary=10, user = j)
lsj.save()

lsp=LearningStyleInventory(visual=12,verbal=11,aural=20,physical=9,logical=11,
                          social=9, solitary=7, user = p)
lsp.save()


s = SimpleSequencing()
s.assignActivityTree(j,PPP)
s.assignActivityTree(p,PPP)


estudiantes = [
('edgar',          '1234',17,13,16,12,14,16, 9),
('osuna',       '1234',15,12,14,18,14,19, 8),
('malu',         '1234', 7,10, 4, 8,17,14,16),
('jose',        '1234',17, 6,16,13,14,11, 8),
('david',         '1234',15,10,13,14,17,15,11),
('juan',    '1234',11,13,11,10,13,18, 8),
('cota',              '1234',13, 7,18,14,12,10,13),
('omar',            '1234', 7, 3, 7,12,16,17, 6),
('santana',           '1234',10, 9,13,13,13,14,13),
('hector',  '1234', 1,11,11,11,18,13,13),
('edie',           '1234',14, 6,16,12,12,13,12),
('baby',      '1234',15,18,20,17,13,18,17),
('saul',            '1234',13,11,14,11,14,14,13),
('brenda',             '1234',17,13,20,12,14,11,16),
('samara',         '1234',14,15,13,12,15,16,12),
('daniel',      '1234', 9, 8,15,11,13,14,13),
('jorge',           '1234',17,12,14,17,19,18,14),
('mike',             '1234',15,16,17,18,18,13,11),
('luis',            '1234',11, 7,11,10,11,12, 6),
('anguiano.ae22@hotmail.com',       '1234',12,10,12,13,10,18,10)]

for e in estudiantes:
    User.objects.filter(username=e[0]).delete()
    u = User.objects.create_user(e[0],e[0], e[1])
    u.is_active = True
    u.save()
    lsu=LearningStyleInventory(visual=e[2],verbal=e[3],aural=e[4],physical=e[5],logical=e[6],
                          social=e[7], solitary=e[8], user = u)
    lsu.save()
    ss = SimpleSequencing()
    ss.assignActivityTree(u,PPP)


import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")

