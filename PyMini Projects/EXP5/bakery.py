customers={}

def add(id):
    name=input("Enter name:")
    phone=int(input("Enter phone number:"))
    email=input("Enter email:")
    customers[id]= {"Name":name,"Phone":phone,"Email":email}
    print("Customer "+name+" added\n")

def view():
    for x,y in customers.items():
        print(x,y)

def update(id):
    if id in customers:
        key = input("Enter key for updation:")
        if key=="Phone":
            value = int(input("Enter updated value:"))
        else:
            value = input("Enter updated value:")
        customers[id][key]=value
        print("Updated:  ",customers.get(id))
    else:
        print("Customer does not exist.\n")

def search(id):
    if id in customers:
        print("Found Customer "+id)
        print(customers.get(id))
    else:
        print("Customer does not exist.\n")

def delemp(id):
    if id in customers:
        del customers[id]
        print("Deleted successfully")
    else:
        print("Customer does not exist.\n")

if __name__=="__main__":
    print("CUSTOMER DATABASE")
    ch=0
    while ch!=6:
        print("1.View Customer Data\t\t2.Add Customer\n3.Update Customer data\t\t4.Search Customer\n5.Delete Customer\t\t6.Exit\n")
        ch = int(input("Enter choice:"))
        if ch==1:
            view()
        elif ch==2:
            id=input("Enter Customer ID:")
            add(id)
        elif ch==3:
            id=input("Enter Customer ID:")
            update(id)
        elif ch==4:
            id=input("Enter Customer ID:")
            search(id)
        elif ch==5:
            id=input("Enter Customer ID:")
            delemp(id)
        elif ch==6:
            break