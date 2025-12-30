
def check_first_and_last_num_of_list_if_same(num_list):
    if(num_list[0] == num_list[-1]):
        return True
    else:
        return False
    

numbers_x = check_first_and_last_num_of_list_if_same([10, 20, 30, 40, 10])
numbers_y = check_first_and_last_num_of_list_if_same([75, 65, 35, 75, 30])
print(numbers_x)
print(numbers_y)