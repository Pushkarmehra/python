
class mergex:
    def __init__(self,num1,num2):
     self.num1=[int(x) for x in num1.split(',')]
     self.num2=[int(x) for x in num2.split(',')]
    def __add__(self):
        merge_list= self.num1 + self.num2
        return [x for x in merge_list if x !=0 ]
num1 = input("Enter numbers separated by commas: ")
num2 = input("Enter numbers separated by commas: ")
a=mergex(num1,num2)

print(a.__add__())