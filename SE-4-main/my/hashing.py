rec=[]
N= int(input("Enter number of records : "))
for i in range(N):
    temp=int(input("Enter telephone number : "))
    rec.append(temp)

print(rec)

MAX = int(input("Enter size of hash table : "))
HASH =[-1]*MAX
print(HASH)

def hash(value):
    key = value % MAX
    return key


def insert():
    for i in rec:
        key = hash(i)
        HASH[key]=i


def display():
    for i in range(MAX):
        print(i," ", HASH[i])

insert()
print(HASH)
display()

def search(value):
    for i in range(MAX):
        if HASH[i]== value:
            print(f"Element found with key = {i}")
            break
    else:
        print("Element no found!")

search(10)
search(2)