from data import teams

#TO get best score team who's runs more that will be best team
def top_scorer_team(teams):
    
    top_team=None
    top_run=-1
    for team_name, players in teams.items():
        total_run=sum( p.runs for p in players)
        if total_run > top_run:     
            top_run=total_run
            top_team=team_name

    return top_team,top_run

# TO get best bowler team whos have high wicket that will be best team
def best_bowler_team(teams):
    
    top_team=None
    best_wicket=-1
    for team_nm,player in teams.items():
        total_wicket=sum(p.wicket for p in player)
        if total_wicket>best_wicket:
            best_wicket=total_wicket
            top_team=team_nm
            
    return top_team,best_wicket

#To get player details  by serching its name
def search_player_by_name(teams, name):
    
    for team_name,players in teams.items():
        for p in players:
            if p.name.lower()==name.lower():
                return p
            
    return None   # if not found

# Compare two teams who have more runs that will win
def compare_teams_by_runs(teams, t1, t2):
    #To calculate t1's total run
    t1_runs=0
    for p in teams[t1]:
        t1_runs += p.runs
        
    #To calculate t2's total run
    t2_runs=0
    for p in teams[t2]:
        t2_runs += p.runs
        
    if t1_runs > t2_runs:
        return t1,t1_runs
    elif t2_runs > t1_runs:
        return t2,t2_runs
    else:
        return "Tie",t1_runs
    
#--------------------To get list of all players from the teams------------------------------------------------
def list_all_players(teams,team):
    for t,player in teams.items():
        if t==team:
            for p in player:
                return [p.name for p in player]
    


    
        
                     