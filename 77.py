class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k
        
     
    def __str__(self):
        return f"{self.i}i,{self.j}j,{self.k}k"
    def __add__(self,x):
        return f"{self.i+x.i}i,{self.j+x.j}i,{self.k+x.k}i"
    
v= vector(4 , 5 , 7)
print(v)
v2=vector(1,5,9)
print(v2)
print(v+v2)