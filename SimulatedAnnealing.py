from math import *
from random import *

def BestSoFar(d,t): # Best so Far Function
    return exp((d)/t)

def rumus(x1,x2): # Minimum Value Function
    return -(abs(sin(x1)*cos(x2)*exp(abs(1-(sqrt(pow(x1,2)+pow(x2,2)))/pi))))

def probability():
    x1 = uniform(-10,10) # Range for Random Number
    x2 = uniform(-10,10) # Range for Random Number
    return rumus(x1,x2) # Result for Minimum Value

result = probability() # First Minimum Value
currentState = result # Current Value
initialTemp = 1000 # Inital Temperature / Maximum Temperature
compTemp = 0.00001 # Comparison Temperature / Minimum Temperature

while initialTemp>compTemp:
    newState = probability() # Comparison Value
    d = currentState - newState # Delta E

    if d>0: # Best Case
        currentState = newState
        result = newState
    else: # Worst Case
        randnum = random() # Random Number
        prob = BestSoFar(d,initialTemp) # Probability

        if prob>randnum:
            currentState = newState
            result = newState

    initialTemp = initialTemp*0.99999 # Temperature Compressing
    print('Temp:',initialTemp,'Hasil:',result)

