f=open("Calc.txt",'r')
while True:
    ch=input('''Output:
A.Display whole content
B.Display n characters
C.Display first lines
D.Display each line as a string in list
E.Display each character
F.Count all the characters
G.Count vowels
H.Count blank spaces
I.Count characters in lower, upper and digits
J.Count number of words
''')
    if ch=='A':
        print(f.read())         #to display whole content
    elif ch=='B':
        n=int(input("Characters to be displayed"))
        print(f.read(n))        #to display first x character only
    elif ch=='C':
        print(f.readline())     #to display first line 
    elif ch=='D':
        print(f.readlines())    #to display each line as a string in list
    elif ch =='E':
        j=f.read()              #to display every single charcater
        for i in j:
            print(i)
    elif ch=='F':               #Count the characters
        a=0
        j=f.read()
        for i in j:
            a+=1
        print(a)
    elif ch=='G':               #Count vowels
        j=f.readlines()
        a=0
        v=['a','e','i','o','u']
        for i in j:
            i.lower()
            for k in i:
                for l in v:
                    if k==l:
                        a+=1
        print(a)
    elif ch=='H':               #Count Blank Spaces
        a=0
        j=f.read()
        j.lstrip()
        j.rstrip()
        for i in j:
            if i==" ":
                a+=1
        print("Total blank spaces =",a)
    elif ch=="I":               #Count upper lower and digits
        j=f.read()
        l=0
        u=0
        d=0
        for i in j:
            if i.islower()==True:
                l+=1
            elif i.isupper()==True:
                u+=1
            elif i.isdigit()==True:
                d+=1
        print("Lower characters =",l)
        print("Upper characters =",u)
        print("Digits=",d)
    elif ch=='J':
        l=[]
        j=f.read()
        j.lstrip()
        j.rstrip()
        E=j.split(" ")
        for x in E:
            l.append(a for a in x.split("/n"))

        print(l)
        print("Total number of words",len(l))
        
        
                    
                    
                
    
            

