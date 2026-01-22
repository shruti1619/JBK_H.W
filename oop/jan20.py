class parent:
    def m1(self):
        print(333)
        
class child(parent):
    def m2(self):
        print(555)
        
p1=parent()
p1.m1()

c1=child()
c1.m1()
c1.m2()