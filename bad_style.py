import os,sys,json
from pathlib import Path

def BadlyNamedFunction(  param1,param2,param3 ):
    # This function does something
    result=0
    for i in range(0,10):
        result=result+i
    return result

class BadlyFormattedClass:
    def __init__(self):
        self.var1=1
        self.var2=2
        self.var3=3

    def method1(self):
        # This method has inconsistent indentation
      print("Hello")
        print("World")

    def method2(self):
        # This method has no type hints
        x=5
        y="string"
        return x+y

def another_badly_named_function():
    # This function has no docstring
    a=1
    b=2
    c=3
    d=4
    e=5
    f=6
    g=7
    h=8
    i=9
    j=10
    return a+b+c+d+e+f+g+h+i+j

# This line is way too long and violates PEP 8's 79 character limit. It should be split into multiple lines or shortened to improve readability and maintainability.
long_line = "This is a very long line that exceeds the recommended character limit and should be split into multiple lines for better readability and maintainability."

# Inconsistent spacing around operators
x=1+2*3/4
y = 1 + 2 * 3 / 4
z=1+2*3/4

# Multiple statements on one line
if x>0: print("Positive"); print("Still positive") 