l1 = set()
l2 = set()
ch='y'
while (ch == "y"):
    print("\n\n****MAIN MENUE****\n")
    print("1.Insert")
    print("2.Union")
    print("3.Intersection")
    print("4.Difference")
    print("5.Subset")
    print("6.Proper Subset")
    
    c = int(input("Enter the choice :"))
    if (c == 1):
        print("Enter the SET data of A:")
        n1 = int(input("Enter the no of elements:"))
        for i in range(n1):
            a1 = input("Enter the elenet:")
            l1.add(a1)
        print("Enter the SET data of B:")
        n1 = input("Enter the no of elements:")
        for i in range(n1):
            a2 = int(input("Enter the elenet:"))
            l2.add(a2)
        print("Elements inserted!!")
        print("Do you Want to continue:(YES y,NO n)")
        ch=input()
    elif(c==2):
        print("UNION IS:",l1.union(l2))
        print("Do you Want to continue:(YES y,NO n)")
        ch=input()
    elif(c==3):
        print("INTERSECTION IS:",l1.intersection(l2))
        print("Do you Want to continue:(YES y,NO n)")
        ch=input()
    elif(c==4):
        print("DIFFERENCE IS:",l1.difference(l2))
        print("Do you Want to continue:(YES y,NO n)")
        ch=input()
    elif(c==5):
        check=l1.issubset(l2)
        if check==True:
            print("IS SUBSET")
        else:
            print("NOT A SUBSET")
        print("Do you Want to continue:(YES y,NO n)")
        ch=input()
    elif(c==6):
        if l1.issubset(l2):
            if (len(l1)==len(l2)):
                print("IS PROPRER SUBSET")
            else:
                print("NOT A PROPRER SUBSET")
        else:
            print("IS PROPRER SUBSET")
        print("Do you Want to continue:(YES y,NO n)")
        ch=input()
        
        
        
 
