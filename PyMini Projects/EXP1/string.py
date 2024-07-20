def reverse(str):
    rev = str[::-1]
    return rev

def palindrome(str):
    rev = reverse(str)
    if(str==rev):
        print("String is Palindrome")
    else:
        print("String is not Palindrome")

if __name__=="__main__":
    string = input("Enter a string:")
    print("Original string:"+string)
    rev = reverse(string)
    print("Reversed String :"+rev)
    palindrome(string) # type: ignore