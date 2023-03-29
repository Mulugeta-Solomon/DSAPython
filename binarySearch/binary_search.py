## binary search using recursion

def binarySearch(arr, n, start, end):
    
    if start > end:
        return -1
    
    mid = (start + end) // 2
    
    if n == arr[mid]:
        return arr.index(arr[mid])
    if n > arr[mid]:
        return binarySearch(arr, n, mid + 1, end)
    if n < arr[mid]:
        return binarySearch(arr, n, start, end - 1)
    
        
arr = [10, 20, 30, 40, 50, 60]
n = 100       
binarySearch(arr, n, 0, len(arr) -1)


## binary search iterative

def bSearch(arr, n):
    
    start = 0
    end = len(arr) - 1
    
    while start <= end:
        mid = (start + end) // 2 
        
        if n == arr[mid]:
            return mid 
        if n > arr[mid]:
            start = mid + 1
        if n < arr[mid]:
            end = mid - 1
        
    return -1

arr = [10, 20, 30, 40, 50, 60]
n = 60
bSearch(arr, n)
 