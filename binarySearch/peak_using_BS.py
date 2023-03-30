# An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
#Given an array arr[] of size N, Return the index of any one of its peak elements.

def peakElement(arr, n): # n == len(arr)

    low = 0
    high = n - 1 

    while low <= high:
        mid = (high + low) // 2

        if mid == 0 or arr[mid] >= arr[mid - 1]:
            if mid == n - 1 or arr[mid] >= arr[mid + 1]:
                return mid 
            else:
                low = mid + 1
        else:
            high = mid - 1

    return -1 

# test 

arr = [14, 14, 10, 4, 13, 8, 17]
n = len(arr)
print(peakElement(arr, n))


