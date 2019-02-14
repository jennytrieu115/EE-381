# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# problem 1
from random import randint
import numpy as np
def nSideDice(p):
    side = randint(0, p - 1)
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

rollTimes = 100000
rolls = rollDice(6, rollTimes)
print("Rolls = ", rolls)
validate(rolls, rollTimes)

