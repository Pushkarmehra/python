class employ:
    company_name= "apple"
    noofemp=0
    def __init__(self,name):
        self.name=name
        self.raise_amount= 0.02
        employ.noofemp += 1
    def showdetail(self):
        print(f"the name of the employ is {self.name} and the raise amount is {self.raise_amount} of {self.company_name} from {self.noofemp}")
        
        
emp1=employ("pushkar")
emp1.raise_amount=0.3  
emp1.company_name="apple india"
employ.company_name="google"
emp1.showdetail()
# employ.showdetail(emp1)
     
emp2=employ("pristane")
emp2.company_name= "nescle"
emp2.showdetail()