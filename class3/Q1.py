lst=[5,3,2,1,4,8]
ans_lst1=[]
sum=0
for i in range(len(lst)):
    sum=sum+lst[i]

for i in lst:
    ans_lst1.append(sum-i)

print(ans_lst1)
    


