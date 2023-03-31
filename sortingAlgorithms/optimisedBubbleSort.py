def optimiseBubbleSort(l):
    for i in range(len(l)-1):
        swapped = False
        for j in range(len(l)-i-1):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                swapped = True
        if swapped == False:
            return 
l = [5, 8, 9, 2, 6, 7, 6, 2, 7, 10, 100]
optimiseBubbleSort(l)
l 