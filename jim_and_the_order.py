def my_function():
    people=int(input("enter the how many people"))
    i=0
    list1=[]
    customer=[]
    count=0
    while i<people:
        user=int(input("enter the people"))
        order=int(input("enter the how many orderd"))
        prep=int(input("enter theb prepering time"))
        d_time=prep+order
        customer.append(d_time)
        list1.append(user)
        if customer[i] in customer:
            count+=1
        i+=1
    if count>1:
        x=0
        while x<len(customer):
            y=0        
            while y<len(customer):
                if customer[x]<customer[y]:
                    customer[x],customer[y]=customer[y],customer[x]
                    list1[x],list1[y]=list1[y],list1[x]
                y+=1
            x+=1
        print(customer)
        print(list1)
    dict={}
    index=0
    while index<len(customer):     
        dict[list1[index]]=customer[index]
        index+=1
    print(dict)
my_function()
