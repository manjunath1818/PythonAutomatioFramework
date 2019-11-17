def printHello():
    print("Hello")

printHello()

def printHi(name="sanju"):
    print("Hi " +name)

printHi()
printHi("Manju")

def returnSum(a,b):
    """This is the return function to calclulate sum of two numbers"""
    return(a+b)

x = returnSum(10,20)
print(x)