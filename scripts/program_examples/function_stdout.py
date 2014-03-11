__author__ = 'mariosky'


def foo():
    print "Hola"


import unittest, sys
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
test_result = unittest.TextTestRunner(verbosity=2, stream=sys.stderr).run(suite)
