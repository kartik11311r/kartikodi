def Sorting():
    l1=input("Enetr the numbers").split()
    l1=[int(i)for i in l1]
    l1=list(set(l1))
    l1.sort()
    print(l1)
Sorting()