lst=[2,4,6,8,3,5,8,9]
a=len(lst)//2
lst1=lst[:a]
lst2=lst[a:]
print(sum(lst1),end=" ")
print(sum(lst2))
