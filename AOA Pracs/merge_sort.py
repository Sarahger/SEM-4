# merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        return merge(left_half, right_half)
    return arr

def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

if __name__ == '__main__':
    n = int(input("Enter number of elements: "))
    sort_list = [int(input("Enter element: ")) for _ in range(n)]
    
    print("\nEntered list")
    print(','.join(map(str, sort_list)))

    # calling function
    sorted_list = merge_sort(sort_list)
    print("\nSorted list")
    print(','.join(map(str, sorted_list)))