my_list = ["tokyo", "canada", "newyork"]
print(my_list)

my_list[2] = "bangalore"
print(my_list)

for val in my_list:
    print(val)

print(len(my_list))

my_list.append("Boston")
print(my_list)
my_list.insert(1,"pune")
print(my_list)

my_list.remove("bangalore")
print(my_list)

my_list.pop()
print(my_list)

my_list.pop(1)
print(my_list)

del my_list[1]
print(my_list)

fruits = ["apple", "banana", "mango"]
print(fruits)
fruits.reverse()
print(fruits)

my_list_2 = ["manju", [1,2,3], ['a','b']]
print(my_list_2)
print(my_list_2[1][1])