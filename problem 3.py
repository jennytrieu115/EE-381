# -*- coding: utf-8 -*-
"""
Created on Wed Feb 13 13:36:31 2019

@author: admin
"""
# Getting 50 heads when tossing 100 coins
import numpy as np

# declare N equals to 100000 times 
N = 100000 

    
# randomly generate int number to determine flip
def coin(N):
    heads ,tails = 0,0 
    coin = np.random.randint(0,2,N)
    heads = sum(coin)
    tails = N - heads 
    
    return heads, tails
# run the experiment 100000 times 
def runExperiment():
    # declare success time 
    success = 0
    for i in range(0, N):
        if coin(100) [0] == 50:
            success = success + 1
    return success 

# find the probability of success which is 50 heads in tosing 100 coins 
def prob():
    numOfSuccess = runExperiment()
    # p is probability
    p = numOfSuccess / N 
    print('Probability of 50 heads in tossing 100 fairn coins : ', p )
    
prob()


            
