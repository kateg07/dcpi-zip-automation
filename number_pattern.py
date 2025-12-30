
def number_pattern(n):
    print("Original number:",n)
    # for i in range(1, n+1): 
    #     for j in range(1, i+1):
    #         print(i, end=" ")
    #     print("\n")

    for num in range(n):
        for i in range(num):
            print(num, end=" ")
        print("\n")

number_pattern(10)