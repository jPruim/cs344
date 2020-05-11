killer(butch).
married(mia,marcellus).
dead(zed).
kills(marcellus, X):-gives FootMassage(X,mia).
eats(jules,X) :- nutritious(X).
eats(jules, X) :- tasty(X)
%when in doubt, I make the verb the "function" part of the fact and the knowns the "variables". Specifically in S, IO, DO order.
%Classic Math convention of variables


wizard(ron).
hasWand(harry).
quidditchPlayer(harry).
wizard(X):-  hasBroom(X),  hasWand(X).
hasBroom(X):-  quidditchPlayer(X).

wizard(ron). % true
witch(ron). % undefined procedure
wizard(hermione). % false
witch(hermione). % undefined procedure
wizard(harry). % true
wizard(Y). % Y is ron or harry
witch(Y). % undefined

%Prolog goes through the different rules and facts and figures out what it can prove and know. Everything else is false (often with error messages)