# LEVEL 01 Dict :-
mi={}
mi[42]="rohit sharma"
mi[1]="shruti morey"
mi[2]="piyush morey"
mi[3]="madhuri morey"
mi[4]="kishor morey"
print(mi)
print(mi[42])
mi[42]="ambrish puri"
print(mi)
mi[6]="i love you"
print(mi)
mi[93]="jaspreet Bumrah"
print(mi)

for i in mi:
    print(i)  # it will print keys i.e jursey no.
    
for i in mi:
    print(mi[i])  # NOW you will get player name
    
    
for i in mi:
    print(i,"----->",mi[i])  # IT will give both keys and value i.e jersey no. and player
    
print("Total players in mi :-",len(mi))
print("There are",len(mi),"with jersey nu. :-")
for i in mi:
    print(i)
    
# TO PRINT PLAYERS NAME WHICH HAVE "Y" IN THIRE NAME AS WELL AS HOW MANY PLAYERS HAVE "Y" IN THEIR NAME
s11="""TO PRINT PLAYERS NAME WHICH HAVE "Y" IN THIRE NAME AS WELL AS HOW MANY PLAYERS HAVE "Y" IN THEIR NAME"""
print("\n",s11)

count=0
for i in mi:
    if "y" in mi[i]:
        print(mi[i])
        count=count+1
        
print("Total y wale players :-",count)

# TO PRINT names of player with have greater than 10 char
print("\nTO PRINT names of player with have greater than 10 char :-")
count=0
for i in mi:
    if len(mi[i])>12:
        print(mi[i])
        count=count+1
        
print("Total players have upper char than 10 are :-",count)

# TO DISPLAY EACH CHAR OF TOTAL NAME ENDS WITH h
print("\nTO DISPLAY EACH CHAR OF TOTAL NAME ENDS WITH h :-")
for i in mi:
    if mi[i].endswith('h'):
        for ch in mi[i]:
            print(ch)

        
        
