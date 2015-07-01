# -*- coding: utf-8 -*-
#!/usr/bin/env python

activities = [

    {
 '_id':'/activity/SecuenciadoSimple',
  'content':u"""
        <h3>Introducción</h3>
		<p>
		    Aprender a programar de forma autodidácta puede ser una tarea difícil. No sabemos por donde empezar, ¿que material debo leer
		    primero?, ¿que ejercicios son los adecuados, para mi habilidad actual?, ¿que necesito instalar para empezar?,¿veo videos o leo?.
			Uno de los problemas de la Web es que nos podemos perder entre tanta información, todos los recursos necesarios pueden estar ahí, pero
			   ¿cual podría ser una secuencia adecuada para visitarlos?.
		</p>
		<p>
		   Para Protoboard nos basamos en una especificación llamada <a href="http://www.imsglobal.org/simplesequencing/"> IMS Simple Sequencing Specification (SS) </a>,
		   la cual sirve para <em>representar el  comportamiento deseado en una experiencia de aprendizaje </em>, básicamente es una manera de especificar
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
          <p>
             Con este demo  iremos probando la funcionalidad básica de la plataforma sin agregar todavía los módulos de personalización,
             ya que ésta es una nueva versión en desarrollo.
          </p>
          <p>

              Se irán explicando a lo largo del demo las capacidades de secuenciado y el
             tipo de actividades de aprendizaje implementadas. En las explicaciones se tratará de reducir al mínimo
             el uso de términos técnicos de computación. Bueno ya empezamos mal.
          </p>
        <h3> Arbol de Secuencia</h3>
    <p> Cuando un instructor planea un curso en línea o presencial, podría empezar por  decidir y organizar los temas
        y objetivos didácticos que cubrirá en el curso. Adecuarlos al tiempo disponible y nivel académico de sus alumnos.
        Una forma muy común de organización es emplear un árbol de tres niveles: Unidad-Tema-Actividades, las plataformas
        más populares de cursos en línea utilizan esta estructura. En la especificación SS se generaliza la solución a un
        árbol de <strong>n</strong> niveles. Solo las hojas del arbol representan actividades de aprendizaje o recursos
        didácticos con los que interactuarán los alumnos. Estas actividades de aprendizaje se llaman también objetos de
        aprendizaje ya que son auto contenidos y pueden reutilizarse en varios cursos. A los otros nodos podemos verlos como
        contenedores, igual que en las carpatas de archivos en la computadora. Los contenedores pueden corresponder a objetivos de
        aprendizaje o niveles jerárquicos de organización como unidades, temas, subtemas, etc.
    </p>
    <p>
        Una secuencia de dichas actividades puede establecerse al recorrer el árbol en pre-orden. Utilizando reglas de secuencia se pueden
        omitir algunos nodos con todo y sus descendientes. Por ejemplo en la figura se puede omitir el recurso <code> AAB </code> o el contenedor <code>AB</code>
    </p>
			<img src="https://s3.amazonaws.com/mariogarcia/images/ActivityTree.png" class="img-responsive" alt="Responsive image">

    <p> Las reglas se estipulan en el lenguaje python y pueden hacer referencia al <em> árbol de secuenciado</em> un árbol donde se lleva el avance que
     a tenido el alumno en un curso en particular. Por ejemplo la regla:
        <pre>
pre_condition_rule = \"\"\"
if get_attr('/activity/SecuenciadoSimple','objective_status') == 'satisfied':
    activity['pre_condition'] = 'hidden'
else:
    activity['pre_condition'] = ''
\"\"\",
        </pre>

 <p> Ocultaría esta actividad después de visitarla una vez. </p>
    <p> This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Reconocimiento 3.0 Unported License</a>.</q>
</p>"""},


    {'_id':'/activity/video/intro',
     'title':u'Ejemplo de video',
     'url':u"http://www.youtube.com/embed/qM5nKU40KVg?rel=0",
     'youtube_id':'iUrrwxOG9uU',
     'startSeconds':0,
     'endSeconds':10,
      'content' : u"""
                <p> Este video salta a la siguiente actividad después de 10 segundos. </p>
                  """

     },


    {'_id':'/test/demo',

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
                    'question': "Cual fué la primera selección en ganar el mundial de Fútbol",
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


{'_id':'/program/csharp/1',
     'title':u"product.cs",
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




<h4>La clase <code>Product</code> tiene errores</h4>
  <p>
       La clase <code>Product</code> se utiliza en un programa de la siguiente manera:
  </p>

<pre>
Product p = new Product(1, "iPhone 6");
p.Print();
</pre>
  <p>
       Completa el código para que funcione.
  </p>

<row>
<button class="btn btn-info" type="button" data-toggle="collapse" data-target="#collapseExample" aria-expanded="false" aria-controls="collapseExample">
  Ayuda
</button>
</row>
<div class="collapse" id="collapseExample">
  <div class="well">
  <p>
    En C# al declarar los campos debes indicar su tipo de dato. Por ejemplo:
    </p>
<pre>
public int intentos;
public string email;</pre>
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








    {'_id':'/program/js/1', 'title':u"suma.js",
                'initial_code':u"""//Completa el código

 function suma(a, b){
    return ;
 }
                                """,
                'correct_code':u"""""",
                'instructions':u"""<p>Escribe una función llamada <code>suma</code> la cual tome dos argumentos <code>a</code> y <code>b</code> y regrese la
                                        suma de ambos.</p> </code>""",
                'unit_test':u"""
                    QUnit.test("JQuery", function( assert ) {
                        assert.equal(suma(2,3), 5, "Debe sumar positivos");
                        assert.equal(suma(2,-3), -1, "Debe sumar negativos");
                        });""",
                "lang":"javascript",
                "type":"unit_test" },



    {'_id':'/program/js/2', 'title':u"titulo.js",
                'initial_code':u"""//Corrige el código

$('.panel-title').html("Hola");
                                """,
                'correct_code':u"""
                                    """,
                'instructions':u"""
                <h4> Modificando el texto dentro de un elemento</h4>

                <p> Podemos utilizar JQuery para cambiar el texto de un elemento en particular.  Primero buscamos el
                elemento, si el elemento tiene un <code> id </code> es fácil, lo encontramos con el selector <code> # </code>.
                Una vez que lo tenemos  modificamos el texto con la función <code>html()</code>.

                <h4> Instrucciones</h4>

                Cambia el titulo del HTML Renderizado en la parte superior, en lugar de Hola debería decir: <strong>Hola JQuery</strong>.</p>

                <h5> El HTML original es el siguiente:</h5>
                """,
                'unit_test':u"""
                    QUnit.test("JQuery", function( assert ) {
                        assert.equal($('#titulo').html(), "Hola JQuery", "El titulo debe decir 'Hola JQuery'");

                        });""",
                'HTML_code': u""" <h3 id='titulo'> Hola </h3> """,
                "CSS": """

                """,
                "lang":"javascript",
                "type":"unit_test",
                "hint":u"""
                Recuerda que se utiliza el selector <code> . </code> para encontrar los elementos que tienen cierta clase.
                En este caso buscamos un <code>id</code>. Algo como:
                <pre>
$('<strong>#</strong>nombre_del_elemento');
                </pre>
                """},



    {'_id':'/program/1', 'title':u"Imprime Hola",
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



    {'_id': '/program/suma/3',
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







    {'_id':'/program/java/1',
     'title':u"Calculator.class",
     'initial_code':r"""
public class Calculator {

  public int evaluate(String expression) {


    return sum;
  }
""",
            'correct_code':u""" """,
             'instructions':u"""<p>Completa el método <code> evaluate </code> de la clase <code>Calculator</code>. Este
              método toma como parámetro una cadena con número enteros y el operador de adición, por ejemplo: <code>"2+2+4+4"</code>
             y regresa un entero con la suma
              de los números, para el caso de ejemplo sería 12.""",
            'unit_test':r"""//CalculatorTest
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class CalculatorTest {
  @Test
  public void evaluatesExpression() {
    Calculator calculator = new Calculator();
    int sum = calculator.evaluate("1+2+3");
    assertEquals(6, sum);
  }
}""",
     "lang":"java" }

    ]





import os

if __name__ == "__main__":
     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protoboard.settings")
     from pymongo import MongoClient
     from django.conf import settings
     client = MongoClient(settings.MONGO_DB)
     db = client.protoboard_database

     activities_collection = db.activities_collection
     #print activities_collection.find_one({'_id':'/activity/Preliminar'})
     activities_collection.remove()
     activities_collection.insert(activities)


     #activities_collection.remove()
     #activities_collection.insert(activities)


