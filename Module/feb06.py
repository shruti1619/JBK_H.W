import re 
s="I love python progamming"
# IT will check starting or not by r
s1=r"python"
r1=re.match(s1,s)
print(r1)

# search will find first occurance
pattern= r"love"
r2=re.search(pattern,s)
print(r2)

# findall will find all occurance and give list of it
ptn="o"
r3=re.findall(ptn,s)
print(r3)

# TO GET ALL INT VALUE AND FIND THERE SUM
str1="shruti got 90,99,88 in her exam and total is 540."
ptr1=r"\d+"  # \d+ is find all occurence int and give list of str int
re4=re.findall(ptr1,str1)
print(re4)

sum=0
for i in re4:
    sum =sum +int(i)
print("sum of all int is :- ",sum)

# To find number who start with 9 after that zero to all digit can acceptable by *
p4="\b9\d*"

re5=re.findall(p4,str1)
print(re5)
