# FIND COUNT OF CHAR IN GIVEN STRING
"""print("find total white spaces in given string")
s='Welcome to Kiran Academy'

count=0
for ch in s:
    if ch==" ":
        count=count+1
print(f"There are total {count} in string '{s}'")"""

# FIND COUNT OF CHAR IN GIVEN STRING
"""print("***find total of any charachter  in given string***\n")
s='Welcome to Kiran Academy'
print(s)
char =input("Enter char from above string :- ")
count=0
for ch in s:
    if ch==char:
        count=count+1
print(f"There are total {count} of {char}'s in string '{s}'")"""


"""print("***find total of any charachter  in any string***\n")
s=input("Enter any string :- ")
print(s)
char =input("Enter char from above string :- ")
count=0
for ch in s:
    if ch==char:
        count=count+1
print(f"There are total {count} of {char}'s in string '{s}'")"""

#THERE ARE SEPARATE METHOD OF PYTHON COUNT NO NEED TO WRITE THIS WHOLE CODE FOR EX:-
strg=input("Enter a string ")
a=input("enter a char :- ")
# cmd=strg.count(a)
# print(f"there are total {cmd}")  #or
print(f"There are total {strg.count(a)}")