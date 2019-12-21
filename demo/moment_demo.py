import moment

x= moment.now()
print(x)
x=moment.now().strftime("%d-%m-%Y_%H-%M-%S")
print(x)
x=moment.now().strftime("%m-%d-%Y_%H-%M-%S-%m")
print(x)