'''
This module implements a simple classroom example of probabilistic inference
over the full joint distribution specified by AIMA, Figure 13.3.
It is based on the code from AIMA probability.py.

@author: kvlinden & Jason Pruim
@version Jan 1, 2013
'''
import sys
sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/aima")
sys.path.insert(0,"/home/jrp27/Documents/cs344-code/tools/paip")
from probability import JointProbDist, enumerate_joint_ask

# The Joint Probability Distribution Fig. 13.3 (from AIMA Python)
P = JointProbDist(['Toothache', 'Cavity', 'Catch', 'Rain'])
T, F = True, False
P[T, T, T,T] = 0.108/2; P[T, T, F,T] = 0.012/2
P[F, T, T,T] = 0.072/2; P[F, T, F,T] = 0.008/2
P[T, F, T,T] = 0.016/2; P[T, F, F,T] = 0.064/2
P[F, F, T,T] = 0.144/2; P[F, F, F,T] = 0.576/2

P[T, T, T,F] = 0.108/2; P[T, T, F,F] = 0.012/2
P[F, T, T,F] = 0.072/2; P[F, T, F,F] = 0.008/2
P[T, F, T,F] = 0.016/2; P[T, F, F,F] = 0.064/2
P[F, F, T,F] = 0.144/2; P[F, F, F,F] = 0.576/2

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())

# i. Now contains 2^4 or 16 entries.
# ii. The probabilities add up to one (as they always must). P(Sample Space) = 1. This is an axiom of probability.
# iii. Generally no. Probability assumes predicate logic. Predicat logic assumes that something is either true or not. This is not generally how the world works. There is gradient in how much it is raining, but that isn't part of this kind of probability work
# iv. Yes, The probability of Rain is 0.5, and the probabilities are the same with or without rain for any combination of the other variables.


PC = enumerate_joint_ask('Toothache', {'Rain': T}, P)
print(PC.show_approx())

"""
P(Rain) = 0.054+0.36+0.008+0.72+0.006+0.004+0.032+0.288=0.5
P(Toothache && Rain) = 0.054+0.008+0.006+0.032 =  0.1
P(Toothache| Rain) = P(Toothache&&Rain)/P(Rain) = 0.1/0.5 = 0.2

"""

"""
P(Catch) = 0.108+0.072+0.016+0.144 = 0.340
P(Cavity) = 0.108+0.072+0.012+0.008 = 0.200
P(Catch && Cavity) = 0.108+0.72 = 0.180
P(Catch|Cavity) = P(Catch&&Cavity)/P(Cavity) = 0.180/0.200=0.900

P(Cavity|Catch)= P(Catch|Cavity)P(Cavity)/P(Catch) = 0.9*0.2/0.34 = 0.529

"""

# New Coin flipping Probability
P2 = JointProbDist(['head1','head2'])
T,F = True, False
P2[T,T] = 0.25
P2[T,F] = 0.25
P2[F,T] = 0.25
P2[F,F] = 0.25

# P(head2|head1)
PC2 = enumerate_joint_ask('head2',{'head1':T},P2)
print(PC2.show_approx())
#Yes it should what I expected it to


