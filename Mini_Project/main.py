from operations import *
from data import teams

def main():
    while True:
        print("\n--------Cricket Database Menu--------")
        print("1.Show Top Scorer Team")
        print("2.Show Best Bowler Team")
        print("3.Search Player by Name")
        print("4.compare Two Teams by Run")
        print("5.List all Player of a team")
        print("6.Exit")
        
        choice=input("Enter your choice :- ")
        
        if choice == "1":
            team,run=top_scorer_team(teams)
            print(f"\nBest score of the team is {team} and Total Runs are {run}")
            
        elif choice == '2':
            team,wicket=best_bowler_team(teams)
            print(f"\nBest Bowler team i {team} and Total wicket are {wicket}")
            
        elif choice == '3':
            name=input("Enter player name whos you want to get details :- ")
            # name=name.capitalize()
            # print(name)
            player = search_player_by_name(teams, name)
            if player:
                print(player)
            else:
                print("player not found")
                
        elif choice == '4':
            print("\n")
            t1=input("Enter Team 1st you want to take for comparision :- ")
            t2=input("Enter Team 2nd you want to take for comparision :- ")
            team,total_runs=compare_teams_by_runs(teams, t1, t2)
            print(f"The Winner team is {team} and It have total {total_runs} runs.")
            
        elif choice=='5':
            print('\n')
            team=input("Enter team who's player you want to display :- ")
            players_name=list_all_players(teams,team)
            if players_name:
                print(f"---------------------Player of {team} is --------------------------")
                for names in players_name:
                    print(names)
            else:
                print("Team is not found")

        elif choice == "6": 
            print("Exiting program...")
            break
            
            
            
            
if __name__=="__main__":
    main()