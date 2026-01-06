print("********* Functional Programming Nested function Closure **********")

def total_a(s):
    count=0
    for ch in s:
        if ch=='a' or ch=='A':
            count +=1
            
    def index_ch():
        print("-------Calling inner functon------")
        i=0
        for ch in s:
            print(f"{i} ----> {ch}")
            i += 1
            
    return count,index_ch

string=input("Enter a string to find toatal A's :- ")
count,index_func=total_a(string)
print("Total no. of A's in String is ",count) 

res1=index_func()


print("********* Functional Programming 3 nested function **********\n")

def total_a(s):
    print("-----calling outer function------")
    count=0
    for ch in s:
        if ch=='a' or ch=='A':
            count +=1
            
    def index_ch(str=s):
        print("-------Calling inner functon------")
        i=0
        for ch in str:
            print(f"{i} ----> {ch}")
            i += 1
            
        def concatenate_str():
            print("------super inner function is calling------")
            combine_str=s+" "+str
            return combine_str
        
        return concatenate_str()
            
    return count,index_ch

string=input("Enter a string to find toatal A's :- ")
count,index_func=total_a(string)
print(f"Total no. of A's in String is {count} \n") 
st=input("Enter string to perform inner function :- ")
res=index_func(st)
print("This is combination of both function string separated by space :- ",res)

