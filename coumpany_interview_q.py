country=input("enter your country name")
product_code=input("enter your product code")
weight=float(input("enter your weight in kg"))
carancy=input("enter the curancy")
if country=="UK":
    if weight<5:
        shipping_cost=5
        if product_code[0:3]=="123":
            if carancy=="INR" or carancy=="inr":
                cost_1=shipping_cost*1.2*(1+0.18)
                print(cost_1)
            elif carancy=="US" or carancy=="us":
                cost_1=shipping_cost*1.2*(1+0.18)
                cost=cost_1/80
                print(cost,"us dollor")
            else:
                print("your carency is not matching")
        elif product_code[0:3]=="234":
            if carancy=="INR" or carancy=="inr":
                cost_1=shipping_cost*1.5*(1+0.18)
                print(cost_1)
            elif carancy=="US" or carancy=="us":
                cost_1=shipping_cost*1.2*(1+0.18)
                cost=cost_1/80
                print(cost,"us dollor")
            else:
                print("your carency is not matching ")
        else:
            cost_1=shipping_cost*(1+0.18)
            print(cost_1)
    elif weight>=5:
        shipping_cost=15
        if product_code[0:3]=="123":
            if carancy=="INR" or carancy=="inr":
                cost_2=shipping_cost*1.2*(1+0.18)
                print(cost_2)
            elif carancy=="US" or carancy=="us":
                cost_2=shipping_cost*1.2*(1+0.18)
                cost=cost_2/80
                print(cost,"dollor")
            else:
                print("your carency is not matching")
        elif product_code[0:3]=="234":
            if carancy=="INR" or carancy=="inr": 
                cost_2=shipping_cost*1.5*(1+0.18)
                print(cost_2)
            elif carancy=="US" or carancy=="us":
                cost_2=shipping_cost*1.5*(1+0.18)
                cost=cost_2/80
                print(cost,"dollor")
            else:
                print("your carency is not matching")
        else:
            cost_2=shipping_cost*(1+0.18)
            print(cost_2)
elif country=="US":
    if weight<10:
        shipping_cost=5
        if product_code[0:3]=="123":
            if carancy=="INR" or carancy=="inr":
                cost_3=shipping_cost*1.2*(1+0.18)
                print(cost_3)
            elif carancy=="US" or carancy=="us":
                cost_3=shipping_cost*1.2*(1+0.18)
                cost=cost_3/80
                print(cost,"dollor")
            else:
                print("your carency is not matching")
        elif  product_code[0:3]=="234":
            if carancy=="INR" or carancy=="inr":
                cost_3=shipping_cost*1.5*(1+0.18)
                print(cost_3)
            elif carancy=="US" or carancy=="us":
                cost_3=shipping_cost*1.5*(1+0.18)
                cost=cost_3/80
                print(cost,"dollor")
            else:
                print("your carency is not matching")
        else:
            cost_3=shipping_cost*(1+0.18)
            print(cost_3)
    elif weight>=10:
        shipping_cost=15
        if product_code[0:3]=="123":
            if carancy=="INR" or carancy=="inr":
                cost_4=shipping_cost*1.2*(1+0.18)
                print(cost_4)
            elif carancy=="US" or carancy=="us":
                cost_4=shipping_cost*1.2*(1+0.18)
                cost=cost_4/80
                print(cost,"dollor")
            else:
                print("your carency is not matching")
        elif product_code[0:3]=="234":
            if carancy=="INR" or carancy=="inr":
                cost_4=shipping_cost*1.5*(1+0.18)
                print(cost_4)
            elif carancy=="US" or carancy=="us":
                cost_4=shipping_cost*1.5*(1+0.18)
                cost=cost_4/80
                print(cost,"dollor")
        else:
            cost_4=shipping_cost*(1+0.18)
            print(cost_4)
else:
    print("Not applicable")