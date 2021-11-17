#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 16:18:28 2021

@author: david
"""
#While loop finding the sum of every 2nd number from 5 to 11
sum = 0
n = 5
while(5 <= n < 11):
    sum += n
    n += 2
print (sum)

#For version of the while statement above
mysum = 0
for i in range (5, 11, 2):
    mysum += i
print(mysum)