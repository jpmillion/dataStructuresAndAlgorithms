import unittest
import mathAlgos

class TestMath(unittest.TestCase):
    def testFib(self):
        self.assertEqual(13, mathAlgos.fib(7), 'should equal 13')
        self.assertEqual(21, mathAlgos.fib(8), 'should equal 21')
        self.assertEqual(1, mathAlgos.fib(2), 'should equal 1')
        self.assertEqual(2, mathAlgos.fib(3), 'should equal 13')
        self.assertEqual('Input must be positive', mathAlgos.fib(-1), 'input was invalid')

    def testFac(self):
        self.assertEqual(120, mathAlgos.fac(5), 'should equal 120')
        self.assertEqual(720, mathAlgos.fac(6), 'should equal 720')
        self.assertEqual(3628800, mathAlgos.fac(10), 'should equal 3628800')
        self.assertEqual(39916800, mathAlgos.fac(11), 'should equal 39916800')
        self.assertEqual(1, mathAlgos.fac(0), 'should equal 1')
        self.assertEqual(1, mathAlgos.fac(1), 'should equal 1')
        self.assertEqual('invalid input', mathAlgos.fac(-2), 'input must be positive')

if __name__ == '__main__':
    unittest.main()
