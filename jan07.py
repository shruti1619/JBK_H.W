test_m=[91,56,44,59,90,90,91,91]
grace_m=[]

# --------------FIERST APPROACH TO ADD FIVE IN LIST----------------------
# for i in test_m:
#     # i += 5
#     # grace_m.append(i)  #or
#     grace_m.append(i+5)
# print(grace_m)

# -------------SECOND APPROACH TO ADD 5 IN LIST -------------------------
def addfive(n1):
    return n1+5

# for i in test_m:
#     # m=addfive(i)
#     # grace_m.append(m)   #or
#     grace_m.append(addfive(i))
    
# print(grace_m)

# -------------------TO DO SAME WORK BY MAPPING TO REDUCE LINE OF CODE----------------------------
grace_m=list(map(addfive,test_m))
print(grace_m)



#----------------------------------FILTER FUNCTION-------------------------------------------------
topper_list=[]

def topper(marks):
    return marks>85

topper_list=list(filter(topper,test_m))
print(topper_list)

# ----------------TO CEHCK VALUE TRUE OR FALSE ACCORDING TO CONDITON AND MAP FUNCTION-----------------
yes_no=[]
yes_no=list(map(topper,test_m))
print(yes_no)

#-----------------------------------REDUCE FUNCTION---------------------------------------------------
from functools import reduce
def addtwo(a,b):
    return a+b
#-----To find all list element sum using reduce------ 
sum=reduce(addtwo,test_m)
print("sum of all list element :- ",sum)

# To find multiplication of list element
def mul(a,b):
    return a*b

multi=reduce(mul,test_m)
print("multiplication of list :- ",multi)

# To find max value over list 
def max(a,b):
    if a>b:
        return a
    elif a==b: 
       return b
    
maximum=reduce(max,test_m)
print("maximum from all list :- ",maximum)

# To find min value in list
from functools import reduce
def min(a,b):
    if a > b:
        return b
    else:
        return a
    
minimum=reduce(min,test_m)
print("minimun value from list is :- ",minimum)


#--------------------------------------LAMBDA FUNCTION-------------------------------------------

#----------------------------------To Add 5 in each marks using lambda---------------------------
grace_mark_by_lamda=[]
grace_mark_by_lamda=list(map(lambda m:m+5 if m<90 else m,test_m))
print(grace_mark_by_lamda)

#--------------------------------To return values greater than 85 using lamda--------------------
greater=[]
greater=list(filter(lambda m:m>85,test_m))
print(greater)

#---------------------------------To find higher value from list using lambda--------------------
max_lamda=[]
max_lamda=reduce(lambda a,b: a if a>b else b,test_m)
print(max_lamda)