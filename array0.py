# Given an array of positive numbers ranging from 1 to n, 
# such that all numbers from 1 to n are present except one number x, find x. 
# Assume the input array is unsorted.

def find_missing(arr):
    sumtotal= (len(arr)+1) * (len(arr)+2) / 2
    for num in arr: 
        sumtotal -= num 
    return sumtotal

print(find_missing([10, 1, 2, 3, 4, 5, 7, 8 , 9]))