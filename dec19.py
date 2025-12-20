# mi={}
# mi[42]="rohit sharma"
# mi[1]="shruti morey"
# mi[2]="piyush morey"
# mi[3]="madhuri morey"
# mi[4]="kishor morey"

# for i in mi.items():
#     print(i[-1][0])  # IT WILL PRINT ALL 1ST LETTER OF NAMES

movies2025={}
d_cast=["ranveer singh","akshay khanna", "sara arjun","sanjay dutt"]
s_cast=['aneet padda','ahan pandy','shradha kapoor' ]
z_cast=["jason bateman","ginnifer goodwin","ke huy quan","fortune feimster"]
r_cast=["ajay devgn","riteish deshmukh","vaani kapoor"]
c_cast=["Vicky ","akshay khanna","rashmika manadana"]

movies2025["Dhurandhar"]=d_cast
movies2025["Saiyaara"]=s_cast
movies2025["Zootopia 2"]=z_cast
movies2025["Raid 2"]=r_cast
movies2025["chavva"]=d_cast

for i in movies2025.keys():
    print(i)            # IT WILL PRINT ALL MOVIES NAMES
    
for names,cast in movies2025.items():
    print(names,"number of cast is :-",len(cast))
    
count=0    
for names,cast in movies2025.items():
    if "akshay khanna" in cast:
        print(names)           #IT WILL PRINT AKSHAY KHANNA MOVIES
        count=count+1
print("Total movies of akshya khanna is :-",count)  #IT WILL PRINT HOW MANY MOVIES AKSHAY 
                                                     #KHANNA IS PRESENT
count=0
for names in movies2025:         # TO PRINT SAME AS ABOVE BUT WITHOUT ITEMS
    if "akshay khanna" in movies2025[names]:
            print(names)
            count=count+1
            
print("Toatal movies are",count)
                 
    
    
