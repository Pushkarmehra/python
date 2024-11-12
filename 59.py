def greet(fx):
    def mfx():
        print("good morning")
        fx()
        print("thx for using this program")
    return mfx

@greet
def hello():
    print("hello world")
    
hello()