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
P = JointProbDist(['Toothache', 'Cavity', 'Catch'])
T, F = True, False
P[T, T, T] = 0.108; P[T, T, F] = 0.012
P[F, T, T] = 0.072; P[F, T, F] = 0.008
P[T, F, T] = 0.016; P[T, F, F] = 0.064
P[F, F, T] = 0.144; P[F, F, F] = 0.576

# Compute P(Cavity|Toothache=T)  (see the text, page 493).
PC = enumerate_joint_ask('Cavity', {'Toothache': T}, P)
print(PC.show_approx())
PC = enumerate_joint_ask('Cavity', {'Catch': T}, P)
print(PC.show_approx())


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


