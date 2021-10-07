def my_fun():
    people=int(input("enter the how many people"))
    i=0
    customer=[]
    c=0
    while i<people:
        user=int(input("enter the people"))
        order=int(input("enter the how many orderd"))
        prep=int(input("enter theb prepering time"))
        d_time=prep+order
        customer.append(d_time)
        if customer[i] in customer:
            c+=1
        i+=1
    customer.sort()
    if c>1:
        print("delevery time",customer)
    else:
        print(customer)
my_fun()


