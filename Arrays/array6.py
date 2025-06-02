def main():
    n = int(input("Enter the array size: "))
    a = list(map(int, input("Enter elements: ").split()))
    
    print("Current array is:", a)
    print("Reverse array is:", list(reversed(a)))

if __name__ == "__main__":
    main()
