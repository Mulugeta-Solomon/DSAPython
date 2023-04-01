## naive approach to merge two sorted arrays 

def naiveMerge(l1,l2):
    merged = []
    i, j = 0, 0

    while(max(i,j) <= max(len(l1)-1,len(l2)-1)):
     #while i < len(l1) and j < len(l2)
        if l1[i] <= l2[j]:
            merged.append(l1[i])
            i += 1
            if (i == len(l1)):
                break
        if l1[i] > l2[j]:
            merged.append(l2[j])
            j += 1
            if (j == len(l2)):
                break 
    if (i == len(l1)):
        for x in range(j, len(l2) - 1):
            merged.append(l2[x])
    else:
        for x in range(i, len(l1) - 1):
            merged.append(l1[x])
    
    return merged


l2 = [2, 2, 5, 6, 6, 7, 7]
l1 = [1, 3, 4]
naiveMerge(l1,l2)
