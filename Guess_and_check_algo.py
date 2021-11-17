#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 11 19:47:25 2021

@author: david
"""
#Guess and check algo
# Python code for Heron of Alexandria's algorithm for the square root of a number.

y = float(input("Enter the number whose square root you want to find: "))
guess = float(input("Enter a starting guess: "))

# we want the code to return a guess whose square is within a range of 'epsilon' from y
epsilon = float(input("Enter the desired precision: "))
while (abs(guess**2 - y) >= epsilon):
    guess = (1/2) * (guess + y / guess)

print("An approximation to the square root of " + str(y) + " is " + str(guess))