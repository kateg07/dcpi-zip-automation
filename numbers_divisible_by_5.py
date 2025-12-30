
def numbers_divisible_by_5(list_of_numbers):
    for i in list_of_numbers:
        if(i % 5 == 0):
            print(i)


numbers_divisible_by_5([10, 20, 33, 46, 55])