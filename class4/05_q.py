# wap which will create a list all elemnt devisiable by 3 between 4and 25\\
# lst=[]
# for i in range(4,26):
#     if((i%3)==0):
#         lst.append(i)

# print(lst)

# this code do in single line

lst1=[i for i in range(4,26) if i%3==0]
print(lst1)

