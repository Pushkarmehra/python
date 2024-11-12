import os
# for i in range(5):
    # os.rename(f"day-{i+1}", f"tutorial-{i+1}")
# if (not os.path.exists):
    # os.mkdir("data2")
# for i in range(0,2):
    # os.mkdir(f"date-{i+1}")
folder= os.listdir("data")
for i in folder:
    print(i)
    print(os.listdir(f"data/{i}"))