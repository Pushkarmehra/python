l=[3,4,7,5,8,4,4]
r=[1,4,6,8,5,9]
l.append(7)
# l.sort(reverse=True)
l.sort()
l.remove(4)
a=l.count(4)
print(a)
l[1]= 90
print(l)
m=l+r
m[4]=67
print(m)
