class player:
    def __init__(self,n,jn,r,w,t):
        self.__jersey_no=jn
        self.__name=n
        self.__run=r
        self.__wicket=w
        self.__team=t
        
    def getJN(self):
        return self.__jersey_no

    def setJN(self,nj):
        self.__jersey_no=nj
        
    def getName(self):
       return self.__name
    def getRun(self):
        return self.__run
    def getWicket(self):
        return self.__wicket
    def getTeam(self):
        return self.__team
    
    def setName(self,nn):
        self.__name=nn
    def setRun(self,nr):
        self.__run=nr
    def setWicket(self,nw):
        self.__wicket=nw
    def setTeam(self,nt):
        self.__team=nt
        
        
p1=player("virat ",18,12000,4,"india")
jn=p1.getJN()
print("jersey no is:",jn)
p1.setJN(46)
jn=p1.getJN()
print("new jersey no is:",jn)

p2=player("rohit sharma",45,9000,2,"india")

name=p2.getName()
print(name)

p1.setName("virat kohli")
n=p1.getName()
print("new name is:",n)

p1.setTeam("RCB")
team=p1.getTeam()
print("new team is:",team)

print(p1)