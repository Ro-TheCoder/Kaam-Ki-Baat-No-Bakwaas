import pickle
def create():
    f=open("Student.dat",'wb')
    n=int(input("Enter total number of record"))
    d={}
    for i in range (n):
        key=int(input("Enter Roll number"))
        value=input("Enter Name")
        d[key]=value
    pickle.dump(d,f)
    f.close()

def read():
    f=open("Student.dat",'rb')
    print(pickle.load(f))

def deleterec():
    f=open("Student.dat",'rb')
    temp=pickle.load(f)
    f.close()
    rec=int(input("Enter Roll number"))
    del temp [rec]
    t=open("Student.dat",'wb')
    pickle.dump(temp,t)
    f.close()

while True:
    ch=int(input('''Choose one of the program to run
1. Create dictionary
2. Read Dictionary
3. Delete record'''))
    if ch==1:
        create()
    if ch==2:
        read()
    if ch==3:
        deleterec()
            
