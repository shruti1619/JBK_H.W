# PERFORM 20 OPERATIONS ON YOUR NAME LIKE Indexing,Slicing, +ve stepsize,_ve stepsize
# Iterate your name to find freq of any charachter 
# name="SHRUTI"

# # Indexing  
# print(name[0])           #o/t: S
# print(name[5])           #o/t: I
# print(name[2])           #o/t: R
# print(name[-1])          #o/t: I
# print(name[-6])          #o/t: S

# # Slicing
# print(name[2:7])         #o/t: RUTI
# print(name[:3])          #o/t: SHR
# print(name[-3],name[-4],name[-1])           #o/t: U R I
# print(name[:6:2])                           #o/t: SRT
# print(name[::3])                            #o/t: SU
# print(name[-1:-7:-1])                       #o/t: ITURHS
# print(name[-1:-7])                          #o/t: noting will print empty string
# print(name[5:0:-1])                         #o/t: ITURH
# print(name[0:6:3])                          #o/t: SU whether we write 6 or 7 it print same
# print(name[-1:-7:-2])                       #o/t: IUR
# print(name[-7:-1])                          #o/t: SHRUT
# print(name[-8:-1])                          #o/t: SHRUTI
# print(name[::])                             #o/t: SHRUTI
# print(name[0:6])                            #o/t: SHRUTI

#---------Write a Python program to find the length of a given string without using len().
s='InstagraM'
# count=0
# for ch in s:
#     count+=1
# print(f"Given string have {count} length")   

#--*********** Count the number of vowels and consonants in a string.*******************
# vowels="aeiouAEIOU"
# v_count=0
# c_count=0
# for i in s:
#     if i in vowels:
#         v_count+=1
#     else:
#         c_count+=1
# print(f"string have {v_count} vowels and {c_count} consonants") 

#------To revrse a string without using inbuilt function.---------
# rev_s=""
# for i in s:
#     rev_s=i+rev_s
# print(rev_s) 
# print(rev_s == s[::-1])

#------To check whether the given string is palindrome 
# a="shivay"
# rev=""
# for i in a:
#     rev=i+rev 
# if rev==a:
#     print("Given string is palindrome")
# else:
#     print("Given string is not palindrome")


#-----------Count the occurrences of each character in a string.--------------
# char_count={}
# for i in s :
#     if i in char_count:
#         char_count[i]+=1
#     else:
#         char_count[i]=1
# print(char_count)
    
#-----------Remove all the spaces from a string.----------------
string="I am shruti and One day I will be the richest person in the world"
#print(string.replace(" ",""))      #OR you can try below code too
# print(string.replace(" ","_"))      #to replace space with _
# no_space=""
# for i in string:
#     if i==" ":
#         continue
#     else:
#         no_space+=i
# print(no_space)                     # it also removes all spaces from string

# #-------Convert a string to uppercase and lowercase without using .upper() or .lower()-------------

# upper=""
# lower=""
# for i in s:
#     if 'a' <=i <='z':
#         upper += chr(ord(i)-32)
#     else:
#         upper += i
#     if 'A' <= i <='Z':
#         lower += chr(ord(i)+32)
#     else:
#         lower += i
# print(f"Uppercase: {upper} Lowercase: {lower}")    


#-------separate a string to uppercase and lowercase without using .upper() or .lower()--------

# upper=""
# lower=""
# for i in string:
#     if 'a' <=i <='z':
#         upper += chr(ord(i)-32)
#     elif 'A' <= i <='Z':
#         lower += chr(ord(i)+32)
#     else:
#         upper +=" "
#         lower +=" "
    
# print(f"Uppercase: {upper} \nLowercase: {lower}")    