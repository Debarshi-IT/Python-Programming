def rotate_left(arr, d):
    d %= len(arr)
    return arr[d:] + arr[:d]

def main():
    n = int(input("Enter the array size: "))
    arr = list(map(int, input("Enter elements: ").split()))
    
    d = int(input("Enter the d steps, where d is a positive integer: "))

    print("Original array is:", arr)
    print("The new array is:", rotate_left(arr, d))

if __name__ == "__main__":
    main()
