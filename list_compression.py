#!/usr/bin/python3

#taking 2 divide numer in list and append in new list
#normal method
k = [1,2,3,4,5,6,7,8,9,0]
new = []
for i in  k :
    if i % 2==0:
        new.append(i)
print(new)

#list comprehension method

m = [i for i in range(10) if i%2 == 0 ]
print(m)
