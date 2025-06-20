
def main():
    st1 = input("Please enter your string: ")
    st2 = input("Please enter your name: ")
    
    print(st1 + " " + st2)
    
    st3 = st1 + st2
    print("Length of the string is:", len(st3))
    for char in st3:
        print(char)

if __name__ == "__main__":
    main()
