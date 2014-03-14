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
POO = LearningActivity( name = 'Intro a la POO', slug = 'POO',
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
        <p> Ya deberías saber programación básica en algún lenguaje de programación.</p>"""


cursoPOO = Course(short_description=description, root=POO)
cursoPOO.save()


pretest = LearningActivity( name = 'Pretest', slug = 'Pretest',
    uri = "/test/Pretest",
#   lom = ,
    parent = POO, root  = POO,

    pre_condition_rule = """if self.num_attempts == 0 :
 self.pre_condition = 'stopForwardTraversal'
else:
 self.pre_condition = 'hidden'""",
    post_condition_rule = "" ,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    choice_exit = False,


    is_container = False,
    is_visible = False,
    order_in_container = 1
    )
pretest.save()




content = LearningActivity( name = 'Contenido', slug = 'Contenido',
    uri = "/activity/Contenido",
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

    rollup_rule  = "satisfied IF Any satisfied",
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

    pre_condition_rule = """if self.get_objective_measure('Pretest')  > 2:
	                  self.pre_condition = 'skip' """,
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
    is_visible = True,    order_in_container = 2
    )
program_2.save()

objetosyclases = LearningActivity( name = 'Objetos y Clases', slug = 'OBJETOS_CLASES',
    uri = "/activity/Objetos_y_Clases",
#   lom =
    parent = content, root  = POO,

#   pre_condition_rule = """self.recommendation_value = Text_Verbal.eval(self.user.learningstyleinventory.verbal,self.user.learningstyleinventory.visual)"""  ,

    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = False,
    order_in_container = 1
    )
objetosyclases.save()


objetos_y_clases_html = LearningActivity( name = 'Objetos y Clases HTML', slug = 'OBJETOS_CLASES_HTML',
    uri = "/activity/Objetos_y_Clases_HTML",
#    lom =
    parent = objetosyclases, root   = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = False,

    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = True,
    order_in_container = 0
    )
objetos_y_clases_html.save()

objetos_y_clases_YouTube = LearningActivity( name = 'Objetos y Clases YouTube', slug = 'OBJETOS_CLASES_YouTube',
    uri = "/activity/Objetos_y_Clases_YouTube",
#    lom =
    parent = objetosyclases, root   = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,

    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = True,
    order_in_container = 1
    )
objetos_y_clases_YouTube.save()



encapsulacion = LearningActivity( name = 'Encapsulacion', slug = 'Encapsulacion',
    uri = "/activity/encapsulacion",
#   lom =
    parent = content, root  = POO,

#    pre_condition_rule = """self.recommendation_value = Text_Verbal.eval(self.user.learningstyleinventory.verbal,self.user.learningstyleinventory.visual)"""  ,
    pre_condition_rule = """self.pre_condition = 'disabled'"""  ,
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,


    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 4
    )
encapsulacion.save()


encapsulacion_intro = LearningActivity( name = 'Encapsulacion Introduccion', slug = 'Encapsulacion_intro',
    uri = "/activity/Encapsulacion_intro",
#    lom =
    parent = encapsulacion, root   = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,

    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = True,
    order_in_container = 0
    )
encapsulacion_intro.save()

encapsulacion_ejemplos = LearningActivity( name = 'Encapsulacion Ejemplos', slug = 'Encapsulacion_ejemplos',
    uri = "/activity/Encapsulacion_Ejemplos",
#    lom =
    parent = encapsulacion, root   = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,

    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = True,
    order_in_container = 1
    )
encapsulacion_ejemplos.save()

herencia = LearningActivity( name = 'Herencia', slug = 'Herencia',
    uri = "/activity/Herencia",
#    lom =
    parent = content, root   = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,

    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = True,
    order_in_container = 7
    )
herencia.save()

polimorfismo = LearningActivity( name = 'Polimorfismo', slug = 'polimorfismo',
    uri = "/activity/Polimorfismo",
#    lom =
    parent = content, root   = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,

    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = True,
    order_in_container = 14
    )
polimorfismo.save()


posttest_root = LearningActivity( name = 'Post', slug = 'Post',
    uri = "/activity/Post",
    parent = POO,
    root   = POO,

    flow = True,
    forward_only = False,
    choice = True,
    choice_exit = False,

    rollup_rule  = "satisfied IF Any satisfied",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 4
    )
posttest_root.save()

posttest1 = LearningActivity( name = 'Posttest', slug = 'posttest',
    uri = "/test/Posttest1",
#   lom = ,
    parent = posttest_root, root  = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,

    choice_exit = False,
    is_container = False,
    is_visible = True,
    order_in_container = 23
    )
posttest1.save()

posttest2 = LearningActivity( name = 'Posttest2', slug = 'posttest',
    uri = "/test/Posttest2",
#   lom = ,
    parent = posttest_root, root  = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,

    choice_exit = False,
    is_container = False,
    is_visible = True,
    order_in_container = 24
    )
posttest2.save()





# posttest = LearningActivity( name = 'Posttest', slug = 'posttest',
#     uri = "/test/Posttest",
# #   lom = ,
#     parent = POO, root  = POO,
#
#     pre_condition_rule = """if self.num_attempts == 0 :
#                   self.pre_condition = 'stopForwardTraversal' """,
#     post_condition_rule = "",
#
#     rollup_rule  = "",
#     rollup_objective = True,
#     rollup_progress = True,
#
#     choice_exit = False,
#     is_container = False,
#     is_visible = True,
#     order_in_container = 23
#     )
# posttest.save()

comentario_final = LearningActivity( name = 'Comentario_final', slug = 'comentario_final',
    uri = "/activity/Comentario_final",
#    lom =
    parent = POO, root   = POO,

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,

    rollup_objective = True,
    rollup_progress = True,
    is_container = False,
    is_visible = True,
    order_in_container = 34
    )
comentario_final.save()

##
##
##
## Example of two Users
##
##

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

s = SimpleSequencing()
s.assignActivityTree(j,POO)
s.assignActivityTree(p,POO)


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
    ss.assignActivityTree(u,POO)


import os

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")

##
##
## Assign Activity to both Users
##
##

#
# poo =UserLearningActivity.objects.filter(learning_activity__uri = "/activity/POO" ,user = User.objects.filter(username='paul')[0] )[0]
# ss = SimpleSequencing()


#
#
#a = ss.get_nav(poo)
#print ss.nav_to_xml(root=a)
#
#
#pre_j = UserLearningActivity.objects.filter(learning_activity__name = "Pretest" ,user = j )[0]
#s.set_current(pre_j)
#
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)
#
#s.exit(pre_j, objective_measure = 0.20, objective_status = 'satisfied')
#
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)

#
#s.set_current(j,remediation)
#s.exit(j,remediation, objective_measure = 0.80, objective_status = 'satisfied')
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)
#
#
#s.set_current(j,general)
#s.exit(j,general, objective_measure = 0.80, objective_status = 'satisfied')
#a = s.get_nav(root)
#print s.nav_to_xml(root=a)


#root = UserLearningActivity.objects.filter(learning_activity__name = "Unit" ,user = j )[0]
#c = s.get_nav(root)
#print "-"*20
#print s.xml_children(root=c)
#
#s.set_current(j,general)
#s.exit(j, general, objective_measure = 0.80, objective_status = 'satisfied')
#root = UserLearningActivity.objects.filter(learning_activity__name = "Unit" ,user = j )[0]
#c = s.get_nav(root)
#print "-"*20
#print s.xml_children(root=c)


  