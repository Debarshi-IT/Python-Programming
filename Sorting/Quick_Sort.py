def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Taking input from the user
arr = list(map(int, input("Enter numbers separated by spaces: ").split()))

sorted_arr = quick_sort(arr)

print("Sorted array:", sorted_arr)
