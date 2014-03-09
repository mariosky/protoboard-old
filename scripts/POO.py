__author__ = 'mariosky'

##
##  Jugando con la idea de crear los cursos a partir de
##  Doctos YAML
##
import yaml

YAML = """/activity/POO:
    name : Intro a la POO
    flow : True
    forward_only : False
    choice : True
    rollup_rule : satisfied IF All satisfied
    rollup_objective : True,
    rollup_progress : True,
    is_visible : True,

/test/Pretest:
    name : Pretest
    slug : Pretest
    pre_condition_rule : |
        if 1 == 1 :
            print 'stopForwardTraversal'
    is_visible : False"""

tree = """
    activity/POO:
        - test/Pretest:
            - activity/asdasd
        - test/Pxx:
            - test/Pxxx:
        - test/Pxxxs
        - test/Pxaa"""


print yaml.load(YAML)

d =  yaml.load(YAML)

print type(d['/test/Pretest']['pre_condition_rule'])

exec(d['/test/Pretest']['pre_condition_rule'])

print yaml.load(tree)
