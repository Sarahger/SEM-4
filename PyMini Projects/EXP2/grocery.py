products={}

def addemp(prod):
    price=int(input("Enter price:"))
    month=input("Enter month of sale:")
    qnt=int(input("Enter quantity:"))
    products[prod]= {"Price":price,"Month":month,"Quantity":qnt}
    print("Product "+prod+" added\n")

def view():
    for x,y in products.items():
        print(x,y)

def update(prod):
    if prod in products:
        key = input("Enter key for updation:")
        if key=="Price" or key=="Quantity":
            value = int(input("Enter updated value:"))
        else:
            value = input("Enter updated value:")
        products[prod][key]=value
        print("Updated:  ",products.get(prod))
    else:
        print("Product does not exist.\n")

def search(prod):
    if prod in products:
        print("Found product "+prod)
        print(products.get(prod))
    else:
        print("Product does not exist.\n")

def delemp(prod):
    if prod in products:
        del products[prod]
        print("Deleted successfully")
    else:
        print("Product does not exist.\n")

def sales():
    for prod in products:
        print("Product\t\tSold")
        print(prod,"\t\t\t",products[prod]['Month'])

if __name__=="__main__":
    print("Grocery Store Management System")
    ch=0
    while ch!=7:
        print("1.View Groceries\t\t2.Add Product\n3.Update Product\t\t4.Search Product\n5.Delete Product\t\t6.Get Sales\n7.Exit\n")
        ch = int(input("Enter choice:"))
        if ch==1:
            view()
        elif ch==2:
            id=input("Enter Product:")
            addemp(id)
        elif ch==3:
            id=input("Enter Product:")
            update(id)
        elif ch==4:
            id=input("Enter Product:")
            search(id)
        elif ch==5:
            id=input("Enter Product:")
            delemp(id)
        elif ch==6:
            sales()
        elif ch==7:
            break