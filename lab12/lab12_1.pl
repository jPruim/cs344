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