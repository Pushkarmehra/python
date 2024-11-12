# ph = open("i.txt","r")
# i = 0
# while True:
#     i=i+1
#     line = ph.readline()
#     if not line:
#      break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3= line.split(",")[2]
#     print(f"the no. of {i} is {m1}")
#     print(f"the no. of {i} is {m2}")
#     print(f"the no. of {i} is {m3}")
#     print(line)
# ph.close()

pj=open("k.txt","w")
lines= ['line1\n','line2\n','line3\n']
pj.writelines(lines)
pj.close()