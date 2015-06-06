# -*- coding: utf-8 -*-
#!/usr/bin/env python




activities = {


'/activity/video/lo-que-ahora-sabemos':
    {'title':u'Introducción',
     'url':u"https://www.youtube.com/watch?v=GUxyQ6Mj_kc",
      'youtube_id':'GUxyQ6Mj_kc'

      },




'/activity/video/intro':
    {'title':u'Introducción',
     'url':u"http://www.youtube.com/embed/qM5nKU40KVg?rel=0",
      'youtube_id':'iUrrwxOG9uU',
      'startSeconds':20,
      'endSeconds':25,

      } ,

'/activity/video/secuencias':
    {'title':u'Secuencias:Listas, Tuplas y Cadenas',
     'url':u"http://www.youtube.com/embed/aTDJDB_ZjXA?rel=0",
      'youtube_id':'KovkopcILQ8'} ,

'/activity/video/ejercicios_basados_en_pruebas':
    {'title':u'Ejercicios Basados en Pruebas',
     'url':u"http://www.youtube.com/embed/6BL6P48r_9A?rel=0",
      'youtube_id':'iUrrwxOG9uU'} ,

'/activity/video/ejemplo_ejercicio':
    {'title':u'Ejercicios en Protoboard',
     'url':u"http://www.youtube.com/embed/Htk9KAl1GxU?rel=0",
      'youtube_id':'Htk9KAl1GxU'} ,

'/activity/PB':u"""<h3 id="welcome">Bienvenidos</h3>
      <p> En este tutorial aprenderás los conceptos básicos de la programación en Python </p>
      <p> Orientado a principiantes muy avanzados, que se maravillen con la simplicidad de este hola mundo: </p>
            <p><code>print "hola mundo"</code></p>
          <p> Python es utilizado por la  Nasa, Google, Instagram y por su puesto protoboard.org</p>
    """,

'/activity/introduccion': u""" <h3>Introducción</h3>
  <p> Empezamos con una serie de videos introductorios al tutorial y después EJERCICIOS.
   </p>

    """ ,
'/activity2/introduccion': u""" <h3>Introducción</h3>
  <p> Empezamos con una serie de videos introductorios al tutorial y después EJERCICIOS.
   </p>

    """ ,

'/activity/secuencias': u""" <h3>Secuencias</h3>
  <p> Tutorial de objetos tipo secuencia, muy útilies y faciles de entender.
   </p>

    """ ,

'/activity/EjerciciosSec': u""" <h3>Ejercicios</h3>
  <p> Ejercicios variados sobre secuencias.
   </p>

    """ ,

'/activity/EjerciciosSec': u""" <h3>Ejercicios</h3>
  <p> Ejercicios variados sobre secuencias.
   </p>

    """ ,

'/activity/EjerciciosIntro': u""" <h3>Ejercicios</h3>
  <p> Pon en práctica lo vista hasta ahora.
   </p>

    """ ,


 '/program/PPP/1':{ 'title':u"Imprime Hola",
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
            'unit_test':u"""import unittest, sys
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False

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

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},

 '/program/PPP/2':
        {   'title':u"¿Es par?",
            'initial_code':u"""
def es_par():
    pass
""",
            'correct_code':u""" """,
             'instructions':u"""<p>Escribe una función llamada <code> es_par </code> la cual tome un
             parámetro entero y regrese <code> True </code> si es entero y <code> False </code>
             si no lo es.</p>
            </code>""",
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_cero(self):
        self.assertEqual(es_par(0),True)
    def test_par(self):
        self.assertEqual(es_par(6),True)

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},


 '/program/PPP/3':
        {   'title':u"Suma dos números",
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
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_suma_positivos(self):
        self.assertEqual(suma(3,9),12)
    def test_negativos(self):
        self.assertEqual(suma(5,-12),-7)

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},

 '/program/PPP/4':
        {   'title':u"distancia()",
            'initial_code':u"""
def distancia():
    pass
""",
            'correct_code':u""" """,
            'instructions':u"""<p>Escribe una función llamada <code> distancia() </code> la cual reciba como parámetros
                dos enteros y regrese el valor absoluto de la diferencia entre ambos</p>
            <code>
                <p>>>> distancia(3,4)</p>
                <p>1</p>
                <p>>>> distancia(3,-4)</p>
                <p>7</p>
            </code>""",
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_distancia_positivos(self):
        self.assertEqual(distancia(3,9),6)
    def test_negativos(self):
        self.assertEqual(distancia(5,-12),17)

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},


'/program/PPP/5':
        {   'title':u"mayor()",
            'initial_code':u"""
def mayor():
    pass
""",
            'correct_code':u""" """,
            'instructions':u"""<p>Escribe una función llamada <code> mayor() </code> la cual reciba como parámetros
                dos enteros y regrese el mayor entre ellos.</p>
            <code>
                <p>>>> mayor(3,4)</p>
                <p>4</p>
                <p>>>> mayor(2,-4)</p>
                <p>2</p>
            </code>""",
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_mayor_positivos(self):
        self.assertEqual(mayor(3,9),9)
    def test_negativos(self):
        self.assertEqual(mayor(5,-12),5)

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},

 '/program/PPP/6':
        {   'title':u"Dame una lista",
            'initial_code':u"""
def regresa_lista():
    return None
""",
            'correct_code':u""" """,
             'instructions':u"""<p>Escribe una función llamada <code> regresa_lista </code> la cual regrese la siguiente lista:
           <code> ["Tom", 2.23, 12]  </code>.
</p>""",
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_lista(self):
        self.assertEqual(type(regresa_lista()),type([1,2]))
    def test_Tom(self):
        self.assertEqual(regresa_lista()[0],"Tom")
    def test_float(self):
        self.assertEqual(regresa_lista()[1],2.23)
    def test_int(self):
        self.assertEqual(regresa_lista()[2],12)
    def test_len(self):
        self.assertEqual(len(regresa_lista()),3)

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},

'/program/PPP/7':
        {   'title':u"Dame una tupla",
            'initial_code':u"""
def regresa_tupla(a,b,c):
    pass
""",
            'correct_code':u""" """,
             'instructions':u"""<p>Escribe una función llamada <code> regresa_tupla </code>
             la cual tome tres parámetros y regrese una tupla con los tres valores.
             </p>
            """,
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_tupla(self):
        self.assertEqual(type(regresa_tupla(1,2,3)),type((1,2)))
    def test_primero(self):
        self.assertEqual(regresa_tupla(1,2,3)[0],1)
    def test_segundo(self):
        self.assertEqual(regresa_tupla(1,2,3)[1],2)
    def test_tercero(self):
        self.assertEqual(regresa_tupla(1,2,3)[2],3)
    def test_len(self):
        self.assertEqual(len(regresa_tupla(1,2,3)),3)
suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},

'/program/PPP/8':
        {   'title':u"Solo una tajada",
            'initial_code':u"""
def recorta(pelicula):
    pass
""",
            'correct_code':u""" """,
             'instructions':u"""<p> Un sistema externo nos envía en una lista información sobre peliculas,
             aquí un ejemplo: <code> ['tt1877832', 'X-Men: Days of Future Past', 2014,
			['Action', 'Adventure', 'Fantasy'], 8.1,  14740 ] </code>  los elementos corresponden secuencialmente a
			Identificador, Titulo, Año, Lista de Generos y Calificación Promedio, Número de votos. Escribe un método
			llamdo <code> recorta(pelicula) </code> que reciba una pelicula representada como lista y regrese
			otra lista que solo incluya Identificador, Titulo y Año. Por ejemplo para la pelicula anterior regresaría
			<code> ['tt1877832', 'X-Men: Days of Future Past', 2014] </code> </p>
            """,
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_corte(self):
        self.assertEqual(recorta(['tt', 'X', 1, [], 1,  1 ]), ['tt', 'X', 1])

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},
'/program/PPP/9':
        {   'title':u"Solo una tajadita",
            'initial_code':u"""
def recorta(pelicula):
    pass
""",
            'correct_code':u""" """,
             'instructions':u"""<p> Un sistema externo nos envía en una lista información sobre peliculas,
             aquí un ejemplo: <code> ['tt1877832', 'X-Men: Days of Future Past', 2014,
			['Action', 'Adventure', 'Fantasy'], 8.1,  14740 ] </code>  los elementos corresponden secuencialmente a
			Identificador, Titulo, Año, Lista de Generos y Calificación Promedio, Número de votos. Escribe un método
			llamado <code> recorta(pelicula) </code> que reciba una pelicula representada como lista y regrese
			otra lista que solo incluya Titulo y Año. Por ejemplo para la pelicula anterior regresaría
			<code> ['X-Men: Days of Future Past', 2014] </code> </p>
            """,
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_corte(self):
        self.assertEqual(recorta(['tt', 'X', 1, [], 1,  1 ]), [ 'X', 1])

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},

'/program/PPP/10':
        {   'title':u"¡Pura Acción!",
            'initial_code':u"""
def es_accion(pelicula):
    pass
""",
            'correct_code':u""" """,
             'instructions':u"""<p> Un sistema externo nos envía en una lista información sobre peliculas,
             aquí un ejemplo: <code> ['tt1877832', 'X-Men: Days of Future Past', 2014,
			['Action', 'Adventure', 'Fantasy'], 8.1,  14740 ] </code>  los elementos corresponden secuencialmente a
			Identificador, Titulo, Año, Lista de Generos, Calificación Promedio y Número de votos. Escribe un método
			llamado <code> es_accion(pelicula) </code> que reciba una pelicula representada como lista y regrese
			<code> True </code> si es pelicula de acción, y <code> False </code> si no lo es.Por ejemplo para la pelicula anterior regresaría
			<code>True </code>, pero para la pelicula <code>['tt2004420', 'Neighbors', 2014, ['Comedy'], 7.2,  26920]</code>
			  regresaría  <code> False </code>.</p>
            """,
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_Action(self):
        self.assertEqual(es_accion(['tt', 'X', 1, ['Action'], 1,  1 ]), True)
    def test_Not_Action(self):
        self.assertEqual(es_accion(['tt', 'X', 1, ['Otra'], 1,  1 ]), False)
suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},


'/program/PPP/11':
        {   'title':u"Mutantes",
            'initial_code':u"""
def activa_usuario(usr):
    pass
""",
            'correct_code':u""" """,
             'instructions':u"""<p> Un sistema externo nos envía en una lista información sobre usuarios,
             aquí un ejemplo: <code> ['812202', 'Ana', 'Activo'] </code>  los elementos corresponden secuencialmente a
			Identificador, Nombre y Status. Status tiene solo dos valores válidos:<code> 'Activo'</code>  e <code> 'Inactivo'</code>   Escribe un método
			llamado <code> activa_usuario(usr) </code> que reciba a un usuario representado como lista, modifique su
			estado a  <code>'Activo'</code> y regrese la lista.</p>

            <div class="alert alert-warning"> Para usuarios más avanzados: Como el usuario es una lista,
          al pasarse como argumento la modificación se realiza a la  referencia por lo que no es necesario regresar la
          lista. Si está en chino no te preocupes, ésto lo explicaremos más adelante.</div>
            """,
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_Action(self):
        self.assertEqual(activa_usuario(['2', 'A', 'Inactivo']) , ['2', 'A', 'Activo'])

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},
'/program/PPP/12':
        {   'title':u"Ordena la Lista",
            'initial_code':u"""
# Funcion que ordena una lista, puedes utilizar sort()
def solution():
    pass
""",
            'correct_code':u"""# Solution:
def solution(l):
    if l is None:
        return []
    else:
        l.sort()
        return l""",
            'instructions':u"""<p>Escribe una función llamada <code>solution</code> la cual reciba como parámetro
                una lista y regrese la lista ordenada.</p>
            <p>En caso de recibir como parámetro el valor <code>None</code> debe regresar una lista vacía. </p>
            <code>
                <p>>>> solution([4,3,5,1])</p>
                <p>[1, 3, 4, 5]</p>
                <p>>>> solution(None)</p>
                <p>[]</p>
            </code>""",
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_order(self):
        self.assertEqual(solution([2,6,1,5]),[1,2,5,6])
    def test_none(self):
        self.assertEqual(solution(None),[])

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},

'/program/PPP/13':
        {   'title':u"Producto punto",
            'initial_code':u"""
def producto(l1,l2):
    pass
""",
            'correct_code':u""" """,
             'instructions':u"""<p> Escribe un método llamado <code> producto(l1, l2) </code> el cual reciba
              dos listas de enteros del mismo tamaño y regrese el producto escalar entre ellas. El producto escalar
              se calcula de la siguiente manera: Tenemos <b>a</b> = [a<sub>1</sub>, a<sub>2</sub> , ... ,a<sub>n</sub>] y
            <b>b</b>  =  [b<sub>1</sub>, b<sub>2</sub> , ... , b<sub>n</sub>] entonces
            <b> a</b> ·<b> b </b>= a<sub>1</sub>b<sub>1</sub> + a<sub>2</sub>b<sub>2</sub> + .. + a<sub>n</sub>b<sub>n</sub> Se suman
             los productos de los elementos con el mismo indice, el primero con el primero, segundo con el segundo, etc.

            </p>
          <div class="alert alert-warning"> Puedes utilizar <code>map</code> y <code>zip</code></div>

            """,
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_Action(self):
        self.assertEqual(producto([2, 1, 3], [2, 3, 1]), 10)
suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},





'/activity/POO':u"""
      <button class="btn btn-info" data-toggle="modal" data-target=".bs-example-modal-lg">Leer</button>
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
          <p>
             Con este demo  iremos probando la funcionalidad básica de la plataforma sin agregar todavía los módulos de personalización,
             ya que esta es una nueva versión en desarrollo.
          </p>
          <p>

              Se irán explicando a lo largo del demo las capacidades de secuenciado y el
             tipo de actividades de aprendizaje implementadas. En las explicaciones se tratará de reducir al mínimo
             el uso de términos técnicos de computación.
          </p>
        <h3> Arbol de Secuencia</h3>
    <p> Cuando un instructor planea un curso en línea o presencial, podría empezar por  decidir y organizar los temas
        y objetivos didácticos que cubrirá en el curso. Adecuarlos al tiempo disponible y nivel académico de sus alumnos.
        Una forma muy común de organización es emplear un árbol de tres niveles: Unidad-Tema-Actividades, las plataformas
        más populares de cursos en línea utilizan esta estructura. En la especificación SS se generaliza la solución a un
        árbol de <strong>n</strong> niveles. Solo las hojas del arbol representan actividades de aprendizaje o recursos
        didácticos con los que interactuarán los alumnos. Estas actividades de aprendizaje se llaman también objetos de
        aprendizaje, ya que son auto contenidos y pueden reutilizarse en varios cursos. A los otros nodos podemos verlos como
        contenedores, igual que en las carpatas de archivos en la computadora. Los contenedores pueden corresponder a objetivos de
        aprendizaje o niveles jerárquicos de organización como unidades, temas, subtemas, etc.
    </p>
    <p>
        Una secuencia de dichas actividades puede establecerse al recorrer el árbol en pre-orden.
    </p>
			<img src="https://s3.amazonaws.com/mariogarcia/images/ActivityTree.png" class="img-responsive" alt="Responsive image">








      </div>
     </div>
     </div>
     </div>
      <h3 id="welcome">Bienvenidos</h3>
      <p> En esta clase aprenderas algunos conceptos básicos de la Programación Orientada a Objetos. </p>
      <p> Como primer paso realizarás un pequeño examen para
          evaluar tus conocimientos de Programación. </p>

    """
,
'/activity/Bienvenidos': u""" <h3 id="welcome">Bienvenidos</h3>
      <p> En esta clase aprenderas algunos conceptos básicos de la Programación Orientada a Objetos. </p>
      <p> Como primer paso realizarás un pequeño examen para
          evaluar tus conocimientos de Programación. </p>
    """ ,

'/activity/Comentario_final': u""" <h3 id="welcome">Comentario Final</h3>
      <p> En esta clase haz visto algunos de los conceptos básicos de la Programación Orientada a Objetos,
     poco a poco, deberas familiarizarte con los téminos y conceptos aquí vistos, ya que son fundamentales
     para entender y explotar al máximo los lenguajes de programación OO.
      </p>
    """ ,

'/activity/Herencia': u"""
<a name="notion" class="ancre"></a>
<h3>El concepto de herencia</h3>
<p align="justify">La <b>herencia</b> es espec&iacute;fica de la programaci&oacute;n orientada a objetos, donde una clase nueva se crea a partir de una clase existente.
La <i>herencia</i> (a la que habitualmente se denomina <i>subclases</i>) proviene del hecho de que la subclase (la nueva clase creada) contiene las atributos y m&eacute;todos de la clase primaria.
 La principal ventaja de la herencia es la capacidad para definir atributos y m&eacute;todos nuevos para la subclase, que luego se aplican a los atributos y m&eacute;todos heredados.
 <br/>Esta particularidad permite crear una estructura jer&aacute;rquica de clases cada vez m&aacute;s especializada. La gran ventaja es que uno ya no debe comenzar desde cero cuando desea especializar
 una clase existente. Como resultado, se pueden adquirir bibliotecas de clases que ofrecen una base que puede especializarse a voluntad
 (la compa&ntilde;&iacute;a que vende estas clases tiende a proteger las datos miembro usando la
        <a href="Encapsulacion_intro">encapsulaci&oacute;n</a>).

<a name="hierarchie" class="ancre"></a>
<h3>Jerarqu&iacute;a de clase</h3>
<p align="justify">La relaci&oacute;n primaria-secundaria entre clases puede representarse desde un punto de vista jer&aacute;rquico, denominado <i>vista de clases en &aacute;rbol</i>.
 La vista en &aacute;rbol comienza con una clase general llamada superclase (a la que algunas veces se hace referencia como <i>clase primaria</i>, <i>clase padre</i>, <i>clase principal</i>, o <i>clase madre</i>;
 existen muchas met&aacute;foras geneal&oacute;gicas). Las clases derivadas (<i>clase secundaria</i> o <i>subclase</i>) se vuelven cada vez m&aacute;s especializadas a medida que van descendiendo el &aacute;rbol.
 Por lo tanto, se suele hacer referencia a la relaci&oacute;n que une a una clase secundaria con una clase primaria mediante la frase "<i>es una</i>" x o y.

<p align="center"><img src="http://static.commentcamarche.net/es.kioskea.net/pictures/poo-images-animaux.gif"alt="Jerarqu&iacute;a de clase" />

<a name="multiple" class="ancre"></a>
<h3>Herencia m&uacute;ltiple</h3>
<p align="justify">Algunos lenguajes orientados a objetos, como C++ permiten herencias m&uacute;ltiples, lo que significa que una clase puede heredar los atributos de otras dos superclases.
Este m&eacute;todo puede utilizarse para agrupar atributos y m&eacute;todos desde varias clases dentro de una sola.
<p align="center"><img src="http://static.commentcamarche.net/es.kioskea.net/pictures/poo-images-animaux2.gif"alt="Herencia m&uacute;ltiple" />



<ul>
 <li>   Muchos objetos se relacionan entre sí, de alguna forma por ejemplo </li>
        <ul>
        <li>Un Libro y sus Autores</li>
        <li>Un objeto instancia de Reservación, relaciona objetos tipo Vuelo y Pasajero.</li>
        </ul>


 <li>  Un tipo de relación muy importante es la de Herencia, la cual nos permite tener una relación tipo-de. por ejemplo:</li>
        <ul>

        <li>Un Libro es un tipo de Publicación.</li>
        <li>Un MP3 Player es un tipo de Reproductor.</li>
        <li>Una Ventana de Dialogo es un tipo de Ventana.</li>
        </ul>

 <li>   La Herencia nos permite definir un nuevo tipo de objeto especializando la funcionalidad de otro.</li>
 <li>   También nos permite tratar a diferentes tipos de objetos de una forma general, por ejemplo:
       <ul>

        <li> Un Libro, una Revista y un Periódico, se pueden ver como Publicaciones.</li>
       <li>  Un Reproductor de Mp3, un Reproductor de BluRay y una Video-cassetera son todos Reproductores.</li>
       </ul>
 </li>
 <li>   Las relaciones entre objetos se pueden representar en Diagramas de Clases donde se expresan relaciones tipo-de (Herencia), parte-de, utiliza, etc.</li>

</ul>
<q>Este documento intitulado &laquo;&nbsp;<a href="http://es.kioskea.net/contents/poo/polymorp.php3">OOP - Polimorfismo</a>&nbsp;&raquo; de <a href="http://es.kioskea.net">Kioskea.net</a> (<a href="http://es.kioskea.net/">es.kioskea.net</a>) esta puesto a diposición bajo la licencia <a href="/ccmguide/ccmlicence.php3">Creative Commons</a>. Puede copiar, modificar bajo las condiciones puestas por la licencia, siempre que esta nota sea visible.</q>

    """ ,

'/activity/Polimorfismo': u""" <h3>Definici&oacute;n de polimorfismo</h3>
<p align="justify">La palabra <i>polimorfismo</i> proviene del griego y significa <i>que posee varias formas diferentes</i>.
Este es uno de los conceptos esenciales de una programaci&oacute;n orientada a objetos. As&iacute; como la herencia est&aacute;
relacionada con las clases y su jerarqu&iacute;a, el polimorfismo se relaciona con los m&eacute;todos.

<p align="justify">En general, hay tres tipos de polimorfismo:<ul>
<li><a href="#heritage">Polimorfismo de inclusi&oacute;n</a> (tambi&eacute;n llamado <i>redefinici&oacute;n</i> o <i>subtipado</i>)</li></li>
<li><a href="#adhoc">Polimorfismo de sobrecarga</a></li>
<li><a href="#parametrique">Polimorfismo param&eacute;trico</a> (tambi&eacute;n llamado <i>polimorfismo</i> de plantillas)</li>
</ul>
<p align="center">

<p align="justify">Trataremos de describir ahora con m&aacute;s precisi&oacute;n estos tipos de polimorfismo, pero le sugerimos prestar atenci&oacute;n,
ya que muchas personas suelen confundirse al tratar de comprender las diferencias existentes entre estos tres tipos.

<a name="heritage" class="ancre"></a>
<h2>Polimorfismo de subtipado</h2>
<p align="justify">La habilidad para redefinir un m&eacute;todo en clases que se hereda de una clase base se llama <b>especializaci&oacute;n</b>.
Por lo tanto, se puede llamar un m&eacute;todo de objeto sin tener que conocer su tipo intr&iacute;nseco:
 esto es <b>polimorfismo de subtipado</b>. Permite no tomar en cuenta detalles de las clases especializadas de una familia de objetos,
 enmascar&aacute;ndolos con una interfaz com&uacute;n (siendo esta la clase b&aacute;sica).

<p align="justify">Imagine un juego de ajedrez con los objetos <i>rey</i>, <i>reina</i>, <i>alfil</i>, <i> caballo</i>, <i>torre</i> y <i>pe&oacute;n</i>,
cada uno heredando el objeto <i>pieza</i>.
<br/>El m&eacute;todo <i>movimiento</i> podr&iacute;a, usando polimorfismo de subtipado, hacer el movimiento correspondiente de acuerdo a
 la clase objeto que se llama. Esto permite al programa realizar el <i>movimiento.de_pieza</i>
 sin tener que verse conectado con cada tipo de pieza en particular.


<a name="adhoc" class="ancre"></a>
<h2>Polimorfismo de sobrecarga</h2>
<p align="justify">El polimorfismo de sobrecarga ocurre cuando las funciones del mismo nombre existen, con funcionalidad similar,
en clases que son completamente independientes una de otra (&eacute;stas no tienen que ser clases secundarias de la clase objeto).
Por ejemplo, la clase complex, la clase image y la clase link pueden todas tener la funci&oacute;n "display".
Esto significa que no necesitamos preocuparnos sobre el tipo de objeto con el que estamos trabajando si todo lo que deseamos es verlo en la pantalla.
<p align="justify">Por lo tanto, el polimorfismo de sobrecarga nos permite definir operadores cuyos comportamientos var&iacute;an de acuerdo a los
 par&aacute;metros que se les aplican. As&iacute; es posible, por ejemplo, agregar el operador <i>+</i> y hacer que se comporte de manera distinta cuando
  est&aacute; haciendo referencia a una operaci&oacute;n entre dos n&uacute;meros enteros (suma) o bien cuando se encuentra entre dos cadenas de caracteres
  (concatenaci&oacute;n).

<a name="parametrique" class="ancre"></a>
<h2>Polimorfismo param&eacute;trico</h2>
<p align="justify">El polimorfismo param&eacute;trico es la capacidad para definir varias funciones utilizando el mismo nombre,
pero usando par&aacute;metros diferentes (nombre y/o tipo). El polimorfismo <i>param&eacute;trico</i> selecciona autom&aacute;ticamente
el m&eacute;todo correcto a aplicar en funci&oacute;n del tipo de datos pasados en el par&aacute;metro.
<p align="justify">Por lo tanto, podemos por ejemplo, definir varios m&eacute;todos hom&oacute;nimos de <i>addition()</i> efectuando una suma de valores.
    <ul>
        <li>El m&eacute;todo <i>int addition(int,int)</i> devolver&iacute;a la suma de dos n&uacute;meros enteros.</li>
        <li><i>float addition(float, float)</i> devolver&iacute;a la suma de dos flotantes.</li>
        <li><i>char addition(char, char)</i> dar&iacute;a por resultado la suma de dos caracteres definidos por el autor. </li>
        <li>etc. </li>
    </ul>
<p align="justify">Una <i>signature</i> es el nombre y tipo (est&aacute;tico) que se da a los argumentos de una funci&oacute;n.
 Por esto, una firma de m&eacute;todo determina qu&eacute; elemento se va a llamar.
</p>

<q>Este documento intitulado &laquo;&nbsp;<a href="http://es.kioskea.net/contents/poo/polymorp.php3">OOP - Polimorfismo</a>&nbsp;&raquo; de <a href="http://es.kioskea.net">Kioskea.net</a> (<a href="http://es.kioskea.net/">es.kioskea.net</a>) esta puesto a diposición bajo la licencia <a href="/ccmguide/ccmlicence.php3">Creative Commons</a>. Puede copiar, modificar bajo las condiciones puestas por la licencia, siempre que esta nota sea visible.</q>
    """ ,

    '/activity/Encapsulacion_Ejemplos': u"""
    <h3> Una introducción a Objetos y Clases </h3>


    <div class="video">
  <iframe width="560" height="315" src="http://www.youtube.com/embed/2srbnA_V2lI?rel=0" frameborder="0" ></iframe>
   </div>
    """,

'/bye/POO': u""" <h3>Muchas Gracias</h3>
  <p> Con esto termina la evaluación de este sistema prototipo, por ultimo por favor
  danos tus comentarios llenando un cuestionario.
   </p>

    """ ,

'/test/Pretest':{
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


'/test/poo':{
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

"/activity/Post":{ u"""
    <h3> Examen   Final</h3>




    """


},

'/test/Posttest1':{
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
'/test/Posttest2':{
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


'/activity/Preliminar':u"""
    <h3> Programación Orientada a Objetos – ¿Qué es POO?</h3>
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
""",


'/activity/Encapsulacion_intro':
    u"""
    <h3> Encapsulación </h3>

   <p> La encapsulación se considera una de las características definitorias de la orientación a objetos.

Instanciamos objetos con el propósito de  utilizar  los servicios que nos proporcionan a través de sus métodos (públicos).

No necesitamos saber cómo se programó el objeto, ni saber las variables que usa internamente, ni la complejidad del código que contiene.</p>

<p>La encapsulación es un mecanismo de control. El estado (el conjunto de propiedades, atributos ó datos) de un objeto sólo debe ser modificado por medio de los métodos del propio objeto.</p>

<p>Este documento intitulado &laquo;&nbsp;<a href="http://elviajedelnavegante.blogspot.com/2010/04/poo-encapsulacion-y-abstraccion.html">POO: encapsulación y abstracción </a>&nbsp;&raquo;
 de <a href="http://www.blogger.com/profile/09966712995497159376">Ángel Luis García García </a> esta puesto a diposición bajo la licencia <a href="http://creativecommons.org/licenses/by/2.5/es/">Creative Commons</a>. Puede copiar, modificar bajo las condiciones puestas por la licencia, siempre que esta nota sea visible.</p>


    """,

'/activity/video/Objetos_y_Clases_YouTube':
    {'title':u'Una introducción a Objetos y Clases',
     'url':u"http://www.youtube.com/embed/D-w9RKQlAsA?rel=0",
      'youtube_id':"D-w9RKQlAsA"} ,






'/activity/Objetos_y_Clases_YouTube':
    u"""
    <h3> Una introducción a Objetos y Clases </h3>
    <div class="video">
    <iframe width="640" height="510" src="http://www.youtube.com/embed/D-w9RKQlAsA?rel=0" frameborder="0" allowfullscreen></iframe> </div>
    """,

    '/activity/Objetos_y_Clases_HTML':
            u"""
            
           <h3> ¿Qué es una Clase?</h3>
           
          <p> Cuando decimos “ave”, sabemos que nos referimos a “algo” con plumas, pico, dos patas, etc. No importa realmente si hemos visto un ave o no,
           o si tenemos un ave frente a nosotros; entendemos claramente que la palabra “ave” se refiere a alguna cosa que cumple
           con unas características específicas, se comporta de una forma concreta, etc. No es más que una palabra,
           pero nos permite <b>clasificar</b> las cosas. Por ejemplo, sabemos que una gallina <b>es un</b> ave y que un perro no es un ave.</p>
          <p>
         La clasificación es algo que hacemos todos los días, a cada momento. Cada vez que decimos que algo es
           alguna cosa, estamos clasificándolo, asociándolo a una clase.
          </p>
          <p>
          Sin embargo, sabemos que la palabra ave no se refiere a un animal concreto, sino a una serie de animales.
          Ave es la palabra que usamos para identificarlos en un grupo, en tal caso siempre
          nos referiremos a esta o aquella ave, siempre hablaremos de un animal concreto.
          </p>
          <p>
          En la POO ocurre igual, una clase no es más que una serie de código que define a todos los elementos
          relacionados con ella. Así, podríamos escribir la clase ave colocando en ella todas las características
          que tienen las aves (pico, color, alto, ancho, patas,…) esas características las llamaremos en lenguaje
          de programadores, propiedades o atributos.
          </p>
          
         <p>Pero la cosa no termina allí, resulta que las aves tienen también ciertos mecanismos específicos,
 como <i>comer</i>, <i>dormir</i>, <i>reproducirse</i>, etc. Estos mecanismos los llamamos <b>métodos</b> u <b>operaciones</b>. El conjunto de todos estas
 operaciones definen el <b>comportamiento</b> de las aves.
          </p>
            <p>
Por último, también sabemos que las aves reaccionan ante ciertos sucesos, como <i>peligro</i>, <i>atracción</i>, <i>defensa</i>. A esto lo llamaremos eventos
          </p>
<h3>¿Qué es una Instancia?</h3>
          <p>
          Bien, decíamos que una clase es como la definición de un <b>tipo</b> de objetos, pero no es el objeto en sí, del modo como
          una idea no es una cosa concreta. Así que para sentarnos necesitaremos convertir
           esa idea en algo, en un objeto real; a ese objeto lo llamamos instancia.
          </p>

          <p>
          En un mismo proyecto podemos tener una o más instancias de una misma clase sin problemas.
          </p>

          <p>
          Cada vez que creamos una nueva instancia, ésta adquiere las propiedades, métodos y eventos de
           la clase a la que pertenece (es lo que permite la relación es un), sin embargo, cada instancia es
            independiente de las otras; esto nos da dos ventajas:
          </p>
           <ol>
           <li>Si hacemos algún cambio en la clase, todas las instancias de esta clase se actualizarán automáticamente;
           esto nos permite hacer cambios sin tener que ir a cada una de las instancias (se aplica el mismo principio
           en la herencia, aunque a un nivel diferente). </li>
            <li> Al ser independientes de las otras instancias, podemos darles valores diferentes sin que afecten
            a las demás.
             Aunque comparten la misma estructura, pueden programarse individualmente, dando versatilidad y
             flexibilidad al código.</li>

           </ol>
          <p>
          </p>

            """
    ,
    '/program/1':
        {   'title':u"Ordena la Lista",
            'initial_code':u"""
# Funcion que ordena una lista, puedes utilizar sort()
def solution():
    pass
""",
            'correct_code':u"""# Solution:
def solution(l):
    if l is None:
        return []
    else:
        l.sort()
        return l""",
            'instructions':u"""<p>Escribe una función llamada solution la cual reciba como parámetro
                una lista y regrese la lista ordenada.</p>
            <p>En caso de recibir como parámetro el valor None debe regresar una lista vacía. </p>
            <code>
                <p>>>> solution([4,3,5,1])</p>
                <p>[1, 3, 4, 5]</p>
                <p>>>> solution(None)</p>
                <p>[]</p>
            </code>""",
            'unit_test':u"""
import sys
import unittest
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False


class Test(unittest.TestCase):
    def setUp(self):
        pass
    def test_order(self):
        self.assertEqual(solution([2,6,1,5]),[1,2,5,6])
    def test_none(self):
        self.assertEqual(solution(None),[])

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},


    '/program/2':
        { 'title':u"Imprime Hola",
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
            'unit_test':u"""import unittest, sys
import json

class ResultadoPrueba(unittest.TestResult):
    def __init__(self):
         super(ResultadoPrueba, self).__init__()
         self.success = []
    def addSuccess(self, test):
         self.success.append(test)
    def shouldStop(self, test):
         return False

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

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
Resultado = ResultadoPrueba()
suite.run(Resultado)
result = {}

if Resultado.wasSuccessful():
    result['result'] = "Success"
else:
    result['result'] = "Failure"
result['errors']=  [str(e[0])   for e in Resultado.errors]
result['failures']=  [str(e[0]) for e in Resultado.failures]
result['successes']=  [str(e)  for e in Resultado.success]
print "!!!---"
print json.dumps(result)
"""},

'/survey/EESM1':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM2':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM3':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM4':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM5':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM6':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM7':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM8':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM9':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM10':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM11':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM12':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },
'/survey/EESM13':{
    'questions':  [
                    {'id': 9903,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia frustrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9909,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia aburrido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9910,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia distraido",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    
                    {'id': 9912,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia relajado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9913,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia concentrado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    {'id': 9915,
                    'interaction': 'simpleChoice',
                    'inline': 1,
                    'title': "Pregunta Abierta",
                    'question': "Me sentia entusiasmado",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Muy de acuerdo",
                                "De acuerdo",
                                "Neutral",
                                "En desacuerdo",
                                "Muy en desacuerdo"],
                    'answer': [1,0,0,0,0],
                    'answer_text': "",
                    'hints': []
                    },
                    ],
    'intro':"""<h3>Prueba de Experiencia</h3>
    <p>Contesta las siguientes preguntas de acuerdo a como te sentiste mientras resolvias el ejercicio anterior.</p>""",
    'bye':""" """,
    'satisfied_at_least':3
                    },

'/survey/EP':{
    'questions':  [{'id': 8801,
                    'interaction': 'simpleChoice',
                    'inline': 0 ,
                    'title': "Pregunta Abierta",
                    'question': u'¿Cuántos años tienes programando?',
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["0 años", "1 año", "2-4 años", "5 ó más años"],
                    'answer': [1,1,0,0],
                    'answer_text': "Solo son México y USA",
                    'hints': ["España está en Europa", "Nicaragua es de Sudamérica"]
                    },
                    {
                    'id':8802,
                    'interaction': 'simpleChoice',
                    'inline': 0,
                    'title': "Pregunta Abierta",
                    'question': "¿Cuántos cursos de programación has llevado?",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["0 cursos","1 curso","2-4 cursos","5 ó más cursos"],
                    'answer': [0,1,0,1],
                    },
                    {
                    'id':8803,
                    'interaction': 'simpleChoice',
                    'inline': 0,
                    'title': "Pregunta Abierta",
                    'question': "¿Te gusta programar?",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Sí", "Más o menos", "No"],
                    'type':"str",
                    'answer': [1,0,0],
                    },
                    {
                    'id':8804,
                    'interaction': 'choiceInteraction',
                    'inline': 0,
                    'title': "Pregunta Abierta",
                    'question': "¿Qué paradigmas de programación manejas?",
                    'can_check': "True",
                    'can_show': "True",
                    'can_hint': "True",
                    'options': ["Programación Orientada a Objetos", "Programación Funcional", "Programación Declarativa",
                    "Programación Imperativa", "Ninguno", "No sé"],
                    'type':"str",
                    'answer': [1,0,0,0,0,0],
                    },
                    ],
    'intro':"""<h3>Experiencia en Programaci&oacute;n</h3>
    <p>Antes de empezar el curso, dinos algo sobre tu experiencia en programación.</p>""",
    'bye':"""""",
     'satisfied_at_least':3
                    },

'/activity/actividad1': u""" <h3>Redes</h3>
  <p>Actividad 1 </p> """ ,

'/activity/actividad2': u""" <h3>Redes</h3>
  <p>Actividad 2 </p> """ ,
'/activity/actividad3': u""" <h3>Redes</h3>
  <p>Actividad 3 </p> """ ,
'/activity/actividad4': u""" <h3>Redes</h3>
  <p>Actividad 4 </p> """ ,
'/activity/actividad5': u""" <h3>Redes</h3>
  <p>Actividad 5 </p> """ ,
'/activity/actividad6': u""" <h3>Redes</h3>
  <p>Actividad 6 </p> """ ,
'/activity/Redes': u""" <h3>Redes</h3>
  <p>Blah </p> """ ,

}



multi_device_activities = {
              '/activity/Redes':
                            [{'url': '/objetos/Actividad1/Dispositivo1_Imagen1.png', 'estado': 'play', 'dispositivo':  '1', 'tipo': 'imagen'}
                              ],


              '/activity/actividad1':
                             [{'url': '/objetos/Actividad1/Dispositivo1_Imagen1.png', 'estado': 'play', 'dispositivo':  '1', 'tipo': 'imagen'} ,
                              {'url': '/objetos/Actividad1/Dispositivo2_Imagen2.png', 'estado': 'play', 'dispositivo':  '2', 'tipo': 'imagen'},
                              {'url': '/objetos/Actividad1/Dispositivo3_Imagen3.png', 'estado': 'play', 'dispositivo':  '3', 'tipo': 'imagen'},
                              {'url': '/objetos/Actividad1/Dispositivo4_Imagen4.png', 'estado': 'play', 'dispositivo':  '4', 'tipo': 'imagen'},
                              {'url': '/objetos/Actividad1/Dispositivo5_Imagen5.png', 'estado': 'play', 'dispositivo':  '5', 'tipo': 'imagen'}

                              ],

             '/activity/actividad2': [{'url':'/objetos/Actividad2/Dispositivo1_Video1.gif',  'estado': 'play', 'dispositivo':  '1', 'tipo': 'imagen'} ,
                              {'url': '/objetos/Actividad1/Dispositivo2_Imagen2.png', 'estado': 'play', 'dispositivo':  '2', 'tipo': 'imagen'},
                              {'url': '/objetos/Actividad1/Dispositivo3_Imagen3.png', 'estado': 'play', 'dispositivo':  '3', 'tipo': 'imagen'},
                              {'url': '/objetos/Actividad1/Dispositivo4_Imagen4.png', 'estado': 'play', 'dispositivo':  '4', 'tipo': 'imagen'},
                              {'url': '/objetos/Actividad1/Dispositivo5_Imagen5.png', 'estado': 'play', 'dispositivo':  '5', 'tipo': 'imagen'}

                              ],
           '/activity/actividad3':
             [{'url': '/objetos/Actividad1/Dispositivo1_Imagen1.png',  'estado': 'play', 'dispositivo':  '1', 'tipo': 'imagen'} ,
              {'url': '/objetos/Actividad3/Dispositivo2_Video2.gif', 'estado': 'play', 'dispositivo':  '2', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad1/Dispositivo3_Imagen3.png', 'estado': 'play', 'dispositivo':  '3', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad1/Dispositivo4_Imagen4.png', 'estado': 'play', 'dispositivo':  '4', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad1/Dispositivo5_Imagen5.png', 'estado': 'play', 'dispositivo':  '5', 'tipo': 'imagen'}

              ],

            '/activity/actividad4':
             [{'url': '/objetos/Actividad1/Dispositivo1_Imagen1.png', 'estado': 'play', 'dispositivo':  '1', 'tipo': 'imagen'} ,
              {'url': '/objetos/Actividad1/Dispositivo2_Imagen2.png', 'estado': 'play', 'dispositivo':  '2', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad4/Dispositivo3_Video3.gif', 'estado': 'play', 'dispositivo':  '3', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad1/Dispositivo4_Imagen4.png', 'estado': 'play', 'dispositivo':  '4', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad1/Dispositivo5_Imagen5.png', 'estado': 'play', 'dispositivo':  '5', 'tipo': 'imagen'}

              ],


            '/activity/actividad5':
             [{'url': '/objetos/Actividad1/Dispositivo1_Imagen1.png', 'estado': 'play', 'dispositivo':  '1', 'tipo': 'imagen'} ,
             {'url': '/objetos/Actividad1/Dispositivo2_Imagen2.png', 'estado': 'play', 'dispositivo':  '2', 'tipo': 'imagen'},
             {'url': '/objetos/Actividad1/Dispositivo3_Imagen3.png', 'estado': 'play', 'dispositivo':  '3', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad5/Dispositivo4_Video4.gif', 'estado': 'play', 'dispositivo':  '4', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad1/Dispositivo5_Imagen5.png', 'estado': 'play', 'dispositivo':  '5', 'tipo': 'imagen'}
             ],
            '/activity/actividad6':
             [{'url': '/objetos/Actividad1/Dispositivo1_Imagen1.png', 'estado': 'play', 'dispositivo':  '1', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad1/Dispositivo2_Imagen2.png', 'estado': 'play', 'dispositivo':  '2', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad1/Dispositivo3_Imagen3.png', 'estado': 'play', 'dispositivo':  '3', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad1/Dispositivo4_Imagen4.png', 'estado': 'play', 'dispositivo':  '4', 'tipo': 'imagen'},
              {'url': '/objetos/Actividad6/Dispositivo5_Video5.gif', 'estado': 'play', 'dispositivo':  '5', 'tipo': 'imagen'}],

             }


#
# if __name__ == "__main__":
#
#     from pymongo import MongoClient
#     client = MongoClient()
#     a = { '_id':'/activity/video/lo-que-ahora-sabemos',
#           'title':u'Introducción',
#           'url':u"https://www.youtube.com/watch?v=GUxyQ6Mj_kc",
#           'youtube_id':'GUxyQ6Mj_kc'}
#
#
#     db = client.protoboard_database
#     activities_collection = db.activities_collection
#     activity_id = activities_collection.insert(a)
#     print activity_id