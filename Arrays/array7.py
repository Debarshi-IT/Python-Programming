def move_zeros(arr):
    non_zero = [num for num in arr if num != 0]
    zero_count = len(arr) - len(non_zero)
    return non_zero + [0] * zero_count

def main():
    n = int(input("Enter the array size: "))
    arr = list(map(int, input("Enter elements: ").split()))

    print("Original array is:", arr)
    print("New array is:", move_zeros(arr))

if __name__ == "__main__":
    main()
