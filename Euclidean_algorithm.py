#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 10 00:17:47 2021

@author: david
"""

def gcdRecur(a, b):
    '''
    input: integer number
    output: greatest common divisor
    Uses Euclidean algorithm
    Formal description of the Euclidean algorithm
    Input Two positive integers, a and b.
    Output The greatest common divisor, g, of a and b.
    Internal computation
    If a<b, exchange a and b.
    Divide a by b and get the remainder, r. If r=0, report b as the GCD of a and b.
    Replace a by b and replace b by r. Return to the previous step.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a % b)
print(gcdRecur(0, 21))