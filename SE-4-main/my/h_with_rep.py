rec=[]
N= int(input("Enter number of records : "))
for i in range(N):
    temp=int(input("Enter telephone number : "))
    rec.append(temp)

MAX = int(input("Enter size of hash table : "))
HASH =[-1]*MAX

def hash(value):
    key = value % MAX
    return key

def lin_prob(i):
        key = hash(i)
        for t in range(1,MAX):
            if HASH[key]==-1:
                HASH[key]=i
                break
            else:
                key = hash(i+t) 

def insert():
    for i in rec:
        key = hash(i)
        for t in range(1,MAX):
            if HASH[key]==-1:
                HASH[key]=i
                break
            elif hash(HASH[key]) == key:
                key = hash(i+t)
            elif hash(HASH[key]) != key:
                lin_prob(HASH[key])
                HASH[key] = i
                break
            else:
                key = hash(i+t)
            


def display():
    for i in range(MAX):
        print(i," ", HASH[i])

insert()
display()
