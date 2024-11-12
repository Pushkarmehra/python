class emp:
    company="apple"
    def show(self):
        print(f"the name of {self.name} this is {self.company}")
    
    @classmethod
    def change(x,newcp):
        x.company=newcp
        
        
        
ep1=emp()
ep1.name="pushkar"
ep1.show()
ep1.change("hellno")
ep1.show()
print(emp.company)