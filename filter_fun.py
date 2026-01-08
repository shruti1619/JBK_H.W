#------------------------------Filter all even numbers from a list.---------------------------------------
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ev_num=[]

def even(x):
    if x % 2 == 0:
        return x
    
ev_num=list(filter(even,nums1))
print("Even number list is :- ",ev_num)


#-------------------------------Filter all odd numbers from a list.--------------------------------------
nums2 = [11, 22, 33, 44, 55, 66]
od_num=[]
def odd(x):
    if x % 2 !=0:
        return x
    
od_num=list(filter(odd,nums2))
print("Odd number list is :- ",od_num)


#--------------------------------Filter numbers greater than 50 from a list.------------------------------
nums3 = [10, 45, 50, 55, 60, 75, 30]
g_50=[]

def greater(x):
    if x>50:
        return x
    
g_50=list(filter(greater,nums3))
print("list of numbers which is greater than 50 :- ",g_50)


#---------------------------------Filter all positive numbers from a list containing negatives.------------
nums4 = [-10, -5, 0, 5, 10, -2, 8]
posi_num=[]

def positive(x):
    if x>0:
        return x
    
posi_num=list(filter(positive,nums4))
print("List of Positive numbers :- ",posi_num)


#-----------------------------------Filter strings with length greater than 5.-------------------------------
words = ["apple", "banana", "cat", "elephant", "dog", "python"]
g_str=[]

def greater_five_len(x):
    if len(x)>5:
        return x
    
g_str=list(filter(greater_five_len,words))
print("List of string who's lenght is greater than 5 :- ",g_str)


#-----------------------------------filters vowels from characters-------------------------------------------
chars = ['a', 'b', 'e', 'i', 'o', 'u', 'z']
vow_list=[]

def vowels(x):
    if x in "aeiou":
        return x
    
vow_list=list(filter(vowels,chars))
print("List of vowels char :-",vow_list)


#------------------------------------Filter names that start with a vowel.--------------------------------------
names = ["Anu", "Ravi", "Om", "Kiran", "Ishita"]
vow_start=[]

def vol_start_names(x):
    
    if x[0].lower() in ("aeiou"):
        return x
    
vow_start=list(filter(vol_start_names,names))
print("List of names starting with vowels :-",vow_start)


#------------------------------------- Filter numbers that are divisible by both 3 and 5.--------------------------
nums = [12, 15, 18, 21, 24, 30, 35]
div_list=[]

def div_by_5_3(x):
    if x %3==0 and x % 5 ==0:
        return x
    
div_list=list(filter(div_by_5_3,nums))
print("List of numbers which is divisible by both :-",div_list)


#-------------------------------------From a list of strings, filter words that contain the letter ‘a’.-------------------
names = ["Anu", "Ravi", "Om", "Kiran", "Ishita"]
cont_a=[]

def contain_a(x):
    for i in x:
        if i =='a':
            return x
    
cont_a=list(filter(contain_a,names))
print(cont_a)


#------------------------------------ Filter all palindrome strings from a list.-----------------------------------
words2 = ["madam", "hello", "level", "world", "radar"]
pal_list=[]

def palindrom(x):
    rev=""
    for i in x:
        rev =i+rev
    if rev==x:
        return x
    
pal_list=list(filter(palindrom,words2))
print(pal_list)


#--------------------------------------perfect square filteration---------------------------------------
import math
nums6 = [1, 4, 9, 10, 16, 20, 25]
per_sq=[]

def perfect_sq(x):
    root = int(math.sqrt(x))
    return root*root == x

per_sq=list(filter(perfect_sq,nums6))
print(per_sq)

