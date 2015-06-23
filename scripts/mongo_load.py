# -*- coding: utf-8 -*-
#!/usr/bin/env python

activities = [
    {
     '_id':'/activity/video/lo-que-ahora-sabemos',
    'title':u'Introducción',
     'url':u"https://www.youtube.com/watch?v=GUxyQ6Mj_kc",
     'youtube_id':'GUxyQ6Mj_kc'

    },
    {
 '_id':'/activity/Preliminar',
  'content':u"""
    <h3> ¿Qué es Orientado a Objetos?</h3>
          <p> La P.O.O. (también conocida como O.O.P., por sus siglas en inglés) es lo que se conoce como un paradigma o modelo de programación.
          Esto significa que no es un lenguaje específico, o una tecnología, sino una forma de programar, una manera de plantearse la programación.
          No es la única (o necesariamente mejor o peor que otras), pero se ha constituido en una de las formas de programar más populares
          e incluso muchos de los lenguajes que usamos hoy día lo soportan o están diseñados bajo ese modelo (PHP, ActionScript, C#, Java).</p>
          <p>
          Lo que caracteriza a la POO es que intenta llevar al mundo del código lo mismo que encontramos en El Mundo Real™.
          Cuando miramos a nuestro alrededor ¿qué vemos? pues, cosas, objetos, pero podemos reconocer estos objetos porque cada objeto pertenece a una clase,
           eso nos permite distinguir, por ejemplo, un perro de un auto (porque son de clases diferentes) y también un TV de otro (porque, aunque sean iguales,
           cada uno es un objeto distinto). Éste es el modelo que la POO intenta seguir para estructurar un sistema.
          </p>
          <p>
          Es importante recalcar nuevamente que la POO no es un lenguaje de programación, es una forma de enfrentarse a ella.
           Esto significa que la POO le servirá para desarrollar en muchos de los lenguajes comunes de hoy en día
            manteniendo un mismo esquema mental. Incluso le permitirá enfrentar otros proyectos que no necesariamente estén relacionados con
          escribir código.
          </p>
         <q>Programación Orientada a Objetos,</span> by <a rel="cc:attributionURL" href="http://thefricky.wordpress.com/poo/">César Frick</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Reconocimiento 3.0 Unported License</a>.</q>
"""},


    {'_id':'/activity/video/startup/business-model-canvas',
     'title':u'Introducción',
     'url':u"http://www.youtube.com/embed/qM5nKU40KVg?rel=0",
     'youtube_id':'iUrrwxOG9uU'

     } ,


    {'_id':'/activity/video/intro',
     'title':u'Introducción',
     'url':u"http://www.youtube.com/embed/qM5nKU40KVg?rel=0",
     'youtube_id':'iUrrwxOG9uU',
     'startSeconds':20,
     'endSeconds':25,
     },

    {'_id':'/activity/video/tomala',
     'title':u'Secuencias:Listas, Tuplas y Cadenas',
     'url':u"http://www.youtube.com/embed/aTDJDB_ZjXA?rel=0",
      'youtube_id':'KovkopcILQ8'} ,

    {'_id':'/activity/video/secuencias',
     'title':u'Secuencias:Listas, Tuplas y Cadenas',
     'url':u"http://www.youtube.com/embed/aTDJDB_ZjXA?rel=0",
      'youtube_id':'KovkopcILQ8'} ,


    { '_id':'/activity/video/ejercicios_basados_en_pruebas',
       'title':u'Ejercicios Basados en Pruebas',
       'url':u"http://www.youtube.com/embed/6BL6P48r_9A?rel=0",
      'youtube_id':'iUrrwxOG9uU'} ,

    {'_id':'/activity/video/ejemplo_ejercicio',
     'title':u'Ejercicios en Protoboard',
     'url':u"http://www.youtube.com/embed/Htk9KAl1GxU?rel=0",
     'youtube_id':'Htk9KAl1GxU'} ,

    {'_id':'/activity/PB',
      'content':u""},


    {'_id':'/activity/introduccion',
     'content' : u""" <h3>Introducción</h3>
                <p> Empezamos con una serie de videos introductorios al tutorial y después EJERCICIOS. </p>
    """} ,



    {'_id':'/program/POO/2', 'title':u"Imprime Hola",
            'initial_code':u"""
# Funcion que imprime Hola
def foo():
    pass
""",
            'correct_code':u"""# Solution:
def foo(l):
    print 'hola'
    """,
            'instructions':u"""<p>Escribe una función llamada foo la cual imprima Hola.</p>
            </code>""",
            'unit_test':u"""
class Test(unittest.TestCase):
    def test_foo(self):
        from StringIO import StringIO
        saved_stdout = sys.stdout
        output = None
        try:
            out = StringIO()
            sys.stdout = out
            foo()
            output = out.getvalue().strip()
            assert output == 'Hola'
        finally:
            sys.stdout = saved_stdout
            print output
""","lang":"python", "type":"unit_test" },

    {'_id':'/program/POO/1',
     'title':u"Clase Producto",
     'initial_code':u"""
using System.IO;
using System;
public class Product
{
        public   code;
        public   desc;

        public Product(int c, string d)
        {
        code=c;
        desc=d;
        }

        public void Print()
        {
        Console.WriteLine("Producto {0}: {1}", code,desc);
        }

}
""",
            'correct_code':u""" """,
             'instructions':u"""


      <button class="btn btn-default" data-toggle="modal" data-target=".bs-example-modal-lg">Leer Detalle</button>
      <div class="modal fade bs-example-modal-lg" tabindex="-1" role="dialog" aria-labelledby="myLargeModalLabel" aria-hidden="true">
      <div class="modal-dialog modal-lg">
      <div class="modal-content">
      <div class="modal-header">
        <button type="button" class="close" data-dismiss="modal" aria-hidden="true">&times;</button>
        <h4 class="modal-title" id="myModalLabel"> Secuenciado </h4>
      </div>
 <div class="modal-body">

      <h3>Introducción</h3>
		<p>
		    Aprender a programar de forma autodidácta puede ser una tarea difícil. No sabemos por donde empezar, ¿que material debo leer
		    primero?, ¿que ejercicios son los adecuados, para mi habilidad actual?, ¿que necesito instalar para empezar?,¿veo videos o leo?.
			Uno de los problemas de la Web es que nos podemos perder entre tanta información, todos los recursos necesarios pueden estar ahí, pero
			   ¿cual podría ser una secuencia adecuada para visitarlos?.
		</p>
		<p>
		   Para Protoboard nos basamos en una especificación llamada <a href="http://www.imsglobal.org/simplesequencing/"> IMS Simple Sequencing Specification (SS) </a>,
		   la cual sirve para 	"representar el  comportamiento deseado en una experiencia de aprendizaje", básicamente es una manera de especificar
		   como se deberían ir entregando las actividades de aprendizaje a los alumnos. No pretendemos cumplir totalmente con la especificación y más bien
		   se ha ido adaptando a nuestras necesidades. Trabajaremos en lograr que el sequenciado se adapte a los usuarios utilizando técnicas de
		   personalización y sistemas de recomendación. Por ejemplo:
		 </p>
		   <ul>
              <li> Agregando reglas difusas para especificar el secuenciado.</li>
              <li> Implementando un sistema de recomendación híbrido para proponer actividades de aprendizaje.</li>
		      <li> Proponiendo un modelo para medir de manera indirecta el nivel de fluidez que experimenta el
                 estudiante para sugerirle ejercicios adecuados</li>
              <li> Considerar información  contexto en los algoritmos de recomendación </li>
           </ul>

			<img src="https://s3.amazonaws.com/mariogarcia/images/ActivityTree.png" class="img-responsive" alt="Responsive image">



      </div>
     </div>
     </div>
     </div>

      <h3 id="welcome">Bienvenidos</h3>
  <p>
		   Para Protoboard nos basamos en una especificación llamada <a href="http://www.imsglobal.org/simplesequencing/"> IMS Simple Sequencing Specification (SS) </a>,
		   la cual sirve para 	"representar el  comportamiento deseado en una experiencia de aprendizaje", básicamente es una manera de especificar
		   como se deberían ir entregando las actividades de aprendizaje a los alumnos. No pretendemos cumplir totalmente con la especificación y más bien
		   se ha ido adaptando a nuestras necesidades. Trabajaremos en lograr que el sequenciado se adapte a los usuarios utilizando técnicas de
		   personalización y sistemas de recomendación. Por ejemplo:
		 </p>
		   <ul>
              <li> Agregando reglas difusas para especificar el secuenciado.</li>
              <li> Implementando un sistema de recomendación híbrido para proponer actividades de aprendizaje.</li>

           </ul>
   	<img src="https://s3.amazonaws.com/mariogarcia/images/ActivityTree.png" class="img-responsive" alt="Responsive image">

<button class="btn btn-info" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
  Ayuda
</button>
<div class="collapse" id="collapseExample">
  <div class="well">
    En este ejemplo debes de agregar algo como:
    <code>
                <p>>>> suma(3,4)</p>
                <p>7</p>
                <p>>>> suma(3,-4)</p>
                <p>-1</p>
    </code>
  </div>
</div>



             """,
            'unit_test':u"""
[TestFixture]
public class ProductTest
{

    [Test, Description("Prueba del Constructor")]
    public void Constructor()
    {
        Product p = new Product(1,"hola");
        // Constraint Syntax
        Assert.AreEqual(p.code,1);
    }


    [Test, Description("Imprimir la Descripción")]
    public void PrintTest()
    {
        Product p = new Product(1,"hola");
        p.Print();

        using (StringWriter sw = new StringWriter())
        {
            Console.SetOut(sw);


            p.Print();

        string expected = "Producto 1: hola";
        StringAssert.StartsWith(expected, sw.ToString());


        }

    }
}""",
     "lang":"csharp",
     "type":"unit_test" },

    {'_id': '/program/PPP/3',
     'title':u"Suma dos números",
            'initial_code':u"""
# Funcion que suma dos números
def suma():
    pass
""",
            'correct_code':u"""# Solution:
def suma(a,b):
    return a + b""",
            'instructions':u"""<p>Escribe una función llamada <code> suma() </code> la cual reciba como parámetros
                dos enteros y regrese la suma de ambos.</p>
            <code>
                <p>>>> suma(3,4)</p>
                <p>7</p>
                <p>>>> suma(3,-4)</p>
                <p>-1</p>
            </code>""",
            'unit_test':u"""
class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_suma_positivos(self):
        self.assertEqual(suma(3,9),12)
    def test_negativos(self):
        self.assertEqual(suma(5,-12),-7)
"
print json.dumps(result)
""", "lang":"python", "type":"unit_test"  },





    {'_id':'/test/Pretest',

    'questions':  [{'id': 1324,
                    'interaction': 'choiceInteraction',
                    'inline': 0 ,
                    'title': "Pregunta Abierta",
                    'question': "Son paises de America del Norte",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Mexico","USA","Nicaragua","España"],
                    'answer': [1,1,0,0],
                    'answer_text': "Solo son México y USA",
                    'hints': ["España está en Europa", "Nicaragua es de Sudamérica"]
                    },
                    {
                    'id':1323,
                    'interaction': 'choiceInteraction',
                    'inline': 1,
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
                    'interaction': 'textEntryInteraction',
                    'inline': 0,
                    'title': "Pregunta Abierta",
                    'question': "Cual fué la primera selección en ganar el primer mundial",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': [],
                    'type':"str",
                    'answer': ["Uruguay", "uruguay"],
                    }
                    ],
    'intro':"""<h3>Evaluación Previa</h3>
    <p> Contesta las preguntas, eligiendo la opción mas adecuada de la lista </p>""",
    'bye':"""""",
     'satisfied_at_least':3
                    },
    {'_id':'/test/poo',
    'questions':  [{'id': 1,
                    'interaction': 'simpleChoice',
                    'inline': 0,
                    'title': "Pregunta Abierta",
                    'question': "La Programación Orientada a Objetos es:",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Es un  programa parecido a Visual Studio",
                                "Un lenguaje de programación basado en Java ",
                                "Un Paradigma o Modelo de Programación",
                                "Un estándar de programación apoyado por Microsoft y Apple"],
                    'answer': [0,0,1,0],
                    'answer_text': "Es un paradigma de programación",
                    'hints': []
                    },
                    {
                    'id':2,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "¿Donde se especifican los atributos y comportamiento que tendrá un conjunto de objetos?",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Un Arreglo",
                                "La Clase",
                                "Un objeto instancia",
                                "En C#"],
                    'answer': [0,1,0,0],

                    },
                    {
                    'id':3,
                    'title': "Pregunta Abierta",
                    'interaction': 'simpleChoice',
                    'inline': 0,
                    'question': "¿Como se determina el estado de un objeto?",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Es el conjunto de atributos y sus valores actuales",
                                "El estado se indica en la clase",
                                "No se puede",
                                "Un objeto no tiene estado"],
                    'answer': [1,0,0,0],
                    },
                    {
                    'id': 4,
                    'interaction': 'simpleChoice',
                    'inline': 0,
                    'title': "Pregunta Abierta",
                    'question': "¿Que otro nombre reciben los objetos?",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Clases básicas",
                                "Instancias",
                                "Entidades",
                                "Agentes"],
                    'answer': [0,1,0,0],
                    }
                    ],
    'intro':"""<h3>Evaluación Final</h3>
    <p> Contesta las preguntas, eligiendo la opción mas adecuada de la lista </p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },

    {'_id':'/program/PPP/2000',
     'title':u"Clase Producto",
     'initial_code':u"""
