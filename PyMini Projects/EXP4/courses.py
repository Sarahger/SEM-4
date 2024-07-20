class Course:
    def __init__(self,title,inst,dur):
        self.title = title
        self.inst = inst
        self.dur = dur
        self.student = ['Raj','Seema','Kabir']
        self.materials = {'Books':'Improtance of Programming','Questions':"PYQ's"}

    def enroll(self,name):
        self.student.append(name)
        print(f"Successfully enrolled student {name} in course {self.title} for the duration of {self.dur} months.\n")

    def progress(self):
        print(f"\nStudents enrolled in {self.title} course:")
        for i in self.student:
            print(i)
        print(f"\nMaterial available in {self.title} course:")
        for x in self.materials:
            print(x)

    def certificate(self,name):
        print("---------------------------------------------------------------------")
        print("*********************************************************************\n")
        print("                            CERTIFICATE                             \n")
        print(f"         Congratulations Mr/Miss {name} !\n        You have successfully completed the course named {self.title}.\n")
        print("*********************************************************************")
        print("---------------------------------------------------------------------")
    
    def material(self, name, link):
        self.materials[name] = link

    def display(self):
        print(f"Course information:\nInstructor : {self.inst}\nCourse duration : {self.dur}")

if __name__=="__main__":
    print("Online Course Platform")
    c = Course('C','Piyush',6)
    java = Course('Java','Swati',9)
    html = Course('HTML','Saurabh',2)
    py = Course('Python','Prachi',6)
    login = 0
    while login!=3:
        print("Login as:\n1.Instructor\t\t2.Student\n3.Exit")
        login = int(input())
        if login==1:
            ch=0
            while ch!=5:
                print("\nCourses Available:\n1.C Language\t\t2.Java\n3.HTML\t\t4.Python\n5.Exit\n")
                ch = int(input("Enter course number for more information:"))
                if ch == 1:
                    a = int(input("Add Material:\n1.Yes\t\t2.No\n"))
                    if a==1:
                        mat = input("Enter Material:")
                        link = input("Enter link:")
                        c.material(mat,link)
                    c.progress()
                elif ch == 2:
                    a = int(input("Add Material:\n1.Yes\t\t2.No\n"))
                    if a==1:
                        mat = input("Enter Material:")
                        link = input("Enter link:")
                        java.material(mat,link)
                    java.progress()
                elif ch == 3:
                    a = int(input("Add Material:\n1.Yes\t\t2.No\n"))
                    if a==1:
                        mat = input("Enter Material:")
                        link = input("Enter link:")
                        html.material(mat,link)
                    html.progress()
                elif ch == 4:
                    a = int(input("Add Material:\n1.Yes\t\t2.No\n"))
                    if a==1:
                        mat = input("Enter Material:")
                        link = input("Enter link:")
                        py.material(mat,link)
                    py.progress()
                elif ch==5:
                    break
        elif login==2:
            ch=0
            while ch!=5:
                print("Courses Available:\n1.C Language\t\t2.Java\n3.HTML\t\t4.Python\n5.Certificates\t\t6.Exit\n")
                ch = int(input("Enter course number for more information:"))
                if ch == 1:
                    c.display()
                    x = int(input("Enroll student :\n1.Yes\t\t2.No\n"))
                    if x==1:
                        name = input("Enter student name:")
                        c.enroll(name)
                        y = input("View Progress:\n1.Yes\t\t2.No\n")
                        if y==1:
                            c.progress()
                elif ch==2:
                    java.display()
                    x = int(input("Enroll student :\n1.Yes\t\t2.No\n"))
                    if x==1:
                        name = input("Enter student name:")
                        java.enroll(name)
                        y = input("View Progress:\n1.Yes\t\t2.No\n")
                        if y==1:
                            java.progress()
                elif ch==3:
                    html.display()
                    x = int(input("Enroll student :\n1.Yes\t\t2.No\n"))
                    if x==1:
                        name = input("Enter student name:")
                        html.enroll(name)
                        y = input("View Progress:\n1.Yes\t\t2.No\n")
                        if y==1:
                            html.progress()
                elif ch==4:
                    py.display()
                    x = int(input("Enroll student :\n1.Yes\t\t2.No\n"))
                    if x==1:
                        name = input("Enter student name:")
                        py.enroll(name)
                        y = input("View Progress:\n1.Yes\t\t2.No\n")
                        if y==1:
                            py.progress()
                elif ch==5:
                    print("Cretificates:\n1.C\t\t2.Java\n3.HTML\t\t4.Python\n")
                    x = int(input())
                    if x==1:
                        name = input("Enter name:")
                        c.certificate(name)
                    if x==2:
                        name = input("Enter name:")
                        java.certificate(name)
                    if x==3:
                        name = input("Enter name:")
                        html.certificate(name)
                    if x==4:
                        name = input("Enter name:")
                        py.certificate(name)
                elif ch==6:
                    break
            else:
                break