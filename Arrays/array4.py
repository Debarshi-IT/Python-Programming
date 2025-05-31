def main():
    r = int(input("Enter row size: "))
    c = int(input("Enter column size: "))

    arr = []
    print("Enter the values:")
    for i in range(r):
        row = list(map(int, input().split()))
        arr.append(row)

    x = int(input("Please enter the search element: "))

    print("Index of 2D array is:")
    for i in range(r):
        for j in range(c):
            if arr[i][j] == x:
                print(f"({i},{j})")

if __name__ == "__main__":
    main()
