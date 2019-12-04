my_dict = {
    "class" : "animal",
    "name" : "giraffe",
    "age" : 10

}

print(my_dict)
print(my_dict["name"])
print(my_dict.get("age"))
print(my_dict.values())

for x in my_dict:
    print(my_dict[x])

for x,y in my_dict.items():
    print(x, y)

my_dict["name"] = "lion"
print(my_dict)

my_dict["color"] = "red"
print(my_dict)

print(my_dict.popitem())
print(my_dict)