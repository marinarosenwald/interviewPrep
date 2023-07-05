# Given an array of integers and a value, determine if there are any two integers in the array whose sum is equal to the given value.

#n^2 runtime 
def two_int (arr, num):
    base=0 
    curr=1
    newSum = 0

    while base<len(arr): 
        curr = base + 1
        while curr<len(arr):
            newSum = arr[base] + arr[curr]
            if newSum == num:
                return True
            
            curr+=1
        base+=1 
    
    return False 

#n runtime 
def two_int1 (arr, num):
    for i in arr:
        if num-i in arr:
            return True
    return False 

print(two_int1([1, 2, 3], 3))