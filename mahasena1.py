def mahasena():
    soldier=int(input("enter the soldiers ="))
    list1=[]
    i=0
    e_c=0
    o_c=0
    while i<soldier: 
        weapens=int(input("enter the number of weapens ="))
        list1.append(weapens)
        if list1[i]%2==0:
            e_c+=1
        else:
            o_c+=1
        i+=1
    if e_c<o_c:
        print("not ready")
    elif e_c>o_c:
        print("ready for battle")
    else:
        print("not ready")
mahasena()