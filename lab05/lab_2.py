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
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('T1', 'Cancer', {T: 0.9, F: 0.2}),
    ('T2', 'Cancer', {T: 0.9, F: 0.2}),
    ])



print("Excercise 5.2")
print(enumeration_ask('Cancer', dict(T1 = T, T2 = T), cancer).show_approx())
print(enumeration_ask('Cancer', dict(T1 = T, T2 = F), cancer).show_approx())

"""
By hand work

P(C) = 0.01
P(T1|C) = 0.9
P(T2|C) = 0.9
P(T1) = 0.9*0.01+0.99*0.2 = 0.207
P(T2) = 0.9*0.01+0.99*0.2 = 0.207
P(T1 && T2) = 0.01*0.9*0.9 + 0.99*.2*.2 = 0.0477
P(C && T1 && T2) = 0.01*0.9*0.9 = 0.0081
P(C|T1 && T2) = P(C && T1 &&T2)/P(T1 && T2) = 0.0081/0.0477 = 0.17



P(T1 && !T2) = 0.01*0.9 * 0.1 + 0.99*0.8*0.2 = 0.1593
P(C && T1 && !T2) = 0.01*0.9 * 0.1 = 0.0009
P(C|T1 && !T2) = P(C && T1 && !T2)/ P(T1 && !T2) = 0.0009/0.1593 = 0.00565


Both of these results make sense due to the extreme rarity of having the disease. This is a classic intro to probability excercise.
Failing one test makes it about one third as likely to actually have cancer.

"""