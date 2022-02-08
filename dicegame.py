# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Rolling dice game
import random
import time

min_no=1
max_no=6

roll_again = "yes"
while roll_again =="yes" or roll_again=="y":
    print "Rolling the dices..."
    time.sleep(1)
    print "The values are.."
    time.sleep(1)
    print random.randint(min_no,max_no)
    time.sleep(1)
    print random.randint(min_no,max_no)
    
    roll_again = raw_input("Roll the dices again?")

