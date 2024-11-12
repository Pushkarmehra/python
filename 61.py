class employe:
    def __init__(self,m,n):
        self.name = m
        self.id=n 
        
    def showdetail(self):
        print(f"""the name of the employe is {self.name} and id is {self.id}""")
        

class programmer(employe) :
    def showlanguage(self):
        print("helllo")
e= programmer("pushkar",89) # type: ignore
e.showdetail()
e.showlanguage() 