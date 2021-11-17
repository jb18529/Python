#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 23:18:20 2021

@author: david
"""
#Using a tuple to return multiple values in a function
def function(x, y):
    q = x + y
    r = x-y
    return(q, r)

(add, sub) = function(2, 3)
print(add)
print(sub)


