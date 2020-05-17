directlyin(olga,katarina).
directlyin(natasha,olga).
directlyin(irina,natasha).
in(X,Y) :- directlyin(X,Y).
in(X,Y) :- directlyin(X,Z),
      in(Z,Y).

?-in(natasha,katarina).
?-in(katarina,natasha).

tran(eins,one).
tran(zwei,two).
tran(drei,three).
tran(vier,four).
tran(fuenf,five).
tran(sechs,six).
tran(sieben,seven).
tran(acht,eight).
tran(neun,nine).

listtran([],[]).
listtran([a|Ta],[b|Tb]):-tran(a,b),listtran(Ta,Tb).
?-listtran(X,[one,seven,six,two]).


/**
*Does Prolog implement a version of generalized modus ponens (i.e., modus ponens with variables and instatiation)? If so
*, demonstrate how it’s done; if not, explain why not. If it doesn’t, can you implement one? Why or why not?
* My understanding is that it doesn't implement a generalized modus ponens because it only does Horn clauses.
* Thus a implies b can be written as b:-a, but a implies b or c is unwrittable in normal prolog. Now, it is possible to 
* expand the a implies b or c into just ands and ors. Thus a implies b or c is (b or c) or not a. In prolog this would be ((b;c); Not(a)).
* However, I believe the computation in prolog has some different results with how it works.
* Thus it doesn't really have a generalized modus ponens.
 */
