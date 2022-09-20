f=open("Calc.txt","w")
n1=float(input("Enter first number"))
n2=float(input("Enter second number"))
while True:
    ch=input('''Enter one of the following options to perform the operation on the numbers
(A) Sum
(B) Subtract
(C) Multiply
(D) Divide''')
    if ch=='A':
           f.write(str(n1+n2))
    elif ch=='B':
           f.write(str(n1-n2))
    elif ch=='C':
           f.write(str(n1*n2))
    elif ch=='D':
           f.write(str(n1/n2))
    f.write('''
Here's your answer''')
    f.close()
           
           
       
             
