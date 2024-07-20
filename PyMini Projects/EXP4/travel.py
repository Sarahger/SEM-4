class Destination:
    def __init__(self,loc) :
        self.loc = loc
        self.attract = ['Waterfalls','Beaches','Wildlife','Mountains']
        self.acti = ['Rafting','Sky Diving','Swimming','Jungle Safari','Rock Climbing','Scuba Diving']
        
    def expense(self,days):
        cost = 5000*days
        travel = 10000
        print("Total Expenses = ",cost+travel)

    def rate(self):
        print(f"\nHow was your Tour to {self.loc}? ")
        stars = int(input("Enter stars out of 5:"))
        s = '*'
        for i in (1,stars):
            i+=1
        print(s*i)
        print("Thank You!")

    def display(self):
        print(f"\nTravel Destination : {self.loc}")
        print(f"Tourist attractions : {self.attract}")
        print(f"Activities : {self.acti}")

if __name__=="__main__":
    print("TOURS AND TRAVELLS")
    h = Destination('Hawaii')
    u = Destination('USA')
    m = Destination('Maldeives')
    s = Destination('Singapore')
    e = Destination('Europe')
    ch = int(input("Enter Destination:\n1.Hawaii\t\t2.USA\n3.Maldeives\t\t4.Singapore\n5.Europe\n"))
    if ch ==1:
        h.display()
        day = int(input("\nHow many days:"))
        h.expense(day)
        x = int(input("Would you like to rate us?\n1.Yes\t\t2.No\n"))
        if x == 1:
            h.rate()
    elif ch ==2:
        u.display()
        day = int(input("How many days:"))
        u.expense(day)
        x = int(input("Would you like to rate us?\n1.Yes\t\t2.No\n"))
        if x == 1:
            u.rate()
    elif ch ==3:
        m.display()
        day = int(input("How many days:"))
        m.expense(day)
        x = int(input("Would you like to rate us?\n1.Yes\t\t2.No\n"))
        if x == 1:
            m.rate()
    if ch ==4:
        s.display()
        day = int(input("How many days:"))
        s.expense(day)
        x = int(input("Would you like to rate us?\n1.Yes\t\t2.No\n"))
        if x == 1:
            s.rate()
    if ch ==5:
        e.display()
        day = int(input("How many days:"))
        e.expense(day)
        x = int(input("Would you like to rate us?\n1.Yes\t\t2.No\n"))
        if x == 1:
            e.rate()