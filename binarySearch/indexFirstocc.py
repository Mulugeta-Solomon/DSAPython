# index of first occurence of  an item in sorted array 
# iterative method is an efficient compared to recursion because of constant auxiliary space   

def indexFirstOccurence(arr, item): ## complexity O(logn) and auxialiary space O(1) 
    start = 0
    end = len(arr) - 1 

    while(start <= end):

        mid  = (start + end) // 2 

        
        if item > arr[mid]:
            start = mid + 1
        if item < arr[mid]:
            end = mid - 1
        if item == arr[mid]:
            if mid  == 0 or arr[mid-1] != arr[mid]:
                return f'index of the first occurence of {item} is: {mid}'
            else:
                end = mid - 1

    return f'there is no occurence of { item}'


arr = [1, 10, 10, 10, 20, 20, 40]
item = 10
print(indexFirstOccurence(arr, item))


## index of the first occurence using recursion

def firstOccurence(arr, n, low, high):  ## complexity O(logn) and auxialiary space O(logn)
    if low > high:
        return -1 
    
    mid = (high + low) // 2 
    if n > arr[mid]:
        return firstOccurence(arr, n, mid + 1, high)
    if n < arr[mid]:
        return firstOccurence(arr, n, low, mid - 1)
    if n == arr[mid]:
        if mid == 0 or arr[mid - 1] != arr[mid]:
            return mid
        else:
            return firstOccurence(arr, n, low, mid - 1)
arr = [1, 10, 10, 10, 20, 20, 40]
item = 20
print(firstOccurence(arr, item, 0, len(arr) - 1))
