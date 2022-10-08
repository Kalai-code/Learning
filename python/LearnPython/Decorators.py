def decorate_it(func):
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

@decorate_it
def hello():
    print("Hello world")

hello()

def outerfunc(func):  
    print("This is outer function")
    def innerfunc():       
        func()
        print("This is inner function")
    return innerfunc

def middlefunc():
    print("This is middle function")

middlefunc = outerfunc(middlefunc)

middlefunc()

def headerfunc(func):   
    def footerfunc():
        print("Hello There!")
        func()
        print("Enjoy Learning!!")
    return footerfunc

@headerfunc
def bodyfunc():
    print("Are you ready to Learn Python?")

bodyfunc()
