#Question:WAP to assign 10 int elements and give their location and also print a message if they don't exist
l=[]
for i in range (10):
    num=int(input("Enter numbers"))
    l.append(num)
ind=eval(input("Enter number to find"))
for j in l:
    if j==ind:
        print("Index of the element",ind,"is",l.index(j))
        break
    else:
        print("Element not there")
        break    
