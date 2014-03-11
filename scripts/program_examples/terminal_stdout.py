__author__ = 'mariosky'



import unittest, sys
class Test(unittest.TestCase):
    def test_console(self):
        from StringIO import StringIO
        saved_stdout = sys.stdout
        output = None
        try:
            out = StringIO()
            sys.stdout = out

### CODE HERE

            tu=[1,2,3,4]
            print tu[0]
###
            output = out.getvalue().strip()
            self.assertEqual( output,'1')
        finally:
            sys.stdout = saved_stdout
            print output

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
test_result = unittest.TextTestRunner(verbosity=2, stream=sys.stderr).run(suite)
