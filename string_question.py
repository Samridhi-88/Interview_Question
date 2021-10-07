a="samridhi"
a.split()
i=0
x={}
while i<len(a):
    j=0
    count=0
    while j<len(a):
        if a[i]==a[j]:
            count+=1
        j+=1
        x[a[i]]=count
    i+=1
print(x)



a="samridhi"
a.split()
i=0
while i<len(a):
    print(a[i])
    i+=1