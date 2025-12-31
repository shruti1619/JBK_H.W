# def add_two(p,q):
#     res=p+q
#     #print(p)
#     return res
    
# print("My Calculator")
# print("Calling of Function")
# op=add_two(10,20)                  #function calling
# print(op)                          #after excuting this fun it is return nothing i.e none 

#---------Task 01----------
def add_three(p,q,r):
    sum=p+q+r
    return sum

# a=int(input("Enter 1st value: "))
# b=int(input("Enter 2nt value: "))
# c=int(input("Enter 3rt value: "))
op=add_three(10,11,12)
print("Addition of three number: ",op)

#---------Task 02----------
def avg_three(p,q,r):
    
    sum=add_three(p,q,r)
    avg=sum/3
    return avg

op1=avg_three(10,20,30)
print("average of three number: ",op1)


#---------Task 03----------
def dic_avg_three(p,q,r):
    
    avg=avg_three(p,q,r)
    dic=(avg*5)/100
    return dic

op2=dic_avg_three(10,20,30)
print("discount of three number: ",op2)