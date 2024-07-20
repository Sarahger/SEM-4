
def even(list):
    even=[]
    for n in list:
        print (n)
        if((int(n)%2)==0):
            even.append(n)
    print("Even list: ",even)

def odd(list):
    odd=[]
    for n in list:
        if((int(n)%2)!=0):
            odd.append(n)
    print("Odd list: ",odd)

if __name__=="__main__":
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original List: ",lst)
    even(lst)
    odd(lst)