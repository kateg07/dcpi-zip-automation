

def print_char_at_even_index(string):
    result = ""
    for i in range(len(string)):
        if(i % 2 == 0):
            result += string[i]

    print(result)
print_char_at_even_index("PYnative")