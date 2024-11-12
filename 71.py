# x=(1,1,4,5)
# print(dir(x))
# print(x.__add__)

class h:
    def __init__(self,n,m):
        self.name= n
        self.mane= m

a=h("hello","hio")
print(a.__dict__)

print(help(h))