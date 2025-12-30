
def print_sum_of_current_num_and_previous_num():
    previous_num = 0

    print("Printing current and previous number sum in a range(10)")

    for i in range(1, 11):
        sum = previous_num + i
        # print(i, " - ",sum)
        print("Current Number", i, "Previous Number", previous_num, "Sum:", sum)
        previous_num = i

print_sum_of_current_num_and_previous_num()