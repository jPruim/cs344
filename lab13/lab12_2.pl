bread  =  bread % true
’Bread’  =  bread % false
food(X)  =  food(bread) % true X = bread
food(bread,X)  =  food(Y,sausage) % true, X = sausage, Y = Bread)
meal(food(bread),X)  =  meal(X,drink(beer)) % false



house_elf(dobby).
witch(hermione).
witch(’McGonagall’).
witch(rita_skeeter).
magic(X):-  house_elf(X).
magic(X):-  wizard(X).
magic(X):-  witch(X).


?-  magic(house_elf). % false
?-  wizard(harry). % false
?-  magic(wizard). % false
?-  magic(’McGonagall’). % true
?-  magic(Hermione). 
%%    Hermione = dobby;
%%    Hermione = hermione;
%%    Hermione = 'McGonagall';
%%    Hermione = rita_skeeter.
%Prolog unification happens by checking if there exists a substation of the system where the values of the two sides are equivallent.
% I had to add in a wizard(ron) to get the program to not crash on wizard having no use. Not sure if that is what you were looking for for reasoning.