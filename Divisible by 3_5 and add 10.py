def push3_5(N):
    only3_5=[]
    for j in N:
        if j%5==0 or j%3==0:
            only3_5.append(j+10)
    return only3_5
                       

Num=[]
for i in range(5):
    n=int(input("Enter Number"))
    Num.append(n)
x=push3_5(Num)
print(x)
