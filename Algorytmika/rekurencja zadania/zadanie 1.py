def reverse_arr(arr, l, r):
    if l < r:
        arr[l], arr[r] = arr[r], arr[l]
        reverse_arr(arr, l + 1, r - 1)

reverse_arr([1,2,3,4,5],0,4)