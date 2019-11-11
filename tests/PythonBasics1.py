def sum(a,b):
    print(a+b)

x = sum(10,20)

x = 2
y = 2.5
z = 4j

print(type(x))
print(type(y))
print(type(z))

# casting

x = int(2) # 2
y = int(2.5)  #2
z = float(1)  # 1.0
p = str(10)  # "10"

print(x)
print(y)
print(z)
print(p)

x = "  Welcome,Manju"
print(x.lower())
print(x.strip())
print(x.replace("e","a"))
print(x.split(","))

print("Enter the number : ")
x = input()
print("Number Entered is :" +x)