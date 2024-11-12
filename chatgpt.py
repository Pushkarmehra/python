import os

# Uncomment the following lines if you want to rename directories and create new ones
# for i in range(5):
#     os.rename(f"day-{i+1}", f"tutorial-{i+1}")

# Check if "data2" directory exists, if not, create it
if not os.path.exists("data2"):
    os.mkdir("data2")

# Uncomment the following lines if you want to create new directories
# for i in range(2):
#     os.mkdir(f"date-{i+1}")

# List and print contents of "data" directory
folder = os.listdir("data")
for i in folder:
    print(i)
    print(os.listdir(f"data/{i}"))
