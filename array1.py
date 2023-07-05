# Given an array of integers and a value, determine if there are any two integers in the array 
# whose sum is equal to the given value. Return true if the sum exists, and false if it does not. 
# Consider the following array and its target sums

def sum(arr, val):
    found = []
    for num in arr: 
        if (val-num) in found: 
            return True
        found.append(num)
    return False 

print(sum([1, 2, 3], 5))
print(sum([1, 2, 3], 6))
print(sum([1, 2, 3], 3))
