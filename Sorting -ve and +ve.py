def shift():
    L=[]
    n=int(input("Enter total number of elements"))
    for j in range(n):
        elements=int(input("Enter numbers"))
        L.append(elements)
        
    for i in range(len(L)):
        if L[i]<0:
            L.append(L[i])
            L.remove(L[i])
        return L
x=shift()
print(x)
