# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 18:26:54 2019

@author: admin
"""
#problem 2
from random import randint
import numpy as np
def nSideDice(p):
    side = randint(0, p - 1)
    return side

def rollDice():
    numOfSucces = 0
    # stop when sum 2 dice is 7
    for k in range (0,10000): 
        dice1 =nSideDice(6)
        dice2 =nSideDice(6)
        if ((dice1+dice2) == 7):
            print('\nThe total number of roll times to find 7 is: ', k)
            #print('dice1 =',dice1)
            #print('dice2 =',dice2)
            break
    # record the number of time that sum =7
    print('\nRoll 10000 time and record number of success : ')
    for k in range(0,10000):
        dice1 =nSideDice(6)
        dice2 =nSideDice(6)
        if((dice1+dice2) == 7):
            numOfSucces = numOfSucces +1
        
    print('\nTotal number of success is :', numOfSucces)

#graph
    
#Label 
x = range(1,5,1)
# Label 
plt.xlabel('Number Of Success time')
plt.ylabel('Probability')
plt.title('PMF for Numbe Of Rolls Needed To Get a "7" With Two Dice')
plt.xtick(b1)
plt.show()

    
    
# Call a function rollDice()
roll = rollDice()
