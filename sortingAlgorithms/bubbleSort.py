def bubbleSort(l):
    for i in range(len(l)-1):
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

l = [5, 8, 9, 2, 6, 7, 6, 2, 7, 10, 100]
bubbleSort(l)

