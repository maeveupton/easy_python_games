# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 10:56:39 2018

@author: Owner
"""
#Importing time module
import time
#Welcome user
name = raw_input("What is your name? ")

print "Hello, " + name, "Time to play hangman!"


#wait for 1 second
time.sleep(1)

print "Start guessing..."
time.sleep(0.5)

#here we set the word
word = "secret"
#creates an variable with an empty value 
guesses = ''
#number of turns
turns = 10
#Create while loop
#ceck if turns more than zero
while turns>0:
    #make counter start with zero
    fail=0
    #for every character in secret_word:
    for char in word:
        #see id character is in players guess
        if char in guesses:
            print char,
        else:
            print "_"
            #increse fail counter with one
            fail+=1
    if fail ==0:
        print " You won"
        #exit script
        break
    print
    #ask user to guess a character
    guess = raw_input("guess a character:")
    #set palyer guess to guesses 
    guesses +=guess
    #if guess not right
    if guess not in word:
        #counter decreases by 1(now 9)
        turns -=1
        print "wrong"
        print "You have", + turns, "more guesses"
        if turns ==0:
            print "you lost"
            
        
            
