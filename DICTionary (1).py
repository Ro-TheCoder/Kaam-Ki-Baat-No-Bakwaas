import pickle
def create(n,num):
    n=input("Enter name of the file")
    n=n+".dat"
    f=open(n,'wb')
    num=int(input("Enter Total number of records"))
    d={}
    for i in range (n):
        key=input("Enter Key")
        value=input("Enter Value")
        d[key]=value
    pickle.dump(d,f)
    f.close()

def read(name):
    name=name+".dat"
    f=open(name,'rb')
    pickle.load(f)

def search(name):
    k=input("Enter the key to find")
    name=name+".dat"
    f=open(name,rb)
    t=pickle.load(f)
    z=open("Temp.dat",'wb')
    try:
        for i in t:
            if i==k:
                t.remove(k)
            pickle.dump(t,z)
    except EOFError:
            break

while True:
    ch=int(input('''Choose one of the follwoing programs
1.Create dictionary
2.Read Dictionary
3.Delete record'''))
    if ch==1:
        create()
    if ch==2:
        read()
    if ch==3:
        search()
                    
        
    
