'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''
import sys
# sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/aima")
# sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/paip")
sys.path.insert(0,r"D:\jason\Documents\Spring2020\CS344\cs344-code\tools\aima")
sys.path.insert(0,r"D:\jason\Documents\Spring2020\CS344\cs344-code\paip")
from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
weather = BayesNet([
    ('Cloudy', '', 0.5),
    ('Sprinkler', 'Cloudy',{T:0.1, F:0.5}),
    ('Rain', 'Cloudy',{T:0.8, F:0.2}),
    ('WetGrass', 'Sprinkler Rain', {(T, T): 0.99, (T, F): 0.90, (F, T): 0.90, (F, F): 0.00})
    ])

print("Excercise 5.1")
print(enumeration_ask('Cloudy', dict(), weather).show_approx())
print(enumeration_ask('Sprinkler', dict(Cloudy = T), weather).show_approx())
print(enumeration_ask('Cloudy', dict(Sprinkler = T, Rain = F), weather).show_approx())
print(enumeration_ask('WetGrass', dict(Cloudy = T, Sprinkler = T, Rain = T), weather).show_approx())
print(enumeration_ask('Cloudy', dict(WetGrass = F), weather).show_approx())

