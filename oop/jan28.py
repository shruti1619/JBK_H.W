print(4/2)
print(4/4)
try:
    print(4/0)
except ZeroDivisionError as e:
    print("Infinity")
    print(e)
    
try:
    print(4/5)
except ZeroDivisionError as e:
    print(e)
else:
    print("Successfully code runs of division")
    try:
        print(4/0)
    except ZeroDivisionError as e:
        print("eception")
        
finally:
    print("if exception comes or not it will always run. it is cleanup activity")
    
print(2/4)

# try:
#     # num1=int(input("Enter num 1:- "))
#     # num2=int(input("Enter num 2:- "))
#     print(num1/num2)
    
# # except NameError as e:
# #     print("NAME error")
    
# # except ValueError as e:
# #     print("value error")

# # except Exception as e:     # for all eception or if you dont know the exception name
# #     print(e)

# except (ZeroDivisionError,NameError,ValueError) as e:
#     print("Write only interger and also avoid 0 on num2")
#     print(e)
    


class HumPadhaiNhiKrengeException(Exception):
    def __init__(self,msg):
        self.message=msg
        super().__init__(msg)
        
        
m=60
try:
    if m<70:
        obj=HumPadhaiNhiKrengeException("nhi krenge")
        raise obj
except HumPadhaiNhiKrengeException as e:
    print(e)