# r=range(5)
# print(type(r))
# print(r)
# l=list(r)
# print(l)

# for i in r:
#     print(i)
    
# r1=range(50,61)
# for i in r1:
#     print(i)
    
# r2=range(2,21,2)#to print even no.
# 


# for i in range(5,51,5):
#     print(i)

# 
# num = input("Enter aa num :- ")
# for i in range (1,11):
#     print(f"{num} * {i} = {num*i}")
    
    
# s="instagram"

# for i in range(0,len(s)):
#     if(i%2)==i:
#         print(i,"------->", s[i])
        
# for i in s:
#     print(i)


L=[2,11,5,9,10,12,7]

chotu_sq_list=[]
chotu_cube_list=[]
for i in range(len(L)):
    if i%2==0:
        chotu_sq_list.append(L[i]*L[i])
    else:
        chotu_cube_list.append(L[i]*L[i]*L[i])
        
print("original list:",L)
print("chotu_sq_list:",chotu_sq_list)
print("chotu cube",chotu_cube_list)
    