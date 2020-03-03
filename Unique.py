# Casandra Villagran
# 03/2/2020

# Write a Python function that takes a list of numbers and returns a new list
# with unique elements of the first list. Use list [1, 3, 3, 3, 6, 2, 3, 5].

# Use the append function.

def unique(mylist) :
    unique_list = []
    for x in mylist:
        if x not in unique_list:
            unique_list.append(x)
    for x in unique_list:
        print(x, end=" ")

mylist = [1, 3, 3, 3, 6, 2, 3, 5]
print("The unique values from the list are")
unique(mylist)
