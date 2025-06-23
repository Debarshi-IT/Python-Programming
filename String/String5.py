def main():
    sb = list("Debarshi")
    print("".join(sb))

    # charAt equivalent
    print(sb[0])

    # Insert value into string at any position
    sb.insert(0, 'p')
    print("".join(sb))

    # Delete value from string at any position
    del sb[0]
    print("".join(sb))

    # Use of append function
    sc = list("Chatterjee")
    print("".join(sc))

if __name__ == "__main__":
    main()
