# selection sort
sort_list = []

def display():
    for i in range(len(sort_list)):
        print(sort_list[i], end=' ')
    print()

def swap(a:int, b:int):
    sort_list[a], sort_list[b] = sort_list[b], sort_list[a]

def selection_sort():
    n = int(input("Enter the number of elements: "))
    for _ in range(n):
        x = int(input("Enter element: "))
        sort_list.append(x)
    print("\nEntered list")
    display()

    for i in range(n):
        min_index = i
        for j in range(i+1,n):
            if sort_list[min_index] > sort_list[j]:
                min_index = j
        
        if min_index != i:
            swap(i, min_index)
    print("\nSorted list")
    display()

if __name__ == '__main__':
    selection_sort()
