# # # # # # # # # # # # # # """# """
# # # # # # # # # # # # # # # class Product:
# # # # # # # # # # # # # # #     def __init__(self):
# # # # # # # # # # # # # # #         self.productno=0
# # # # # # # # # # # # # # #         self.productname=0
# # # # # # # # # # # # # # #         self.cost=0
# # # # # # # # # # # # # # #         self.quantity=0
# # # # # # # # # # # # # # #         self.totalamount=0
    
# # # # # # # # # # # # # # #     def input(self):
# # # # # # # # # # # # # # #         self.productno=int(input("Enetr the product no.:"))
# # # # # # # # # # # # # # #         self.productname=input("Enetr product name:")
# # # # # # # # # # # # # # #         self.cost=int(input("Enetr the cost:"))
# # # # # # # # # # # # # # #         self.quantity=int(input("Enetr the quantity of a product"))

# # # # # # # # # # # # # # #     def calculate(self):
# # # # # # # # # # # # # # #         self.totalamount=self.cost*self.quantity
    
# # # # # # # # # # # # # # #     def display(self):
# # # # # # # # # # # # # # #         print("Product no.",self.productno)
# # # # # # # # # # # # # # #         print("product name",self.productname)
# # # # # # # # # # # # # # #         print("cost",self.cost)
# # # # # # # # # # # # # # #         print("quantity",self.quantity)
# # # # # # # # # # # # # # #         print("total amount",self.totalamount)




# # # # # # # # # # # # # # # products=[]
# # # # # # # # # # # # # # # for i in range(5):
# # # # # # # # # # # # # # #     print("Enter  details of 5 product")
# # # # # # # # # # # # # # #     p=Product()
# # # # # # # # # # # # # # #     p.input()
# # # # # # # # # # # # # # #     p.calculate()
# # # # # # # # # # # # # # #     products.append(p)

# # # # # # # # # # # # # # # costly=products[0]
# # # # # # # # # # # # # # # for p in products:
# # # # # # # # # # # # # # #     if p.totalamount > costly.totalamount:
# # # # # # # # # # # # # # #         costly=p

# # # # # # # # # # # # # # # print("product with max cost:")
# # # # # # # # # # # # # # # costly.display()


# # # # # # # # # # # # # # # import threading

# # # # # # # # # # # # # # # lock = threading.Lock()
# # # # # # # # # # # # # # # counter = 0

# # # # # # # # # # # # # # # def increment():
# # # # # # # # # # # # # # #     global counter
# # # # # # # # # # # # # # #     for _ in range(100000):
# # # # # # # # # # # # # # #         with lock:
# # # # # # # # # # # # # # #             counter += 1

# # # # # # # # # # # # # # # t1 = threading.Thread(target=increment)
# # # # # # # # # # # # # # # t2 = threading.Thread(target=increment)

# # # # # # # # # # # # # # # t1.start()
# # # # # # # # # # # # # # # t2.start()
# # # # # # # # # # # # # # # t1.join()
# # # # # # # # # # # # # # # t2.join()

# # # # # # # # # # # # # # # print("Final Counter:", counter)


# # # # # # # # # # # # # # # from functools import reduce

# # # # # # # # # # # # # # # # Calculate the product of all numbers
# # # # # # # # # # # # # # # numbers = [1, 2, 3, 4]
# # # # # # # # # # # # # # # result = reduce(lambda x, y: x + y, numbers)
# # # # # # # # # # # # # # # print(result)  
# # # # # # # # # # # # # # # """
# # # # # # # # # # # # # # # """"
# # # # # # # # # # # # # # # # Input: Number of terms
# # # # # # # # # # # # # # # n = int(input("Enter the number of Fibonacci terms: "))

# # # # # # # # # # # # # # # # Initial two Fibonacci numbers
# # # # # # # # # # # # # # # a, b = 0, 1
# # # # # # # # # # # # # # # count = 0

# # # # # # # # # # # # # # # print("Fibonacci Series:")
# # # # # # # # # # # # # # # while count < n:
# # # # # # # # # # # # # # #     print(a, end=' ')
# # # # # # # # # # # # # # #     a, b = b, a + b
# # # # # # # # # # # # # # #     count += 1
# # # # # # # # # # # # # # # else:
# # # # # # # # # # # # # # #     print("\nFibonacci series generation completed.")



# # # # # # # # # n=int(input("Enter  no of terms"))
# # # # # # # # # a,b=0,1
# # # # # # # # # count=0
# # # # # # # # # while count < n:
# # # # # # # # #     print(a,end=' ')
# # # # # # # # #     a,b=b,a+b
# # # # # # # # #     count+=1

# # # # # # # # dict={}
# # # # # # # # s=input("Enter a string:")
# # # # # # # # for i in s:
# # # # # # # #     if i in dict:
# # # # # # # #         dict[i] +=1
# # # # # # # #     else:
# # # # # # # #         dict[i]=1
# # # # # # # # for i in dict:
# # # # # # # #     print(i,"-",dict[i])

# # # # # # # global_var=10
# # # # # # # import config
# # # # # # # print("Before change",config.global_var)
# # # # # # # config.global_var=24
# # # # # # # print("After change",config.global_var)


# # # # # # global_var=10
# # # # # # # main.py
# # # # # # import config

# # # # # # # Accessing the global variable from config module
# # # # # # print("Before change:", config.global_var)

# # # # # # # Modifying the global variable
# # # # # # config.global_var = 42

# # # # # # # Confirming the change
# # # # # # print("After change:", config.global_var)

# # # # # try:

# # # # #     a=2
# # # # #     b=0
# # # # #     result=a/b
# # # # #     try:
# # # # #         x='5'
# # # # #         y=2
# # # # #         print(x+y)
# # # # #     except TypeError:
# # # # #         print("type error in inner block")
    
# # # # # except ZeroDivisionError:
# # # # #     print("zeroDivisionError in outer block")

# # # # #single inheritance
# # # # class Animal:
# # # #     def speak(self):
# # # #         print("Animal speaks")

# # # # class Dog:
# # # #     def bark(self):
# # # #         print("dog bark")
# # # # d=Dog()
# # # # d.speak()
# # # # d.bark()



# # # s=input("Enter he string:")
# # # x=int(input("Enter number"))
# # # temp=""
# # # for i in s:
# # #     temp += i*x
# # # print(temp)


# # def sortint():
# #     l1=("Enter the number:").split()
# #     l1=[int(i) for i in l1]
# #     l1=list(set(l1))
# #     l1.sort
# #     print(l1)
# dict={}
# s=input("Enter string")
# for i in s:
#     if i in dict:
#         dict[i] +=1
#     else:
#         dict[i]=1
# for i in dict:
#     print(i,"-",dict[i])




a=input("Enter string:")
prev='a'
temp=''
for i in a:
    if i.isalpha():
        temp+=i
        prev=i
    else:
        cr=chr(ord(prev)+int(i))
        temp=cr
print(temp)