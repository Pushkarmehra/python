import functools
import time
@functools.lru_cache
def f(n):
    time.sleep(5)
    return n*5

print(f(2)) 
print("donne for 20")
print(f(20))
print("donne for 20")
print(f(6))
print("done for 6")
print(f(2)) 
print("donne for 20")
print(f(20))
print("donne for 20")
print(f(61 ))
print("done for 6")