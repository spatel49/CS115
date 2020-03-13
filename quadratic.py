'''
Created on Nov 14, 2018

@author: sypat
'''
import math

class QuadraticEquation(object):
    def __init__(self, A, B, C):
        if A == 0:
            raise ValueError("Coefficient 'a' cannot be 0 in a quadratic equation.")
        self.__A = float(A)
        self.__B = float(B)
        self.__C = float(C)
    @property
    def a(self):
        return self.__A
    
    @property
    def b(self):
        return self.__B
    
    @property
    def c(self):
        return self.__C
    
    def discriminant(self):
        return (self.__B) ** 2 - (4 * (self.__A) * self.__C)
    
    def root1(self):
        if self.discriminant() < 0:
            return None
        return (-(self.__B) + math.sqrt(self.discriminant())) / (2 * self.__A)
    
    def root2(self):
        if self.discriminant() < 0:
            return None
        return (-(self.__B) - math.sqrt(self.discriminant())) / (2 * self.__A)
    
    def __str__(self):
        stringA = ""
        stringB = ""
        stringC = ""
        if self.__A == 1:
            stringA = "x^2"
        elif self.__A == -1:
            stringA = "-x^2"
        else:
            stringA = str(self.__A) + "x^2"
        if self.__B == 1:
            stringB = " + x"
        elif self.__B == -1:
            stringB = " - x"
        elif self.__B == 0:
            stringB = ""
        elif self.__B < 0:
            stringB = " - " + str(abs(self.__B)) + "x"
        elif self.__B > 0:
            stringB = " + " + str(self.__B) + "x"
        if self.__C==0:
            stringC = ""
        elif self.__C > 0:
            stringC = " + " + str(self.__C)
        elif self.__C < 0:
            stringC = " - " + str(abs(self.__C))
        return stringA + stringB + stringC + " = 0"

print(QuadraticEquation(9,-1,81))
    
    