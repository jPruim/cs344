iswitch(hekate).
iswitch(X):-madeofwood(X).
madeofwood(X):-floats(X).
floats(X):-isDuck(X).
isDuck(X):-weighssameasduck(X).
weighssameasduck(accused).


?-iswitch(accused).
