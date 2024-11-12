try:
    a=int(input("enter your no."))
    print(a) if 5>a>4 else print("hi")
except ValueError:
    print("enter a number")