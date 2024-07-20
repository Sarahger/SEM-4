employee={}

def addemp(id):
    name=input("Enter name:")
    age=int(input("Enter age:"))
    dept=input("Enter department:")
    sal=int(input("Enter salary:"))
    employee[id]= {"Name":name,"Age":age,"Department":dept,"Salary":sal}
    print("Employee "+id+" added\n")

def view():
    for x,y in employee.items():
        print(x,y)

def update(id):
    if id in employee:
        key = input("Enter key for updation:")
        if key=="Age" or key=="Salary":
            value = int(input("Enter updated value:"))
        else:
            value = input("Enter updated value:")
        employee[id][key]=value
        print("Updated:  ",employee.get(id))
    else:
        print("Invalid ID. Employee does not exist.\n")

def search(id):
    if id in employee:
        print("Found Employee "+id)
        print(employee.get(id))
    else:
        print("Employee does not exist.\n")

def delemp(id):
    if id in employee:
        del employee[id]
        print("Deleted successfully")
    else:
        print("Employee does not exist.\n")

def avgsal():
    id=1
    sum=0
    for id in employee:
        sum += employee[id]['Salary']
    avg = sum/len(employee)
    print("Average Salary = ",avg)

if __name__=="__main__":
    print("Employee Management System")
    ch=0
    while ch!=7:
        print("1.View Employee Data\t\t2.Add Employee\n3.Update Employee data\t\t4.Search Employee\n5.Delete Employee\t\t6.Average Salary\n7.Exit\n")
        ch = int(input("Enter choice:"))
        if ch==1:
            view()
        elif ch==2:
            id=input("Enter ID:")
            addemp(id)
        elif ch==3:
            id=input("Enter ID:")
            update(id)
        elif ch==4:
            id=input("Enter ID:")
            search(id)
        elif ch==5:
            id=input("Enter ID:")
            delemp(id)
        elif ch==6:
            avgsal()
        elif ch==7:
            break
    