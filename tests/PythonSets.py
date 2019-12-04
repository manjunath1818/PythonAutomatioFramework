my_set = {"chalk", "Duster", "Board"}
print(my_set)


for x in my_set:
    print(x)

print("chalk" in my_set)

my_set.add("pen")  # Adding single element
print(my_set)  # unordered

my_set.update(["paper","book"]) # Adding multiple element
print(my_set)

my_set.remove("book")
my_set.discard("Pen")
print(my_set)
#my_set.remove("book")
my_set.discard("Pen")

my_list = [1,2,3]
my_set_2 = set(my_list)  # list to set
print(my_set_2)

A = {'A','B',1,2,3}
B = {'C','A',3,4,5}
print(A | B) # union
print(A & B) #intesection
print(A - B) # not present in b
print(A ^ B) # Symmnetrric difference