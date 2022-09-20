for a in range(99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999):
    print(''' Enter the number to run the program
1. Count the number of vowels in the list
2.Display the sum of all the elements in the list
3. Get an element from the user and display its location in the list
4. To get an element from the user & display its number of occurences in the list''')
    choice=int(input("Enter Number"))
    if choice ==1:
        l1=['an','apple','a','day','keeps','the','doctor','away']
        l2=['a','e','i','o','u']
        count=0
        for n in l2:
            for i in l1:
                i.lower()
                for j in i:
                    if j==n:
                        count+=1
        print(count)
    elif choice ==2:
        l1=['an','apple','a','day','keeps','the','doctor','away']
        print(len(l1))
    elif choice ==3:
        l1=['an','apple','a','day','keeps','the','doctor','away']
        string=input('Enter the element')
        for i in l1:
            if i==string:
                print(l1.index(i))
    elif choice==4:
        l1=['an','apple','a','day','keeps','the','doctor','away','apple']
        string=input('Enter the element')
        count=0
        for i in l1:
            if string==i:
                count+=1
        print(count)
        
                
            
                
                
                
