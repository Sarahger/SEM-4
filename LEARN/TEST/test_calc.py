import unittest as ut
import random
from calc import *

def add_test(self):
    x = random.randint(10000)  
    y = random.randint(10000) 
    self.assertEqual(add(x,y),x+y)

def sub_test(self):
    x = random.randint(10000)  
    y = random.randint(10000) 
    self.assertEqual(add(x,y),x-y)
    
def mul_test(self):
    x = random.randint(10000)  
    y = random.randint(10000) 
    self.assertEqual(add(x,y),x*y)
    
def div_test(self):
    x = random.randint(10000)  
    y = random.randint(10000) 
    self.assertEqual(add(x,y),x/y)
    with self.assertRaise(ZeroDivisionError):
        add(x,0)