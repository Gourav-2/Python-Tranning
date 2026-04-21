lst1=[i for i in range(4,26) if i%3==0]
print(lst1)

lst2=[i**2 for i in lst1 if i%2==0]
lst3=[i**2 for i in lst1 if i%2!=0]

print(lst2)
print(lst3)