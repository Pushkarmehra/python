
class emp:
    name="pristane"
    def __len__(self):
       
        i=0
        for c in self.name:
            i=i+1
        return i
    
e = emp()
print(e.name) 
print(len(e))
