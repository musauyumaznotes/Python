#Set Sorgu Islemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

# Iki kumenin kesisiminin bos olup olmadiginin sorgulanmasi

set1.isdisjoint(set2)


#bir kumenin butun elemanlarinin baska bir kume icerisinde yer alip almadigi

set1.issubset(set2)

# bir kumenin bir diger kumeyi kapsayip kapsamadigi

set2.issuperset(set1)
