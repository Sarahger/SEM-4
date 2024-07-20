def grade(total):
    #assuming each subject is 100 marks
    perc = (total/500) *100
    print("Total Percentage = ",perc)
    if perc>90 and perc<100:
        print("Grade = A")
    elif perc>80 and perc<90:
        print("Grade = B")
    elif perc>70 and perc<80:
        print("Grade = C")
    elif perc>60 and perc<70:
        print("Grade = D")
    if perc>50 and perc<60:
        print("Grade = E")

if __name__=="__main__":
    print("Enter marks :")
    maths=int(input("Maths:"))
    phy=int(input("Physics:"))
    chem=int(input("Chemistry:"))
    eng=int(input("English:"))
    bio=int(input("Biology:"))
    total = maths+phy+chem+eng+bio
    print("Total marks scored = ",total)
    grade(total)