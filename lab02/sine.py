"""
This module implements local search on a simple abs function variant.
The function is a linear function  with a single, discontinuous max value
(see the abs function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
import sys
sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/aima")
sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/paip")
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math


class AbsVariant(Problem):
    """
    State: x value for the abs function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, initial, maximum=30.0, delta=0.001):
        self.initial = initial
        self.maximum = maximum
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        return math.fabs(x*math.sin(x))


if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    ann_max = 0;
    hill_max = 0;
    for x in range(0,100):
        initial = randrange(0, maximum)
        p = AbsVariant(initial, maximum, delta=1.8)
        # print('Initial                      x: ' + str(p.initial)
        #     + '\t\tvalue: ' + str(p.value(initial))
        #     )

        # Solve the problem using hill-climbing.
        hill_solution = hill_climbing(p)
        if p.value(hill_solution) > hill_max:
            hill_max = p.value(hill_solution)

        # Solve the problem using simulated annealing.
        
        annealing_solution = simulated_annealing(
            p,
            exp_schedule(k=20, lam=0.005, limit=1000)
        )
        if p.value(annealing_solution) > ann_max:
            ann_max = p.value(annealing_solution)
        
    print('Hill-climbing max solution value: ' + str(hill_max)
            )
    print('Simulated annealing max solution value: ' + str(ann_max)
            )
