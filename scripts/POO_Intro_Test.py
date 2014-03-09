# -*- coding: utf-8 -*-
from activitytree.models import LearningStyleInventory, LearningActivity, Course
from django.contrib.auth.models import User
from activitytree.interaction_handler import SimpleSequencing

##
##
##  Example of a Learning Activity Tree
##
##



LearningActivity.objects.all().delete()
POO = LearningActivity( name = 'Intro a la POO', slug = 'POO',
    uri = "/activity/POO",
    parent = None,
    root   = None,

    pre_condition_rule = "",
    post_condition_rule = "",

    flow = True,
    forward_only = False,
    choice = True,

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
                  self.pre_condition = 'stopForwardTraversal' """,
    post_condition_rule = "",

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,

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

    match_rule = "",
    filter_rule = "",

    rollup_rule  = "satisfied IF Any satisfied",
    rollup_objective = True,
    rollup_progress = True,
    is_container = True,
    is_visible = False,
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

#   pre_condition_rule = """self.recommendation_value = Text_Verbal.eval(self.user.learningstyleinventory.verbal,self.user.learningstyleinventory.visual)"""  ,

    post_condition_rule = "",

    flow = True,
    forward_only = True,
    choice = False,


    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,

    is_container = True,
    is_visible = True,
    order_in_container = 2
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
    order_in_container = 3
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
    order_in_container = 4
    )
polimorfismo.save()

posttest = LearningActivity( name = 'Posttest', slug = 'posttest',
    uri = "/test/Posttest",
#   lom = ,
    parent = POO, root  = POO,

    pre_condition_rule = """if self.num_attempts == 0 :
                  self.pre_condition = 'stopForwardTraversal' """,
    post_condition_rule = "",

    rollup_rule  = "",
    rollup_objective = True,
    rollup_progress = True,

    is_container = False,
    is_visible = True,
    order_in_container = 3
    )
posttest.save()

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
    order_in_container = 4
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
('edgar.gm1691@gmail.com',          '10211108',17,13,16,12,14,16, 9),
('m.machuca.osuna@gmail.com',       '10211123',15,12,14,18,14,19, 8),
('malu.esquivel@gmail.com',         '10211102', 7,10, 4, 8,17,14,16),
('jose-eleasar@hotmail.com',        '10211156',17, 6,16,13,14,11, 8),
('davidhdez.sin@gmail.com',         '10211090',15,10,13,14,17,15,11),
('chavezjuancarlos12@gmail.com',    '10211607',11,13,11,10,13,18, 8),
('isaicota@gmail.com',              '10211618',13, 7,18,14,12,10,13),
('omar_147@hotmail.com',            '10211166', 7, 3, 7,12,16,17, 6),
('santana77@hotmail.com',           '10211670',10, 9,13,13,13,14,13),
('hector.guerrero.1325@gmail.com',  '10211325', 1,11,11,11,18,13,13),
('edie_1023@hotmail.com',           '10211147',14, 6,16,12,12,13,12),
('chiquibaby1000@hotmail.com',      '10211129',15,18,20,17,13,18,17),
('saulgreen7@gmail.com',            '10211141',13,11,14,11,14,14,13),
('brenda_mcr@live.com',             '10211107',17,13,20,12,14,11,16),
('samara.heba@hotmail.com',         '10211158',14,15,13,12,15,16,12),
('danieladelgado.h@gmail.com',      '10211092', 9, 8,15,11,13,14,13),
('jorge.hrdez@gmail.com',           '10211112',17,12,14,17,19,18,14),
('jonathanbarronleon@gmail.com',    '10211091',14, 5,16,12, 6,12, 7),
('itandreasalgado@gmail.com',       '10211183', 7,12,10, 8,15, 8,11),
('victorpaniagua91@gmail.com',      '10211136', 9,10,11,12,14,20, 9),
('mike.amms@gmail.com',             '10211167',15,16,17,18,18,13,11),
('luisjuan91@gmail.com',            '10211103',11, 7,11,10,11,12, 6),
('link_ztb@hotmail.com',            '10211100', 8, 7, 6,10,13,14,15),
('anguiano.ae22@hotmail.com',       '10211097',12,10,12,13,10,18,10)]

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


  