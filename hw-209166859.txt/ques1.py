# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 20:11:51 2023

@author: rache
"""

#question 1:
def my_func(x1,x2,x3):
    if (x1+x2+x3==0):
        print("Not a number – denominator equals zero")
    elif type(x1)== int or type(x2)== int or type(x3) == int:
        print("Error: parameters should be float")
    elif type(x1)!= float or type(x2)!= float or type(x3) != float:
         print("None")   
    else:
        print(((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3))



my_func(4.6,9.0,-86.0)
   
