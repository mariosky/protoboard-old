# -*- coding: utf-8 -*-
__author__ = 'mariosky'

activities = { '/test/Pretest':{
    'questions':  [{'id': 1324,
                    'title': "Pregunta Abierta",
                    'question': "Son paises de America del Norte",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Mexico","USA","Nicaragua","España"],
                    'answer': [1,1,0,0],
                    'answer_text': "Solo son México y USA",
                    'hints': ["España está en Europa", "Nicaragua es de Sudamérica"],
                    'image':"images/test.jpg"
                    },
                    {
                    'id':1323,
                    'title': "Pregunta Abierta",
                    'question': "Son lenguajes de programación orientado a objetos",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["C","Java","Fortran","C++"],
                    'answer': [0,1,0,1],
                    },
                    {
                    'id':1311,
                    'title': "Pregunta Abierta",
                    'question': "Cual fué la primera selección en ganar el primer mundial",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Brasil","Uruguay","Italia","Alemania"],
                    'answer': [0,1,0,0],
                    }


                    ],
    'intro':"""<h3>Evaluación Previa</h3>
    <p> Contesta las preguntas, eligiendo la opción mas adecuada de la lista </p>""",
    'bye':"""<p> Gracias </p>"""
                    }
}


