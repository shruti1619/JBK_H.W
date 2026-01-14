class student:
    #function
    def __init__(self,a,loc):
        self.age=a
        self.location=loc
        
s1=student(10,"pune")
print(s1)
print(type(s1))
print(id(s1))

# a="atul sir"
# print(type(a))

class teacher:
    def __init__(self,sub,stud):
        self.total_sub=sub
        self.total_stud=stud
        
t1=teacher(6,120)
print(t1)
print(type(t1))
print(id(t1))
        
    
class corporation:
    def __init__(self,ep,cl):
        self.total_employee=ep
        self.total_client=cl
        
c1=corporation(520,60)
print(c1)
print(type(c1))
print(id(c1))
        