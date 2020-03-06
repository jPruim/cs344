'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
'''
import sys
sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/aima")
sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/paip")
from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# Compute P(Burglary | John and Mary both call).
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# elimination_ask() is a dynamic programming version of enumeration_ask().
print(elimination_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# gibbs_ask() is an approximation algorithm helps Bayesian Networks scale up.
print(gibbs_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
# See the explanation of the algorithms in AIMA Section 14.4.


print("Excercise 5.1")
print(enumeration_ask('Alarm', dict(Burglary = T, Earthquake = F), burglary).show_approx())
print(enumeration_ask('JohnCalls', dict(Burglary = T, Earthquake = F), burglary).show_approx())
print(enumeration_ask('Burglary', dict(Alarm = T), burglary).show_approx())
print(enumeration_ask('Burglary', dict(JohnCalls = T, MaryCalls = T), burglary).show_approx())

"""
Elimination ask is another algorithm that perfectly ends up with the distribution
Gibbs ask is just running the probabilities a certain number of times and spitting out an answer. Should average the correct answer, but won't necassarily be right (or even particularly close)
I only see two though. So I don't know what the third is supposed to be.

"""