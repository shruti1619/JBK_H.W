age=int(input("Enter your age: "))

class AgeTooSmallException(Exception):
    def __init__(self,msg):
        self.message=msg
        super().__init__(msg)
        
class AgeTooLargeException(Exception):
    def __init__(self,msg):
        self.message=msg
        super().__init__(msg)
        
try:
    if age<18:
        raise AgeTooSmallException("Age is too small to Drive")
    elif age>75:
        obj=AgeTooLargeException("Age is too large to Drive")
        raise obj
    else:
        print("Welcome to RTO portal!")
except AgeTooSmallException as e:
    print(e)
except AgeTooLargeException as e:
    print(e)