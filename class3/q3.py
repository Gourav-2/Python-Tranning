lst=[[3,2,1,8],[50,3,7,9],[2,3,7,8]]
ans=[]
for i in range(len(lst)):
    temp=lst[i].copy()
    if((i%2)==0):#even index
        for j in range(len(temp)) :
            if((temp[j]%2)==0):
                temp[j]=temp[j]-1
        ans.append(temp)
    else:#for odd index
        for j in range(len(temp)):
            if((temp[j]%2)!=0):
                temp[j]=temp[j]+1
        ans.append(temp)
           

print(lst)
print(ans)
        

