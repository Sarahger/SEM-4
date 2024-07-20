def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        
        if min_index != i:
            swap(arr, min_index, i)

def binarySearch(arr, x, low, high):
    mid = low + (high - low) // 2
    if arr[mid] == x:
        print(f"Element found at index: {mid}")
        return
    elif arr[mid] > x:
        binarySearch(arr, x, low, mid)
    elif arr[mid] < x:
        binarySearch(arr, x, mid + 1, high)
    else:
        print("Element not found!")

if __name__ == '__main__':
    n = int(input("Enter the number of elements: "))
    arr = [int(input("Enter element: ")) for _ in range(n)]
    selection_sort(arr)
    print(arr)
    search = int(input("Enter the element to be searched: "))
    binarySearch(arr, search, 0, len(arr) - 1)
