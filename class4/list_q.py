lst=[[23,45,76],[45,3,12],[3,5,20]]

lst1=[]
for i in lst:
    lst2=i
   
    lst1.append(lst2[0])
    lst1.append(lst2[-1])

    
print(lst1)
