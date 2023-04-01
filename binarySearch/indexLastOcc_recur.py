## index of the last occurence using recursion

def lastIndex(arr, n):
    start = 0
    end = len(arr) - 1 

    while(start <= end):

        mid  = (start + end) // 2 

        
        if item > arr[mid]:
            start = mid + 1
        if item < arr[mid]:
            end = mid - 1
        if item == arr[mid]:
            if mid  == 0 or arr[mid+1] != arr[mid]:
                return f'index of the last occurence of {item} is: {mid}'
            else:
                start = mid + 1

    return f'there is no occurence of { item}'

arr = [1, 10, 10, 10, 20, 20, 40]
item = 30
print(lastIndex(arr, item))