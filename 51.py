with open("n.txt","w") as f:
    # print(type(f))
    # f.seek(2)#this 
    # print(f.tell())
    # data=f.read(10)
    # print(data)
    f.write('helloworld')
    f.truncate(6)