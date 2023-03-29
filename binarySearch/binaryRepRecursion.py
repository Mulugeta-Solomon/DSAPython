
# Binary representation of a number 
def binaryRep(n):  
    binary = []
    if n == 0:
        return 0
    binaryRep(n//2)
    print(n%2)

binaryRep(13)