# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# problem 1
import matplotlib.pyplot as plt
from random import randint
import numpy as np

def nSideDice(diceSideCount):
    side = randint(0, diceSideCount - 1)
    return side

def rollDice(diceSideCount, rollTimes):
    rolls = [0 for x in range(diceSideCount)]
    for k in range(0, rollTimes):
        r = nSideDice(diceSideCount)
        rolls[r] = rolls[r] + 1
    return rolls

def validate(rolls, rollTimes):
     
    for k in range(0, len(rolls)):
        rolls[k] = rolls[k] / rollTimes
    print("Sum = ", sum(rolls))
    

rollTimes = 10000
rolls = rollDice(6, rollTimes)
print("Rolls = ", rolls)
validate(rolls, rollTimes)

# plotting
#h1,binEdges = np.histogram(s,b)
x = range(1,5,1)
# Label 
plt.xlabel('Number On The Face Of The Die')
plt.ylabel('Probability')
plt.title('PMF for an unfair N-side die')
plt.xtick(b1)
plt.show()
