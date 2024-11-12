import  threading
import time

def fun(sec):
    print(f"slepp for{sec} second")
    time.sleep(sec)
    
    
# fun(1)
# fun(2)
t= threading.Thread(target=fun,args=[6])
t2= threading.Thread(target=fun,args=[4])  
t3= threading.Thread(target=fun,args=[5])

t.start()
t2.start()
t3.start()