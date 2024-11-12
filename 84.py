
# def hi():
#     i=0
#     while (i<=100):
#         print(i)
#         i=i+10
# def ki():
#     for i in range(8):
#         print(i)
        
# t2 = time.time( )
# hi()
# print(time.time( )-t2)
# init = time.time( )
# ki()
# print(time.time( )- init )
# time delay
# print('0')
# time.sleep(10)
# print("this the print")
import time
t=time.localtime( )
formatted_time= time.strftime("%y-%m-%d %H:%M:%S", t)
print(formatted_time)