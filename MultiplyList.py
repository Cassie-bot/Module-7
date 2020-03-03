# Casandra Villagran
# 03/2/2020

# Write a Python function to multiply all
# the numbers in a list. Use list [5, 2, 7, -1].

def multiply(numbers):
    total = 1
    for x in numbers:
        total *= x
    return total
print(multiply((5, 2, 7, -1)))
