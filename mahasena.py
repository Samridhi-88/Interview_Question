def function():    
    soldier=int(input("enter the soldiers ="))
    list1=[]
    i=1
    while i<=soldier:
        weapens=int(input("enter the number of weapens ="))
        list1.append(weapens)
        i+=1
    index=0
    e_c=0
    o_c=0
    while index<len(list1):
        if list1[index]%2!=0:
            o_c+=1
        else:
            e_c+=1
        index+=1
    if e_c<o_c:
        print("not ready")
    elif e_c>o_c:
        print("ready for battle")
    elif e_c==o_c:
        print("not ready")
function()