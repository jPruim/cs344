"""
This module implements local search on a simple tsp problem.

@author: jpruim
@version 6feb2013
"""
import sys
# sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/aima")
# sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/paip")
sys.path.insert(0,r"D:\jason\Documents\Spring2020\CS344\cs344-code\tools\aima")
sys.path.insert(0,r"D:\jason\Documents\Spring2020\CS344\cs344-code\paip")
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import itertools


class TSP(Problem):
    """
    State: list of visited cities (ints)
    Move: the next city (int) to visit
    """
    
    def __init__(self, initial, maximum, array ,n):
        self.initial = initial
        self.array = array
        self.n = n
        self.maximum = maximum
        
    def actions(self, state):
        # return [state + self.delta, state - self.delta]
        actions = []
        for i in range(self.n):
            if i not in state:
                actions.append(i)
        return actions
    
    def goal_test(self, state):
            """Check to see if each city is visited."""
            for i in range(self.n):
                if i not in state:
                    return False
            return True

    def result(self, state, move):
        """Makes the given move on a copy of the given state."""
        new_state = state[:]
        new_state.append(move)
        return new_state
    
    def value(self, state):
        count = 0
        for i in range(len(state)):
            if i > 0:
                count-=self.array[state[i]][state[i-1]]
                count+=self.maximum
        return count


if __name__ == '__main__':
    n = 40
    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 10
    array = [[0 for x in range(n)] for y in range(n)]
    #initialize array.
    for i in range (0,n):
        for j in range (0,math.floor(i/2)):
            array[i][j] = randrange(5,maximum)
            array[j][i] = array[i][j]  
    ann_max = -100
    hill_max = -100
    for x in range(1,50):
        initial = [randrange(0,n)]
        p = TSP(initial, maximum, array,n)
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
        
    print('Hill-climbing max solution value: ' + str(-hill_max+maximum*n)
            )
    print('Simulated annealing max solution value: ' + str(-ann_max+maximum*n)
            )
