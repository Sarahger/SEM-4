# insertion sort
sort_list = []

def display():
    for i in range(len(sort_list)):
        print(sort_list[i], end=' ')
    print()

def insertion_sort():
    n = int(input("Enter the number of elements: "))
    for _ in range(n):
        x = int(input("Enter element: "))
        sort_list.append(x)
    print("\nEntered list")
    display()

    for i in range(1,n):
        j = i - 1
        key = sort_list[i]
        while j>=0 and sort_list[j] > key:
            sort_list[j+1] = sort_list[j]
            j -= 1
        sort_list[j+1] = key

    print("\nSorted list")
    display()

if __name__ == '__main__':
    insertion_sort()