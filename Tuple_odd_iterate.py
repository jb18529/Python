#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 22:54:41 2021

@author: david
"""
#iterate over tuple and print out odd elements in tuple

def Tuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    # Your Code Here
    new = ()
    if aTup == ():
        return ()
    else:
        yes = aTup[::2]
        new = new + yes
        return new
   

x = ('I', 'am', 'a', 'test', 'tuple')
print(Tuples(x))

#alternative solution

def Tuples(aTup):
    new = ()
    for i in range(len(aTup)):
        if i % 2 == 0:
            new += (aTup[i],)
    return new

