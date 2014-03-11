__author__ = 'mariosky'




# Solution:
def solution(l):
    if l is None:
        return []
    else:
        l.sort()
        return l


#Test
import unittest,sys
class Test(unittest.TestCase):
    def setUp(self):
        pass

    def test_order(self):
        self.assertEqual(solution([2,6,1,5]),[1,2,5,6])

    def test_none(self):
        self.assertEqual(solution(None),[])

suite = unittest.TestLoader().loadTestsFromTestCase(Test)
test_result = unittest.TextTestRunner(verbosity=2, stream=sys.stderr).run(suite)
