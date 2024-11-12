# THIS IS FOR READING 
# t=open("h.txt","r")# r mode is defalte we add rb if we want to open binarry file 
# # print(t)
# hi = t.read()
# print(hi)



#THIS IS FOR WRITING
# t=open("p.txt","w")#if you write the file name which is not preaswnt than it will create automatcali
# t.write("hello world")
# t.close() this will re write 
  
# # FOR APPEND (this will add )
# t=open("p.txt","a")
# t.write("\nhell yeah")
# t.close()

with open("p.txt","a")as f:
    f.write("\n hell yeah:)")