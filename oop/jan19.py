class student:
    #class var
    c_name="TKA"
    def __init__(self,r,n,m):
        self.roll=r
        self.name=n
        self.marks=m
        
# IT IS INSTANCE METHOD ALL BELOW 4 METHODS      
    # def displayAllDetails(self):
    #     print(self.roll)
    #     print(self.name)
    #     print(self.marks)
        
    # def getRoll(self):
    #     return self.roll
    
    # def getName(self):
    #     return self.name
    
    # def getMarks(self):
    #     return self.marks
    
# IT IS CLASS METHOD
    @classmethod
    def displayclass1(cls):
        print(cls.c_name)
        # print(cls.roll)  #It will display error because class method have decorater so it will only access #                    class method
        
    @classmethod
    def updateclgname(cls,nclg):
        cls.c_name=nclg
        return cls.c_name
            
        
# IT IS INSTANCE METHOD    
    def displayclass2(self):
        print(self.c_name)
        print(self.roll)
        
     #LOCAL METHOD   
    @staticmethod  
    def computePercentage(m1,m2,m3,m4,m5):
        sum=m1+m2+m3+m4+m5
        per=(sum/500)*100
        return per
    
    
s1=student(1,"shruti",90)
# print(s1.getRoll())
# print(s1.getName())
# print(s1.getMarks())
# s1.displayAllDetails()

s1.displayclass1()
s1.displayclass2()
res=student.updateclgname("taa")   #or
res1=s1.updateclgname("JBK")
print(res1)
print(res)


RES3= s1.computePercentage(90,98,97,95,80)
print(RES3)

        