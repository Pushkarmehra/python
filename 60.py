class my :
    def __init__(self,value):
        self._value=value
        
    def show(self):
        print(f"value of {self._value}")
        
    @property
    def ten_value(self):
        return 10* self._value
    
obj= my(10)
print(obj.ten_value)
obj.show()