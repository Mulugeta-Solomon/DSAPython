# best case big_theta(n)
# worst case big_theta(n^2)

def insertionSort(l):
    for i in range(1,len(l)):
        X = l[i] ## index 1 element
        j = i-1
        
        while j >= 0 and X < l[j]:
            l[j+1] = l[j] # index 0 is empty now 
            j -= 1
        l[j+1] = X # insert index 1 element to index 0 

l = [5, 8, 9, 2, 6, 7, 6, 2, 7, 10, 100]
insertionSort(l)
  