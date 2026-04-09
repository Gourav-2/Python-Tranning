# #creating function 
# # WAR which will take a number from user if num is even it calcutale even factorial 
# # and if num is odd then calculate odd factorial

# def factcal(a):
#     fact=1
#     if((a%2)==0):
#         print("Your number is Even")
#         for i in range(2,a+1,2):
#             fact=fact*i
#         print(fact)
#     else:
#         print("Your number is Odd")
#         for i in range(1,a+1,2):
#             fact=fact*i
#         print(fact)

# n=int(input("Enter num: "))
# factcal(n)


# #Same q using two function

# def evenfact(a):#this function calculate even function
#     fact=1
#     for i in range(2,a+1,2):
#             fact=fact*i
#     print("Your even factorial:", fact)


# def oddfact(b):
#     fact=1
#     for i in range(1,b+1,2):
#             fact=fact*i
#     print("Your odd factorial:", fact)

# num=int(input("Enter a number: "))
# if((num%2)==0):
#     evenfact(num)
# else:
#     oddfact(num)

# __________________________pass key word__________________________________

# jab function ki body na ho to pass keyword ka use karte hai jisse function error nahi deta hai 

def sum(a):
    pass

