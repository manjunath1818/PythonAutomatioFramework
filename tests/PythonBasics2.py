num = -1
if num > 0:
    print("This is a positive number")
elif num == 0:
    print("The number is zero")
else:
    print("This is a negative number")


num = [10,20,30,40]
sum = 0
for val in num:
    sum = sum+val
print("Total is : " , sum)

num = 5
sum = 0
i = 1

while i<num:
    sum = sum+i
    i = i+1
print("The total :", sum)