
def merge_two_lists(list1, list2):

    merged_list = []


    # check for odd numbers in list1
    for i in list1:
        if(i % 2 != 0): 
            merged_list.append(i)

    # check for even numbers in list2
    for j in list2:
        if j % 2 == 0:
            merged_list.append(j)

    print(merged_list)

    return merged_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
merge_two_lists(list1, list2)  