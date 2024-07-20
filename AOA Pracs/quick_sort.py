# quick sort
def display(sort_list):
    print(','.join(map(str,sort_list)))

def partition(sort_list, low, high):
    pivot = sort_list[high]
    i = low - 1
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i+1], sort_list[high] = sort_list[high], sort_list[i+1]
    print (i+1)
    return i + 1

def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi - 1)
        quick_sort(sort_list, pi + 1, high)

if __name__ == '__main__':
    n = int(input("Enter the number of elements: "))
    sort_list = [int(input("Enter element: ")) for _ in range(n)]
    print("\nEntered list")
    display(sort_list)
    quick_sort(sort_list, 0, n-1)
    print("\nSorted list")
    display(sort_list)