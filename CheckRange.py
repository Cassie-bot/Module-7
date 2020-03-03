# Casandra Villagran
# 03/2/2020

# Write a Python function to check whether a number is in a given range.
# Use range(1,10). Print whether the number is in or not in the range.

def test_range(n):
    if n in range(1,10):
        print(str(n)," is in the range")
    else :
        print("The number is outside the given range. ")
(test_range(6))
