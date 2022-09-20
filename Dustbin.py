import pickle
f=open("Bin.dat",'wb')
l1=[10,20,3,40]
pickle.dump(l1,f)
f.close()