using System.IO;
using System;
public class Product
{
        public   code;
        public   desc;

        public Product(int c, string d)
        {
        code=c;
        desc=d;
        }

        public void Print()
        {
        Console.WriteLine("Producto {0}: {1}", code,desc);
        }

}
""",
            'correct_code':u""" """,
             'instructions':u"""<p>Completa la clase llamada <code> Producto </code> """,
            'unit_test':u"""
[TestFixture]
public class ProductTest
{

    [Test, Description("Prueba del Constructor")]
    public void Constructor()
    {
        Product p = new Product(1,"hola");
        // Constraint Syntax
        Assert.AreEqual(p.code,1);
    }


    [Test, Description("Imprimir la Descripción")]
    public void PrintTest()
    {
        Product p = new Product(1,"hola");
        p.Print();

        using (StringWriter sw = new StringWriter())
        {
            Console.SetOut(sw);


            p.Print();

        string expected = "Producto 1: hola";
        StringAssert.StartsWith(expected, sw.ToString());


        }

    }
}""",
     "lang":"csharp" }

    ]





import os

if __name__ == "__main__":
     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")
     from pymongo import MongoClient
     from django.conf import settings
     client = MongoClient(settings.MONGO_DB)
     db = client.protoboard_database

     activities_collection = db.activities_collection
     activities_collection.remove()
     activities_collection.insert(activities)

     a = activities_collection.find_one({'_id':'/program/PPP/2000'})
     print a['instructions']

     #activities_collection.remove()
     #activities_collection.insert(activities)


