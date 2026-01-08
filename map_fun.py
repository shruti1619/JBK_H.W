#----------------------map() to return a list of their squares----------------------------
marks=[11, 12, 3, 4, 5]
sq_list=[]

def sq(x):
    return x*x

# for i in marks:
#     m=sq(i)
#     sq_list.append(m)
# print(sq_list)         # THis is not best way to do mapping below is the best method 

sq_list=list(map(sq,marks))
print("THis is the list of squre of given list :- ",sq_list)


#------------------------ Use map() to convert them into integers.-------------------------
str_list=["10", "20", "30"]
int_list=[]

int_list=list(map(int,str_list))
print("List of integer from strings are :- ",int_list)
# This is for loop aproach no need to use when map is there
# for i in str_list:  
#     # x=int(i) ----> why to put x in append when directly I can put int(i) in append 
#     int_list.append(int(i))
# print("List of integer from strings are :- ",int_list)


#------------------------ use map() to make all words uppercase.----------------------------
fruit=["apple", "banana", "cherry"]
upper_fruit=[]

def uppercase(x):
    return x.upper()

upper_fruit=list(map(uppercase,fruit))
print("Upper case fruit list is :- ",upper_fruit)


#-------------------------use map() to return a list of word lengths.--------------------------
string=["Shruti", "Copilot", "Python"]
len_list=[]

def lenght(x):
    return len(x)

# len_list=list(map(lenght,string))
# print("Lenght of all string in list is :- ",len_list)


#--------------------------Convert Celsius values into Fahrenheit using map()-------------------
celsi=[0, 100, 37]
fara =[]

def faranide(c):
    f=round(((9/5)*c)+32, 2)
    return f

fara=list(map(faranide,celsi))
print("The conversion of celsius values to faranide is :- ",fara)


