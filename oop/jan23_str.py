class player:
    def __init__(self,n,jn,r,w,t):
        self.jersey_no=jn
        self.name=n
        self.run=r
        self.wicket=w
        self.team=t
        
    def __str__(self):
        return f"{self.name} | jersey_no={self.jersey_no}, run={self.run}, wicket={self.wicket}, team={self.team}"
    
    
p1=player("virat ",18,12000,4,"india")
print(p1)