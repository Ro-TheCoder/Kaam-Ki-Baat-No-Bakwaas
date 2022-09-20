def replace_num():
    n=int(input("Enter total number of elements"))
    l=[]
    for i in range(n):
        element=int(input("Enter numbers"))
        if element>0:
            l.append(+1)
        elif element<0:
            l.append(-1)
    return l

x=replace_num()
print(x)      
