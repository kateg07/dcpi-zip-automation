
def find_repeated_string(strings, substring=None):
    print("Original string:", strings)
    cnt = strings.count(substring)
    print(substring,"appeared",cnt,"times")

find_repeated_string("Emma is good developer. Emma is a writer", substring="Emma")
# find_repeated_string("Emma is good developer. Emma is a writer")