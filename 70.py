class emp:
    def __init__(self,n,m):
        self.name=n
        self.salary=m
    @classmethod
    def fromstr(cls,string):
        return cls(string.split("-")[0],string.split("-")[1])
string = "jhon-1200"
e=emp.fromstr(string)
print(e.name)
print(e.salary)
