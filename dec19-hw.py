movies2025={}
movies2024={}
movies2023={}

#This dictionary is for 2023 movies
movies2023["Jawan"]= ["Shah Rukh Khan", "Nayanthara", "Vijay Sethupathi", "Deepika Padukone"] 
movies2023["Animal"]= ["Ranbir Kapoor", "Rashmika Mandanna", "Anil Kapoor", "Bobby Deol"]
movies2023["Pathaan"]= ["Shah Rukh Khan", "Deepika Padukone", "John Abraham"]
movies2023["Gadar 2"]= ["Sunny Deol", "Ameesha Patel", "Utkarsh Sharma"]  

#This dictionary is for 2024 movies
s_cast=["Rajkummar Rao", "Shraddha Kapoor"]
b_cast=["Kartik Aaryan", "Vidya Balan", "Madhuri Dixit"]
sg_cast=["Ajay Devgn", "Deepika Padukone", "Akshay Kumar"]
f_cast=["Hrithik Roshan", "Deepika Padukone", "Anil Kapoor"]    

movies2024["Stree 2"]=s_cast
movies2024["Bhool Bhulaiyaa 3"]=b_cast
movies2024[ "Singham Again"]=sg_cast
movies2024["Fighter"]=f_cast

#This dictionary is for 2025 movies
movies2025["Chhaava"]= ["Vicky Kaushal", "Rashmika Mandanna", "Akshaye Khanna"]
movies2025["Dhurandhar"]= ["Ranveer Singh", "Akshaye Khanna", "R. Madhavan", "Arjun Rampal", "Sanjay Dutt", "Sara Arjun"]
movies2025["Saiyaara"]= ["Ahaan Panday", "Aneet Padda"]
movies2025["Ek Deewane Ki Deewaniyat"]= ["Harshvardhan Rane", "Sonam Bajwa"]

allmovies = {2025:movies2025, 2024:movies2024, 2023:movies2023}

#1️⃣ How do you print all movies released in 2023?
"""
for i in movies2023:
    print(f"Movie release in 2023 is : {i}")
    """
for yrs,mov in allmovies.items():
    if yrs ==2023:
        #print(mov.keys())  # or
        for movie in mov:
            print(f"Movie release in 2023 is : {movie}")
    
# 1.1 TO ITERATE year wise ALL MOVIES
for yrs,mov in allmovies.items():
    for mv in mov:
        print(f"{yrs} -----> {mv} \n")
    
#  1.2 TO ITERATE MOVIES and thire perticular cast
for yrs,mov in allmovies.items():
    for mov,cast in mov.items():
        print(f"{mov} ---> {cast}\n")
    
#2️⃣ How do you print all cast members of the movie Jawan?
for yrs,mov in allmovies.items():
    #print(yrs,"--",mov)
    for mov,cast in mov.items():
        if mov=="Jawan":
            a=0
            for word in cast:
                a=a+1
                print(f"{a}. Cast of movie {mov} is {word}")
               
#3️⃣ How do you print movie name + cast for 2024 movies?
for yrs,mov in allmovies.items():
    if yrs == 2024:
        for movie,cast in mov.items():
            print(f"\n Movies name is {movie} and cast are {cast}\n")
            
#4️⃣ How do you find how many movies Akshaye Khanna is acting in from 2023 to 2025? 
count=0
for yrs,mov in allmovies.items():
    for mv,cast in mov.items():
        
        if "Akshaye Khanna" in cast:
            count=count+1
            print(f"Akshaye Khanna appear in {mv} on {yrs}")
print(f"total movies from 2023 to 2025 are {count}")

# 5. How do you count how many movies were released in each year?

for yrs,mov in allmovies.items():
      print(f"Movies were released in {yrs}--->{len(mov)}")
    
# 6. How do you print all years available in the dataset?
for yrs in allmovies.keys():
    print(yrs)
    
# 7. How do you print all movie names available in the dataset?
for yrs,mov in allmovies.items():
    for mv in mov:
        print(f"{mv}")





        

