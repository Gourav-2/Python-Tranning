# --------------------------------CRUD OPERATION---------------

l=["gourav","harsh",27,28,"nishant"]#creation of list 
print(l)

for i in range(0,len(l)): #access each element of list
    print(l[i], end=" ")

lst=[]
lst=list()               #both create empty list

#PROPERTY OF LIST 
# 1. LIST IS MUTABLE
# 2. DYNAMIC SIZE 
# 3. CONTAIN MIX DATA TYPE 
# 4. LIST KO CREATE KARNE KE LIAA [] KA USE KARTE HAI

l[0]="Gourav"
print(l)

#FOR LOOP IN LIST 
for i in l:
    print(i)


list3=[3,5,7,8,12,10,2,5,8]        #list slicing 
print(list3[-3: :-2])
print(list3[-3:-8:-4])







