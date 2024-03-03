def selection_sort(arr: list):
    for i in range(len(arr)):
        _min_idx = i
        _min_value = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < _min_value:
                _min_idx = j
                _min_value = arr[j]
        arr[i], arr[_min_idx] = arr[_min_idx], arr[i]
    return arr

A = [34, 11, 94, 30, 25]
print(*selection_sort(A))
