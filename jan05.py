def sign_up(en,age,cn="tcs",sal=25000):
    
    print(f"Name of emplayee is {en}")
    print(f"Age of emplayee is {age}")
    print(f"Salary of emplayee is {sal}")
    print(f"Company name of emplayee is {cn}") 
    
 # POSITIONAL ARGUMENTS 
print("--------POSITIONAL ARGUMENT--------")  
#sign_up(24,25000,"tcs","jay")
                              # it will print  :---> Name of emplayee is 24
                              #                      Age of emplayee is 25000
                              #                      Salary of emplayee is tcs
                              #                      Company name of emplayee is jay
                              
# KEY-WORD Arguments
print("----------BY KEY-WORD ARGUMENTS------------")
#sign_up(age=24,sal=25000,cn="tcs",en="jay")


# DEFAULT ARGUMENT :--> 
# 1.Dont write default at first 
# 2.after default dont write paramenter
#3. we can write at first only if all parameters are default 
print("-----------DEFAULT ARGUMENTS----------")
sign_up(age=24,en="jay")
sign_up(age=20,en="shruti",cn="Google",sal="5000000")
sign_up(age=20,en="shruti",cn="microsoft")
# sign_up(age=24,sal=25000,cn="tcs",en="jay")
# sign_up(age=24,sal=25000,cn="tcs",en="jay")
# sign_up(age=24,sal=25000,cn="tcs",en="jay")

# ARBITARY ARGUMENTS
print("------------ POSITINAL Arbitary argument------------")
def add(*args):
    print(args)
    print(type(args))
    sum=0
    for i in args:
        sum +=i
    
    return(sum)
    
res=add(40,30,10,20)
print(res)

print("----------KEY-WORD ARBITARY Argument--------------")
def submit(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k ,"---->",v)
    
submit(name="shruti",mobile=937022)    
