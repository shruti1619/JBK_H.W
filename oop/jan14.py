class player:
    def __init__(self,jn,nm,rn,wk,tn):
        self.jersy_no=jn
        self.name=nm
        self.run=rn
        self.wicket=wk
        self.t_name=tn
        
p1=player(jn=18,nm="virat kohli",wk=5,tn="RCB",rn=9876)
p2=player(jn=7,nm="M. S. Dhoni",tn="CSK",rn=4356,wk=10)
p3=player(10,"Sachin tendulkar",9087,19,"ABCD" )
p4=player(jn=12,nm="Shruti",rn=9872,wk=2,tn="XYZ")
p5=player(tn='PQR',nm="Sejal",rn=2345,wk=6,jn=15)

print(p4.name,p4.run  )
print(p3.name,p3.jersy_no,p3.run)    

all_team_name=[]
all_team_name.append(p1)
all_team_name.append(p2)
all_team_name.append(p3)
all_team_name.append(p4)
all_team_name.append(p5)

print(all_team_name)     # it will print list but of objects memmory location

for p in all_team_name:
    print(p.name)            # it will print all player name 
    if p.run>9500:
        print(p.name)        # it will print players name whos name is greater than 9500