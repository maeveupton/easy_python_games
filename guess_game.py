# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:41:43 2018

@author: Owner
"""
#Guessing game with a limit
import random

#Random number between 1 and 99
min_no = 1
max_no = 99
number= random.randint(min_no,max_no)
#Set initial guess to 0
guesses = 0
#Guesses less than 5 ask user to guess number
while guesses<5:
    guess=int(raw_input("Enter an integer from 1 to 99: "))
    guesses +=1
    print "This is your %d guess" %guesses

#Check is guess lower, higher or equal to random number

    if guess < number:
        print "Guess is low"
    elif guess > number:
        print "Guess is high"
    elif guess == number:
        break
if guess == number:
    guesses = str(guesses)
    print " You guess it in: ", guesses + "guesses"
if guess !=number:
    number = str(number)
    print "The secret number was", number
    