class player:
    def __init__(self,jn,nm,rn,wk,tn):
        self.jersey_no=jn
        self.name=nm
        self.runs=rn
        self.wicket=wk
        self.team_name=tn
    
    # IF IN FUTURE WE HAVE TO PRINT PLAYER DETAILS IT WILL ONLY GIVE MEMORY LOCATION in print BUT if we write this func it will   give us proper output without applying for loop   ** Optional: makes printing cleaner **
    def __str__(self):
        return f"{self.jersey_no} - {self.name} | Runs = {self.runs}, Wicket= {self.wicket}, Team_name = {self.team_name}"
   
    ## Optional: easy conversion to dictionary for future DB or JSON use 
    def to_dict(self):
        return {
            "Jersey_no" : self.jn,
            "Name" : self.nm,
            "Runs":self.rn,
            "Wicket":self.wk,
            "Team_Name":self.tn
        }