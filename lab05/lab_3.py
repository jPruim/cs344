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
joy = BayesNet([
    ('Raise', '', 0.01),
    ('Sunny', '', 0.7),
    ('Happy', 'Sunny Raise', {(T, T): 1, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

print("Excercise 5.3")
print(enumeration_ask('Raise', dict(Sunny = T), joy).show_approx())
print(enumeration_ask('Raise', dict(Happy = T, Sunny = T), joy).show_approx())



print(enumeration_ask('Raise', dict(Happy = T), joy).show_approx())
print(enumeration_ask('Raise', dict(Happy = T, Sunny = F), joy).show_approx())
"""
By hand work
P(R|S) = P(R) as they are independent ( so P(R) = 0.01)

P(H && S) = 0.7*(0.01*1+0.99*0.7) = 0.4921
P(R && H && S) = 0.7*(0.01*1) = 0.007
P(R | H && S) = P(R && H && S)/P(H && S) = 0.007/0.4921 = 0.014

The first is just how independence works (probability rules)
The second seems fine. Raises are way less likely to happen regardless of the mood. 0.01 is way lower than 0.7 for sunny.


P(H) = 0.7*0.01*1 + 0.7*0.99*0.7 + 0.3 * 0.01 * 0.9 + 0.3 * 0.99 * 0.1 = 0.5245
P(R && H) = 0.7*0.01*1+0.3 * 0.01 * 0.9 = 0.0097
P(R|H) = 0.0097/ 0.5245 = 0.0185

P(H && !S) = 0.3 * 0.01 * 0.9 + 0.3 * 0.99 * 0.1 = 0.0324
P(R && H && !S) = 0.3 * 0.01 * 0.9 = 0.0027
P(R|H && !S) =  0.0027/0.0324 = 0.0833

The probability of Raise given happy and not sunny is higher than the probability of Raise given happy because there not sunny is correlated to less happiness than sunny days. Thus there is a higher chance that happiness is "caused" by the raise being true.
"""