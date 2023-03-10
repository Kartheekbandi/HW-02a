# -*- coding: utf-8 -*-
"""
HW 02a - Testing a legacy program and reporting on testing results
Created on Thu Jan 14 13:44:00 2016
Updated Feb 7, 2023
The primary goal of this file is to demonstrate a simple python program to classify triangles
@author: Kartheek Reddy Bandi
Contact: kbandi1@stevens.edu
"""

def classifyTriangle(a,b,c):
    """
    Your correct code goes here...  Fix the faulty logic below until the code passes all of 
    you test cases. 
    
    This function returns a string with the type of triangle from three integer values
    corresponding to the lengths of the three sides of the Triangle.
    
    return:
        If all three sides are equal, return 'Equilateral'
        If exactly one pair of sides are equal, return 'Isoceles'
        If no pair of  sides are equal, return 'Scalene'
        If not a valid triangle, then return 'NotATriangle'
        If the sum of any two sides equals the squate of the third side, then return 'Right'
      
      BEWARE: there may be a bug or two in this code
    """

    # require that the input values be >= 0 and <= 200
    if a > 200 or b > 200 or c > 200:
        return 'InvalidInput'
        
    if a <= 0 or b <= 0 or c <= 0:
        return 'InvalidInput'
    
    # verify that all 3 inputs are integers  
    # Python's "isinstance(object,type) returns True if the object is of the specified type
    if not(isinstance(a,int) and isinstance(b,int) and isinstance(c,int)):
        return 'InvalidInput'
      
    # This information was not in the requirements spec but 
    # is important for correctness
    # the sum of any two sides must be strictly less than the third side
    # of the specified shape is not a triangle
    if ((a+b)<c) or ((a+c)<b) or ((b+c)<a):
        return 'NotATriangle'
        
    # now we know that we have a valid triangle 
    if ((a*a + b*b) == c*c) or ((b*b + c*c) == a*a) or ((c*c + a*a) == b*b): 
        return 'Right'
    elif (a == b == c):
        return 'Equilateral'
    elif (a==b) or (b==c) or (a==c) :
        return 'Isoceles'
    elif (a != b) and  (b != c) and (a != b):
        return 'Scalene'
from datetime import datetime #Importing datetime command to get the time and date of code execution.
"""def my_brand(assignment_name):
    print("==== Name: Kartheek Reddy Bandi ====")
    print("==== Course: 2023S-SSW567-WS ====")
    print("==== " + "Assignment name:" + ass_name + " ====")
    print("==== " + "Current_date & time : " +datetime.now().strftime("%m-%d-%y & %H:%M:%S")+ " ====")
    
    return 
ass_name=input("Enter Assignment name: ")
my_brand(ass_name)
HONOR PLEDGE: I Have done this assignment on my own and haven't copied from others or internet.
Considered my SSW-567 Hw_01 as reference and made changes accordingly.
"""
