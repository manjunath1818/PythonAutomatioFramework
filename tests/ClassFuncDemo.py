class MyClass:
    name = "Manju"

    def __init__(self, name ,age):
        self.name = name
        self.age = age


#self is the variable used as the very first parameter/argumnet for every function
    def sum(self, a, b):
        print(a+b)


x = MyClass("manju", 33)
print(x.name)
print(x.age)
x.sum(4,5)

#__init__ built in functions which is always preset