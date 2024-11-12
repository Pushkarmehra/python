# # a=input("hey enter your code")
# # print(a)
# # # Update the blanks in the code below
# # a=int(input(""))
# # print(a)
# # a,b,c = map(int,input().split())
# # print(a,b,c)
# a,b=map(input(),int)
# c,d,f=map(input(),int.split())
# g,h,i,j=map(input(),int.split())
# print(a,b,c,d,f,g,h,i,j)
# ph.close()



# ph = open("i.txt", "r")
# i = 0
# while True:
#     i += 1
#     line = ph.readline()
#     if not line:
#         break
#     m1, m2, m3 = line.strip().split(",")  # Corrected method from 'spill' to 'split' and added 'strip()'
#     print(f"the no. of {i} is {m1}")
#     print(f"the no. of {i} is {m2}")
#     print(f"the no. of {i} is {m3}")
    
# ph.close()  # Added to ensure the file is properly closed

# a,b=map(int,input("enter the first\n").split( ))
# c,d,e=map(int,input("enter the second\n").split( ))
# f,g,h,i=map(int,input("enter the third\n").split( ))
# print(a,b,c,d,e,f,g,h,i)
# N=int(input())
# S=(input())
# print(N,S)

# a=int(input())

# for i in range(a):  
#     b,c=map(int,input().split())
#     d,e,f=map(int,input().split())
#     print(b,c,d,e,f)
# t=int(input())
# for i in range(t):
#     n=int(input())
#     print(n+1)

    
class my:
    def __init__(self):
        self.nums=list(map(int,input().split()))
        self.target=input()
        return (self.nums in self.target)
    
my()
