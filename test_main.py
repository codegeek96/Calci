#!/usr/bin/env python3

import unittest
import main

class TestCalci(unittest.TestCase):

    def setUp(self):
        pass

    def test_add(self):
        self.assertEqual(main.add(3, 4), 7, 'addition fail')

    def test_sub(self):
        self.assertEqual(main.sub(6, 4), 2, 'subtraction fail')

    def test_div(self):
        self.assertEqual(main.div(6, 3), 2, 'division fail')

    def test_multi(self):
        self.assertEqual(main.multi(6, 2), 12, 'multiplication fail')

    def test_perc(self):
        self.assertEqual(main.perc(138), 1.38, 'percentage fail')

    def test_fact(self):
        self.assertEqual(main.fact(3), 6, 'factorial fail')

    def test_squarert(self):
        self.assertEqual(main.squarert(4), 2, 'square root fail')

    def test_power(self):
        self.assertEqual(main.power(3, 3), 27, 'power fail') 

    def test_logarithm(self):
        self.assertAlmostEqual(main.log(5), 0.6989700043360189, 'logarithm fail')
        
    def test_nlogarithm(self):
        self.assertAlmostEqual(main.nlog(3), 1.0986122886681098,
'natural logarithm fail')

    def test_exp(self):
        self.assertAlmostEqual(main.exp(2), 7.38905609893065,
'exponential fail')

    def test_sine(self):
        self.assertAlmostEqual(main.sin(int(90)), float(1.0), 'sine fail')

    def test_cosine(self):
        self.assertAlmostEqual(main.cos(int(0)), float(1.0), 'cosine fail')

    def test_tangent(self):
        self.assertAlmostEqual(main.tan(int(45)), float(0.9999999999999999), 'tangent fail')

    def test_degrees(self):
        self.assertAlmostEqual(main.deg(1), 57.29577951308232, 'radians to degrees fail')

    def test_radians(self):
        self.assertAlmostEqual(main.rad(int(1)), float(0.017453292519943295), 'degrees to radians fail')

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
