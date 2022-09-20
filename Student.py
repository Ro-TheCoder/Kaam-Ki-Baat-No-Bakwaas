import pickle
while True:
    ch=int(input('''Enter the following option
1. Create Dictionary File
2. Reading Dictionary
3. Deletion of a record'''))
    if ch==1:
        f=open('Student.dat','wb')
        n=int(input("Enter total number of records"))
        d={}
        for i in range (n):
            k=input("Enter Key")
            v=input("Enter Value")
            d[k]=v
        pickle.dump(d,f)
        f.close()

    if ch==2:
        f=open('Student.dat','rb')
        print(pickle.load(f))
    if ch==3:
        f=open('Student.dat','rb')
        key=input("Enter the key to delete its record")
        t=pickle.load(f)

        print(t)
        dic={}
        for i in t.keys():
            if i==key:
                t.popitem()
            print(t)
            
            
                
        
