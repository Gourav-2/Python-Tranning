#wap to ncr program


def fact(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    

n=int(input("enter n: "))
r=int(input("enter r: "))

nfact=fact(n)

rfact=fact(r)
nr=n-r
n_rfact=fact(nr)
lo=(rfact*n_rfact)
ncr=nfact/lo
print(ncr)

