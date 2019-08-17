%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
male(aditya).
male(rishabh).

male(dhruv).
male(anurag).

male(sushil).
male(kshitij).
male(ritesh).
male(kharagsingh).
male(vipin).

female(ankita).
female(neha).
female(khyati).
female(ritu).
female(mahima).
female(abha).
female(shantidevi).
female(kantidevi).

wife(ritu, sushil).
wife(mahima, ritesh).
wife(abha, kshitij).
wife(kantidevi, kharagsingh).
wife(shantidevi, vipin).

mother(ritu, aditya).
mother(ritu, rishabh).
mother(abha, neha).
mother(mahima, dhruv).
mother(abha, anurag).
mother(shantidevi, sushil).
mother(shantidevi, kshitij).
mother(kantidevi, ritu).
mother(kantidevi, ritesh).
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Rules %
husband(A, B)       :- wife(B, A), male(A).
married(A, B)       :- wife(A, B).
married(A, B)       :- husband(A,B).
child(A, B)         :- husband(B, C), mother(C, A).
child(A, B)         :- mother(B, A).
son(A, B)           :- child(A, B), male(A).
daughter(A, B)      :- child(A, B), female(A).
parent(A, B)        :- mother(A, B).
parent(A, B)        :- father(A, B).
father(A, B)        :- child(B, A), mother(C, B), wife(C, A).
brother(A, B)       :- mother(C, A), mother(C, B), male(A).
sister(A, B)        :- mother(C, A), mother(C, B), female(A).
grandparent(A, B)   :- parent(C, B), parent(A, C).
grandfather(A, B)   :- grandparent(A, B), male(A).
grandmother(A, B)   :- grandparent(A, B), female(A).
grandson(A, B)      :- granparent(B, A), male(A).
granddaughter(A, B) :- grandparent(B, A), female(A).
sibling(A, B)       :- parent(C, A), brother(C, D), child(B, D).
sibling(A, B)       :- parent(C, A), sister(C, D), child(B, D).

