import time
import asyncio
async def fun1():
    await asyncio.sleep(3)
    print("fun1")
async def fun2():
    await asyncio.sleep(1)
    print("fun2")
async def fun3():
    await asyncio.sleep(3)
    print("fun3")
     
# async def main():
#     task= asyncio.create_task(fun1())
#     await fun2()
#     await fun3()
    
# asyncio.run(main())
