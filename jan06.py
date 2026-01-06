# def fact(N):
#     fact=1
#     for i in range (1,N+1):
#         fact=fact*i
#     return(fact)
# print("-----------Factorial of number logic------------")
# a=eval(input("Enter a number :- "))        
# res=fact(a)
# print("factorial of number is ",res,"\n")


# def factorial(N):
#     print(f"computing factorial of {N}")
#     if N==1:
#         return 1
    
#     return N * (factorial(N-1)) 

# print("-----------Factorial of number logic using reccurssion------------")
# a=eval(input("Enter a number :- "))        
# res=factorial(a)
# print("factorial of number is ",res)


# def add_series(N):
#     add=0
#     for i in range (1,N+1):
#         add=add+i
#     return(add)

#print("------------Addition of all series of a number----------------")
# a=eval(input("Enter a number :- "))        
# res=add_series(a)
# print("factorial of number is ",res)


print("------NESTED FUNCTION------")

def out_fun(x):
    print(f"Outer function calling \n {x}")
    
    def inner_fun():
        print("Inner function calling")
        print(x)
    inner_fun()
    
out_fun(10)

print(" Closure in python ")

def outer_fun(x):
    print(f"Outer function calling \n {x}")
    
    def inn_func(y):
        return x+y
    return inn_func

print("Closures in python calling innner function")
inner_function=outer_fun(10)
res=inner_function(5)
print(res)
    