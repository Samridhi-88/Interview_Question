list1=[1,0,0,1,1,0,1,1]
i=0
s=0
b=0
a=len(list1)-1
while i<len(list1):
    print(list1[a])
    d=list1[a]
    c=(d*2)**b
    s=s+c
    a=a-1
    b=b+1
    i=i+1
print(s)