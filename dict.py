import pickle
while True:
    ch=int(input('''Choose any one of the program to run
1.Create a dictionary
2.Display the dictionary'''))
    if ch==1:
        f=open("BT.dat",'wb')
        d={}
        n=int(input('Total number of entries'))
        for i in range(n):
            admn=int(input("Enter admission number"))
            name=input("Enter Name")
            cls=input("Enter class")
            d[admn]=(name,cls)
        pickle.dump(d,f)
    elif ch==2:
        f=open('Bt.dat','rb')
        print(pickle.load(f))
            
        
        
