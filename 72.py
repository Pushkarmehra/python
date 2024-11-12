# class pc:
#     def parrent_m(self):
#         print('k')
    
# class cc(pc):
#     def parrent_m(self):
#         print('h')
#         super().parrent_m()
#     def child_m(self):
#        print("j")
#        super().parrent_m()
# a=cc()
# a.child_m()
# a.parrent_m()
class d:
    def __init__(self,m,n):
        self.name= n
        self.id=m
        
        
class programmer :
    def __init__(self,name,l,o):
        super().__init__(name,l)
        self.lang = o
rohan=d("rohan",24)
harry=programmer(11,"python")
print(rohan.id)