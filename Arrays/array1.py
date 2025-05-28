def main():
    marks = []
    print("Enter all marks: ")
    for _ in range(10):
        marks.append(int(input()))

    print("The all marks:")
    for mark in marks:
        print(mark)

if __name__ == "__main__":
    main()
