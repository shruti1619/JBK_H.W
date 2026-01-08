# def name():
#     print("Shruti Morey")
    
# name()

# # NOTE:-To create decorators we always have to do nested fun/Closure in that we can call another function but not modified it
# # We cant not diretly 
# def myDecorators(fun):
#     def wrapperFun():
#         print("Good Morning")
#         print("*" * 15)
#         fun()
#         print("*" * 15)
#         print("Bye Bye")
        
#     return wrapperFun

# wrapper_call_rename=myDecorators(name)
# wrapper_call_rename()

# # name=myDecorators(name)
# # name()                     # instead of this you can do below process to call decorator no need to rename the fun. defi.

#-------------------------To use decorator in different way instead of calling and renaming-------------------------------------
def my_Decorators(fun):
    def wrapper_Fun():
        print("Good Morning")
        print("*" * 15)
        fun()
        print("*" * 15)
        print("Bye Bye")
        
    return wrapper_Fun

@my_Decorators
def address():
    print("Delhi")
    
address()

#--------------------------To take input and perform output after inhancing function--------------------------------------------
def my_decorator(fun):
    def wrap_fun(a,b,c):
        res=fun(a,b)
        res02=res+c
        return res02
    return wrap_fun

@my_decorator
def addition(a,b):
    return a+b
#----------------It will give us sum of three but if we want 2 num addition then we have to comment the DECORATOR-----------------
sum=addition(1,2,3)
print(sum)