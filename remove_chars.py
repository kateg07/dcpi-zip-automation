
def remove_chars(word, n):
    result = ""
    print("Original word:", word)
    for i in range(len(word)):
        result = word[n:]
    print("'",result,"'", "first", n, "characters removed")

remove_chars("pynative", 4)