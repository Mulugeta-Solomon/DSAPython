# Quick sort algorithm using lomuto partition

def quickSort(arr, low, high):
    if high > low:
        p = lomutoPartition(arr, low, high)
        quickSort(arr, low, p-1)   # the main difference between lomuto and hoare alg
        quickSort(arr, p + 1, high)

def lomutoPartition(arr, low, high):
    pivot = arr[high]
    i = low - 1 
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i+1

#l = [5, 3, 8, 4, 2, 7, 1, 10]
l = [5, 8, 9, 2, 6, 7, 6, 2, 7, 10, 100]
quickSort(l, 0, len(l) - 1)
print(l)