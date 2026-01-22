class student:
    # CLASS LEVEL VARIABLE jo class me hote hai constructor ke bahar 
    c_name="TKA"
    def __init__(self,r,n,m):
        self.roll=r           # roll,name & marks are INSTANCE Variable and r,n,m are LOCAL Variable which only create in function
        self.name=n
        self.marks=m
        
    def display(self):
        print("\n")
        print(f"Roll number of student is {self.roll}")
        print(f"Name of student is {self.name}")
        print(f"Marks of student is {self.marks}")
        print(f"Company of studentn is {self.c_name}")
        
        
        
        
 #--------------------------------------------------------------------------------------------------------------------------------       
s1=student(1,"Jay",88)
s2=student(2,"viru",98)
print(s1.c_name)
s1.c_name="abc"
print(s2.c_name)  # getting class variable from object name is not recommendated access by class name 
print(s1.c_name)
print(s2.c_name)
print(student.c_name)  # getting class variable from object name is not recommendated access by class name 

#---------------------------------------------------------------------------------------------------------------------------------

s3=student(3,"Jay",88)
s4=student(4,"viru",98)
s5=student(21,"shruti",98)
s5.c_name="Google"
s1.display()
s3.display()
s4.display()
s5.display()



