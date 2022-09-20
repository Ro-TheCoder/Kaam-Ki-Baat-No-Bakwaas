while True:
    ch=int(input('''Choose program
1.Make a calculator with some text
2.Read the file using read()
3.Read using read(n)
4.Read using readline()
5.Read using readlines()
6.Count the number of characters
7.Count total number of vowels
8.Count blank spaces
9.Display lines starting with a specific alphabet
10.Display only last line with total number of lines
11.Display only those words which are less than 4 letters
12.Displays the longest line'''))

    if ch==1:
        f=open("Calculator.txt",'w')
        n1=int(input("Enter number"))
        n2=int(input("Enter number"))
        f.write("The numbers are ")
        f.write(str(n1))
        f.write(" and ")
        f.write(str(n2))
        f.write('''
Sum of the numbers - ''')
        f.write(str(n1+n2))
        f.write('''
Subtraction of the number - ''')
        f.write(str(abs(n1-n2)))
        f.write('''
Multiplication of the numbers - ''')
        f.write(str(n1*n2))
        f.close()
    
    elif ch==2:
        f=open("Calculator.txt",'r')
        print(f.read())
    
    elif ch==3:
        f=open("Calculator.txt",'r')
        n=int(input("Enter number of characters to be displayed"))
        print(f.read(n))

    elif ch ==4:
        f=open("Calculator.txt",'r')
        print(f.readline())

    elif ch==5:
        f=open("Calculator.txt",'r')
        print(f.readlines())

    elif ch==6:
        f=open("Calculator.txt",'r')
        count=0
        for i in f.read():
            count+=1
        print("Total number of characters are ", count)

    elif ch==7:
        f=open("Calculator.txt",'r')
        count=0
        for j in f.read().lower():
            if j=='a' or 'e' or 'i' or 'o' or 'u':
                count+=1
                
        print("Total number of vowels are", count)

    elif ch==8:
        f=open("Calculator.txt",'r')
        count=0
        for i in f.read():
            if i ==" ":
                count+=1
        print("Total blank spaces are - ",count)

    elif ch==9:
        f=open("Calculator.txt",'r')
        alpha=input("Enter the alphabet")
        for i in f.readlines():
            if i.startswith(alpha)==True:
                print(i.lstrip('/n'))

    elif ch==10:
        f=open("Calculator.txt",'r')
        t=f.readlines()
        print("Last line is ", t[-1].lstrip('/n') ," and total number of lines are", len(t))

    elif ch==11:
        f=open("Calculator.txt",'r')
        for i in f.read().split(" "):
            if len(i)<4:
                print (i)

    elif ch==12:
        f=open("Calculator.txt",'r')
        a=0
        for i in f.readlines():
            if len(i)>a:
                line=i
                a=len(i)
            else:
                pass
        print("Longest line is" , line)
            
