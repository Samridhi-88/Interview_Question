def my_fun():
    cust=int(input("enter the how many cust"))
    i=0
    list=[]
    emp=[]
    c=0
    while i<cust:
        d_time=0
        order=int(input("enter the how many orderd"))
        prep=int(input("enter the preparing time"))
        d_time=prep+order
        emp.append(d_time)
        list.append(i+1)
        if emp[i] in emp:
            c+=1
        i+=1
    if c>1:
        j=0
        while j<len(emp):
            k=0
            while k<len(emp):
                if emp[j]<emp[k]:
                    emp[j],emp[k]=emp[k],emp[j]
                    list[j],list[k]=list[k],list[j]
                else:
                    emp[j],emp[k]=emp[j],emp[k]
                    list[j],list[k]=list[j],list[k]
                k+=1
            j+=1
        print(emp)
        print(list)
    
my_fun()
