# o= lambda x: x*x*x
from functools import reduce
i=[1,2,3,4,5,6]
# newi=list(map(o,i))
# print(newi)

# #filter
# j= lambda x:x>=2
# newnewi=list(filter(j,i))
# print(newnewi)

#reduce
tatai= reduce(lambda x,y:x*y,i)
print(tatai)