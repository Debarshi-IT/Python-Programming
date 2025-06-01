def second_largest(arr):
    unique_arr = sorted(set(arr), reverse=True)
    if len(unique_arr) > 1:
        print(f"Second largest number is: {unique_arr[1]}")
    else:
        print("-1")

def main():
    test_cases = [
        [12, 35, 1, 10, 34, 1],
        [2, 1, 7, 8, 10, 10],
        [15, 15, 15]
    ]
    
    for arr in test_cases:
        second_largest(arr)

if __name__ == "__main__":
    main()
