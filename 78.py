class cl:
    def __init__(self,n,m):
        self.name=n
        self.id=m
    
class cr(cl):
    def display(self):
     return f"my name is {self.name} and my id is {self.id}" 
 
a=cr("pushkar",89)
print(a.display())