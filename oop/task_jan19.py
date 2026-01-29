class players:
    def __init__(self,jn,n,r,w,tn):
        self.jersey_no=jn
        self.name=n
        self.run=r
        self.wicket=w
        self.team_name=tn
        
    def getname(self):
        return self.name
    
    def getjn(self):
        return self.jersey_no
    
    def getrun(self):
        return self.run
    
    def getwicket(self):
        return self.wicket
    
    def get_tn(self):
        return self.team_name
    
    def update_name(self,new_n):
        self.name=new_n
        
    def update_run(self,new_r):
        self.run=new_r
        
    def update_jersey_no(self,new_j):
        self.jersey_no=new_j
        
    def update_wicket(self,new_w):
        self.wicket=new_w
        
    def update_tn(self,new_tn):
        self.team_name=new_tn
        

s1=players(2,"i_dont_know",100,5,"ABCD")

s1.update_jersey_no(18)
s1.update_name("virat kohli")
s1.update_tn("RCB")
print(s1.name)

    
    