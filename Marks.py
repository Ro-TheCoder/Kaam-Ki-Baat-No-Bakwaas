import pickle
while True:
    ch=int(input('''1. Create Dictionary
2. Read data of students whose sum of marks are greater than 300'''))
    if ch==1:
        f=open("Marks.dat",'wb')

        num=int(input('Enter total number of students'))
        d={}
        for i in range (num):
            name=input("Enter name")
            Pmarks=int(input("Enter physics marks"))
            Cmarks=int(input("Enter chem marks"))
            Mmarks=int(input("Enter maths marks"))
            Emarks=int(input("Enter eng marks"))
            d[name]=[Pmarks,Cmarks,Mmarks,Emarks]
        pickle.dump(d,f)
        f.close()
    if ch==2:
        f=open("Marks.dat",'rb')
        temp=pickle.load(f)
        for k in temp.keys():
            s=sum(temp[k])
            if s>300:
                   print(k,s)
            
    
        
    
    
       
