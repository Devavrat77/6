ht=[0]*10
def hashs( key, max):
    return key%max
def probing(key,max):
    pos=hashs(key,max)
    if (ht[pos]==0):
        ht[pos]=key
    else:
        for i in range(pos,10):
            if(ht[i]==0):
                ht[i]=key
                break
def display():
    print("Telephone Records")
    for i in range(10):
        print("Index",i,":",ht[i])
def se(key):
    for i in range(10):
        if (ht[i]==key):
            print("Element Found!!")
            print("At Index",i)
            break
        else:
            print("Please Enter A VALID KEY!!")
ch="y"
while(ch=="y"):
    print("\n\n****MAIN MENUE****\n")
    print("1.Insert")
    print("2.Display")
    print("3.Search")
    c=int(input("Enter the choice :"))
    if(c==1):   
        n=int(input("Enter the no of RECORDS:"))
        m=int(input("Enter the MAX VALUE:"))
        for i in range(n):
            v=int(input("Enter the value:"))
            probing(v,m)
        print("Do you Want to continue:(YES y,NO n)")
        ch=input()
    elif(c==2):
        display()
    elif(c==3):
        K=int(input("Enter the KEY to Search:"))
        se(K)
        
