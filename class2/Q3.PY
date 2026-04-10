# WAP THAT TAKE INTEGER INPUT  LIST FROM USER AND IN LIST EVEN NUM ICREADE BY 5 AND ODD NUMBER DECREADEBY 5

lst=eval(input("Enter int list: "))
print(lst)

for i in range(len(lst)) :
    if((lst[i]%2)==0):
        lst[i]=lst[i]+5
    else:
        lst[i]=lst[i]-5

print(lst)
