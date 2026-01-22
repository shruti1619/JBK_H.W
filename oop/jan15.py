class student:
    # it is inbuild constructor 
    def __init__(self,r,n,c,s):
        # This two print stmt will show all objects like s1 & s2 and self address are show means for each address it is same
        print("Memory Address of self is ")
        print(id(self))
        self.roll_no=r
        self.name=n
        self.city=c
        self.subject=s
        
s1=student(21,"shruti","Chandrapur","Data science")
print("Memory Address of s1 is ")
print(id(s1))
print(f"Roll no. {s1.roll_no}, {s1.name} is from  city {s1.city} and studing {s1.subject}")

s2=student(23,"priti","pune","Data Analytics")
print("Memory Address of s2 is ")
print(id(s2))
print(f"Roll no. {s2.roll_no}, {s2.name} is from  city {s2.city} and studing {s2.subject}")
