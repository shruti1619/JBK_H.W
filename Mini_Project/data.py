from models import *

mi_team = [ player(45, "Rohit Sharma", 6211, 15, "MI"),
           player(63, "Suryakumar Yadav", 4000, 5, "MI"),
           player(33, "Ishan Kishan", 2000, 0, "MI"),
           player(77, "Tilak Varma", 800, 2, "MI"),
           player(7, "Hardik Pandya", 2000, 50, "MI"),
           player(93, "Kieron Pollard", 3412, 47, "MI"),
           player(99, "Jasprit Bumrah", 50, 150, "MI"),
           player(22, "Trent Boult", 100, 90, "MI"),
           player(55, "Piyush Chawla", 200, 160, "MI"),
           player(11, "Tim David", 600, 0, "MI"),
           player(12, "Cameron Green", 500, 15, "MI"),]

csk_team =[ player(7, "MS Dhoni", 5000, 0, "CSK"),
            player(31, "Ruturaj Gaikwad", 1800, 0, "CSK"),
            player(8, "Ravindra Jadeja", 2500, 150, "CSK"),
            player(99, "Shivam Dube", 1200, 10, "CSK"),
            player(90, "Devon Conway", 800, 0, "CSK"),
            player(9, "Ambati Rayudu", 4000, 0, "CSK"),
            player(18, "Deepak Chahar", 200, 60, "CSK"),
            player(28, "Matheesha Pathirana", 50, 40, "CSK"),
            player(46, "Moeen Ali", 1000, 30, "CSK"),
            player(25, "Ben Stokes", 920, 30, "CSK"),
            player(10, "Dwaine Pretorius", 300, 20, "CSK")]

kkr_team = [ player(27, "Shreyas Iyer", 2800, 0, "KKR"),
             player(99, "Andre Russell", 2200, 90, "KKR"),
             player(12, "Nitish Rana", 2200, 10, "KKR"),
             player(23, "Rinku Singh", 800, 0, "KKR"),
             player(74, "Sunil Narine", 1000, 150, "KKR"),
             player(11, "Varun Chakravarthy", 20, 70, "KKR"),
             player(21, "Vaibhav Arora", 10, 25, "KKR"),
             player(19, "Lockie Ferguson", 50, 40, "KKR"),
             player(9, "Venkatesh Iyer", 1200, 15, "KKR"),
             player(88, "Rahmanullah Gurbaz", 500, 0, "KKR"),
             player(17, "Harshit Rana", 30, 20, "KKR")]

srh_team = [ player(19, "Pat Cummins", 300, 50, "SRH"),
             player(23, "Travis Head", 600, 5, "SRH"),
             player(99, "Abhishek Sharma", 1200, 20, "SRH"),
             player(33, "Heinrich Klaasen", 800, 0, "SRH"),
             player(18, "Rahul Tripathi", 2000, 0, "SRH"),
             player(7, "Aiden Markram", 1000, 15, "SRH"),
             player(10, "Bhuvneshwar Kumar", 200, 150, "SRH"),
             player(22, "Umran Malik", 50, 40, "SRH"),
             player(55, "Washington Sundar", 600, 30, "SRH"),
             player(11, "Mayank Agarwal", 2300, 0, "SRH"),
             player(5, "Jaydev Unadkat", 100, 90, "SRH"),]

rcb_team = [ player(18, "Virat Kohli", 7263, 4,"RCB"), 
            player(17, "AB de Villiers", 5162, 0,"RCB"), 
            player(31, "Chris Gayle", 4965, 18,"RCB"), 
            player(1, "Faf du Plessis", 4000, 0,"RCB"), 
            player(9, "Glenn Maxwell", 2500, 30,"RCB"), 
            player(99, "Dinesh Karthik", 4000, 0,"RCB"), 
            player(5, "Anil Kumble", 100, 45,"RCB"), 
            player(10, "Mohammed Siraj", 200, 50,"RCB"), 
            player(27, "Harshal Patel", 300, 60,"RCB"), 
            player(7, "Yuzvendra Chahal", 100, 125,"RCB"), 
            player(12, "Rajat Patidar", 500, 0,"RCB"), ]

teams = {
    "MI":mi_team,
    "CSK":csk_team,
    "RCB":rcb_team,
    "KKR":kkr_team,
    "SRH":srh_team
}