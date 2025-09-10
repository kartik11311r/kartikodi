def perfect(n):
    div=[] #check remainder =0
    for i in range(1,n):
        if n % i == 0:
            div.append(i)
    sum=0
    for i in div:
        sum=sum+i

    if(sum==n):
        print("perfect")
    else:
        print("not perfect")
perfect(5)