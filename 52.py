def susu(fx,x):
    return fx(x)
# print(susu(8))

# h= lambda x:x*8
# print(h(8))
# j= lambda x,y : (x+y)/2
# print(j(2,2))
# l= lambda x: x/2
print(susu(lambda x:x*x*x,2))