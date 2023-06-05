print("Hello world!")

A = {"k"}
B = {"j"}

def create():
  n = int(input("Enter the number of elements in your set:  "))
  for i in range (0,n):
    a = int(input("Enter elements:"))
    A.add(a)
  A.remove("k")
  print("Set A created successfully")
  print(A)

def create2():
  n = int(input("Enter the number of elements in your set:  "))
  for i in range (0,n):
    a = int(input("Enter elements:"))
    A.add(a)
  A.remove("j")
  print("Set B created successfully")
  print(B)
 
def addd():
  n = int(input("Enter the number of elements you want to add "))
  for i in range (0,n):
    a = int(input("Enter elements:"))
    A.add(a)

def delete():
  n = int(input("Enter the number of elements you want to remove "))
  for i in range (0,n):
    a = int(input("Enter elements:"))
    A.remove(a)

def contain(A):
  n = int(input("Enter the element you want to check for: "))
  if (n in A):
    print(n," is present in the set")
  else:
    print(n, "isn't present in the set")

def length(A):
  print("The length of the set is",len(A))

def intersection(A,B):
  C = A.intersection(B)
  print("The intersection of the two sets is ",C)

def difference(A,B):
  D = A.difference(B)
  print("The elements that exist only in set A and not in set B are: ",D)

def subset(A,B):
  S = A.issubset(B)
  if (S == True):
    print("A is a subset of B")
def union(A,B):
  P = A.union(B)
  print(P)


print("============Main Menu==============")

print("1. Create Set A")
print("2. Create Set B")
print("3. Add elements to Set")
print("4. Remove elements from Set")
print("5. Contain")
print("6. Length of set")
print("7. Intersection of two sets")
print("8. Difference of two sets")
print("9. Union of two sets")

chhoice = int(input("Enter your choice from the menu"));

match chhoice:
  case 1:
    create()
  case 2:
    create2()
  case 3:
    addd()
  case 4:
    delete()
  case 5:
    contain(A)
  case 6:
    length(A,B)
  case 7:
    intersection(A,B)
  case 8:
    difference(A,B)
  case 9:
    subset()
  case 10:
    union()
  case _:
    print("Please enter correct choice: ")
