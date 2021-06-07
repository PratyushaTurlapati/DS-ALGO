i=1
flag=0
a=[]
n=int(input("no.of elements:"))
s=int(input("search element:"))
for i in range(0,n):
    e=int(input())
    a.append(e)
for i in a:
    if(a[i]==s):
        flag=i+1
        break
    else:
        flag=0
    i=i+1
if(flag!=0):
    print("found at "+str(i))
else:
    print("not found")
