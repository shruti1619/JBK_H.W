#-------for identity operator in python--------

# a=10
# b=10
# print(id(a))  #o/t: 140732799872208
# print(id(b))  #o/t: 140732799872208
# print(id(a)==id(b))  #o/t: True
# print(a is b)  #o/t: True
# print(a is not b)  #o/t: False

# print("For to check int id ")
# a=int(input("Enter a value for a: "))
# b=int(input("Enter a value for b: "))
# print(f"a: {a}, b: {b} ")
# if a is b:
#     print("a and b are same objects")
# else:   
#     print("a and b are different objects")


#print("For to check str id ")
# a=input("Enter a value for a: ")
# b=input("Enter a value for b: ")
# print(f"a: {a}, b: {b} ")
# if a is b:
#     print("a and b are same objects")
# else:   
#     print("a and b are different objects")


#---------------for membership operator in python--------

# to check wheteher python is present in the given list or not

l1=["java","python","cpp","c#","javascript"]
# print("python" in l1)        #o/t: True
# print("shruti" in l1)        #o/t: False
# print("java" not in l1)      #o/t: False

# to print all languages containing 'a' in them from the given list
for lang in l1:
    print(lang)
    if "a" in lang:
        print(f"'a' is present in {lang}")
            
# 2nd way to print all languages containing 'a' in them from the given list
for lang in l1:
    print(f"{lang} ---->", "a" in lang)