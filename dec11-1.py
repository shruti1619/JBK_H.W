s="insTagram"
print(f"real string is : {s}")

s1="Insta&gram a&nd Face&book"
words=s1.split(" ")
print(words)           # ['Instagram', 'and', 'Facebook'] it will separate all words
print(len(words))

w1=s1.split("&")
print(w1)              # ['Insta', 'gram a', 'nd Face', 'book'] separate word by 
                       # perticular char
newstring="#".join(w1)
print(newstring)       # Insta#gram a#nd Face#book ---> it will replace & by #

n1="**".join(words)
print(n1)              # Insta&gram**a&nd**Face&book ---> it will replace space by **

v1="insta"
v2="gram"
v3=v1+v2   #instagram
v4=v1.join(v2)  #ginstarinstaainsta --->v2 alpha than v1 hole string print
print(f"{v3} \n {v4}")
#To join v1 and v2 by method we have append method


a="abdh1234"
print(a.isalnum())#True
print(a.isalpha())#False
print(a.isnumeric())#False
print(a.find("h"))
print(a.replace("abdh", "hello")) # hello1234

print("y" in "python") #True
print("123".isnumeric()) #True


"""print(s.startswith("i"))
print(s.endswith("i"))
print(f"count of a is {s.count("a")}")  #2 there are 2 'a' in string
print(f"string in upper case {s.upper()}")
print(f"string in lower case {s.lower()}")
print(f"string in casefold {s.casefold()}")
print(f"string in swapcase {s.swapcase()}")"""