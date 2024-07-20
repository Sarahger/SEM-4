def min_max(arr):
    n = len(arr)
    if n == 1:
        return arr[0], arr[0]
    if n == 2:
        if arr[0] < arr[1]:
            return arr[0], arr[1]
        else:
            return arr[1], arr[0]
    
    mid = n // 2
    l_min, l_max = min_max(arr[:mid])
    r_min, r_max = min_max(arr[mid:])

    min_val = min(l_min, r_min)
    max_val = max(l_max, r_max)
    
    return min_val, max_val

if __name__ == '__main__':
    arr = [90, 87, 65, 45, 23]
    _min, _max = min_max(arr)
    print(f"Minimum: {_min}\nMaximum: {_max}")