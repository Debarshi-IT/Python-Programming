def main():
    r = int(input("Enter row size: "))
    c = int(input("Enter column size: "))
    
    arr = []
    print("Enter the values:")
    for i in range(r):
        row = list(map(int, input().split()))
        arr.append(row)

    print("2D array is:")
    for row in arr:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    main()
