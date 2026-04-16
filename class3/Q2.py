lst=[[1,3,5,6],[3,4,5],[3,5,7],[10,20,30]]
# sort trick 
lst_ans=[]
# for i in range(len(lst)):              
#     lst_ans.append(sum(lst[i]))
# long trock
for i in range(len(lst)):
    temp=0
    for j in lst[i]:
        temp+=j
    lst_ans.append(temp)

print(lst_ans)
    



