ph = open("i.txt", "r")
i = 0
while True:
    i += 1
    line = ph.readline()
    if not line:
        break
    m1, m2, m3 = line.strip().split(",")  # Corrected method from 'spill' to 'split' and added 'strip()'
    print(f"the no. of {i} is {m1}")
    print(f"the no. of {i} is {m2}")
    print(f"the no. of {i} is {m3}")
    
ph.close()  # Added to ensure the file is properly closed
