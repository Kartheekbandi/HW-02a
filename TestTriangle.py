# -*- coding: utf-8 -*-
"""
Updated Feb 7, 2023
The primary goal of this file is to demonstrate a simple unittest implementation

@author: Kartheek Reddy Bandi
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def test_Right_TriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def test_Right_TriangleB(self): 
        self.assertEqual(classifyTriangle(10,8,6),'Right','10,8,6 is a Right triangle')
    
    def test_Equilateral_TrianglesA(self): 
        self.assertEqual(classifyTriangle(3,3,3),'Equilateral','3,3,3 should be Equilateral')

    def test_Equilateral_TrianglesB(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be Equilateral')

    def test_Scalene_TrianglesA(self):
        self.assertEqual(classifyTriangle(8,7,9),'Scalene','8,7,9 should be Scalene')
    
    def test_Isoceles_TrianglesA(self):
        self.assertEqual(classifyTriangle(6,8,8),'Isoceles','6,8,8 should be Isoceles')
    
    def test_InvalidInput_TrianglesA(self): 
        self.assertEqual(classifyTriangle(6,202,10),'InvalidInput','6,202,10 should be InvalidInput')

    def test_InvalidInput_TrianglesB(self): 
        self.assertEqual(classifyTriangle(0,-8,10),'InvalidInput','0,-8,10 should be InvalidInput')

    def test_NotATriangle_TrianglesA(self): 
        self.assertEqual(classifyTriangle(7,2,4),'NotATriangle','7,2,4 is a NotATriangle')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

