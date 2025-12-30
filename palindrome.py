# palindrome means, the sequence reads the same backward as forward.


def palindrome(number):
    print("Original number:", number)
    
    original_num = str(number)

    if number  < 0:
        return False
    

    reversed_num = original_num[::-1]
    # print("Reversed Number:", reversed_num)

    if original_num == reversed_num:
        return True
    else:
        return False
    
y = palindrome(121)
x = palindrome(123)
print(y)
print(x)