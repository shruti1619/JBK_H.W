# s1='instagram123'
# s2="insta@#$$%%^  "
# s3="""     menu : 
#             1. Tea
#             2.Coffee
#             3.Juice
#             4.Water"""
# s4='''insta  $%%1234'''

# print(s1,type(s1),len(s1))
# print(s2,type(s2),len(s2))
# print(s3,type(s3),len(s3))
# print(s4,type(s4),len(s4))


s="instagram"

r1=s[2]
r2=s[3]
r3=s[4]
r4=s[5]

print(type (r1))
#print(r1,r2,r3,r4)   # o/p---->  s t a g or we can get output by doing concatenation as 
#                                  below
res=r1+r2+r3+r4         
print(res,type(res))    #o/p---->  s t a g
res1=s[2]+s[3]+s[4]+s[5]
print(res1)              #o/p---->  s t a g

# print(s[19])    # IndexError: string index out of range

r5=s[0]+s[1]+s[2]+s[3]+s[4]
v1=s[-9]+s[-8]+s[-7]+s[-6]+s[-5]
print(v1)           # insta
print(r5)           # insta

r6=s[6]+s[7]+s[8]
v2=s[-3]+s[-2]+s[-1]
print(r6)   # ram
print(v2)   # ram

r7=s[3]+s[4]+s[5]
v3=s[-6]+s[-5]+s[-4]
print(r7)       # tag
print(v3)        # tag

r8=s[4]+s[3]+s[2]+s[1]+s[0]             
v4=s[-5]+s[-6]+s[-7]+s[-8]+s[-9]
print(r8)                   # atsni
print(v4)                   # atsni

r9=s[8]+s[7]+s[6]
v5=s[-1]+s[-2]+s[-3]
print(r9)          # mar
print(v5)           # mar

r10=s[5]+s[4]+s[3]
v6=s[-4]+s[-5]+s[-6]
print(r10)          # gat
print(v6)           # gat




# print(s[0])  # i 
# print(s[-9]) # i
#OR
# v1=s[0]
# v2=s[-9]
# print(v1,v2)  #i i

# print(s[8])        #m
# print(s(len-1))   #m
# print(s[-1])       #m
