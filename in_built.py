def lengt(list):
    print(len(list))



name = ["irfan","ifan","iran","ianf","fani"]

branch = ["cse", "it", "electrical", "mechanical", "biochem","civil"]


lengt(name)

lengt(branch)

def print_list(list):
    for item in list:
        print(item, end=" ")


print_list(name)

#function for factorial printing 

def fact(n):
    facto= 1
    for i in range(1,n+1):
        facto*=i
    print(facto)

    
fact(4)


#function for converting usd to inr

def usd_converter(usd):
    inr = usd * 83
    print("the inr for the usd given is :",inr)
    return inr


usd_converter(100)


#recursion

def show(n):
    if (n==0): 
        return
    print(n)
    show(n-1)

show(5)
