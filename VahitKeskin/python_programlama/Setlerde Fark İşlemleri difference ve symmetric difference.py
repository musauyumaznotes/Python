#Setler - Klasik Kume Islemleri

# difference() ile iki kumunin farkini ya da "-" ifadesi 
# intersection() iki kume kesisimi ya da "&" ifadesi
# union() iki kumenin birlesimi 
# symmetric_difference() ikisinde de olmayanlari

#difference

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)

set2.difference(set1)

set1.symmetric_difference(set2)

set1 - set2
set2 - set1
