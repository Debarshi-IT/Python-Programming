def main():
    marks = []
    print("Enter all marks: ")
    for _ in range(5):
        marks.append(int(input()))

    x = int(input("Please enter the search element: "))

    for i in range(5):
        if marks[i] == x:
            print(f"Index of number: {i}")

if __name__ == "__main__":
    main()
