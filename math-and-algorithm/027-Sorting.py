from collections import deque


def merge(arr1, arr2):
    merged_array = []
    arr1, arr2 = map(deque, [arr1, arr2])
    while arr1 or arr2:
        if not arr1:
            merged_array.append(arr2.popleft())
        elif not arr2:
            merged_array.append(arr1.popleft())
        else:
            if arr1[0] <= arr2[0]:
                merged_array.append(arr1.popleft())
            else:
                merged_array.append(arr2.popleft())
    return merged_array


def merge_sort(arr: list):
    k = len(arr)
    if k == 1:
        return arr
    elif k == 2:
        if arr[0] <= arr[1]:
            return [arr[0], arr[1]]
        else:
            return [arr[1], arr[0]]
    mid = k // 2
    arr1, arr2 = arr[:mid], arr[mid:]
    arr1_sorted = merge_sort(arr1)
    arr2_sorted = merge_sort(arr2)
    arr_sorted = merge(arr1_sorted, arr2_sorted)
    return arr_sorted


# N = int(input())
# A = list(map(int, input().split()))
# A_sorted = merge_sort(A)
# print(*A_sorted)


def MergeSort(A):
    # 長さが 1 の場合、すでにソートされているので何もしない
    if len(A) == 1:
        return A

    # 2 つに分割した後、小さい配列をソート
    m = len(A) // 2
    A_Dash = MergeSort(A[0:m])
    B_Dash = MergeSort(A[m:len(A)])
    print(A_Dash, B_Dash)


A = [2, 4, 5, 4, 7, 2]
MergeSort(A)