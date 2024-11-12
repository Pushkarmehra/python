x=7
print(f"gloable x is {x}")

def hello():
    # global x it will change globle varble
    x=5
    print(f"local x is  {x}")
    print(x)
    y=4
hello()
    
print(x) 
# print(y) local varble we can't put the value from function outside the function