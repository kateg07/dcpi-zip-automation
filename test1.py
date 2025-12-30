import multiplication_or_sum as mos

# crtl + r to run the program


first = "Kate"
last = "Gonzaga"
len_last = f"{len(last)}"
fullname = first + " " + last

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# thislist[1:3] =  ["chicken", "oreo"] 
x = ["apple", "banana", "cherry"]
y = {"apple", "banana", "cherry"}
z = frozenset({"apple", "banana", "cherry"})
y = {"fruit":"apple", "fruit":"banana", "fruit":"cherry"}

# if "apples" in thislist :
#     print("Yes, 'apple' is in the fruits list") 

# x[1:3] = ["watermelon"]
x[1:2] = ["blackcurrant", "watermelon"]


# print(fullname.upper())
# print(fullname.strip())
# print(fullname.find("Kath"))
# print(fullname.lower()) 
# print(fullname.replace("Kate", "sdf"))
# print(int(len_last)) 
# print(thislist[2:6])
print(thislist[:4])
print(thislist[2:])
# print(thislist[-4:-1])
# print(x)
# print(thislist[1:3])




result = mos.multiplication_or_sum(20, 30)
result = mos.multiplication_or_sum(40, 30)
# print(result)