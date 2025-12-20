c1=20+30j
print(type(c1))
print(c1)

c2= 0b101+0.5j    #0b or 0B is binary represntation
print(type(c2))
print(c2)

c3= 0o123+1.1j    #0o or o0 is octal represntation
print(type(c3))
print(c3)

c4= 0Xface+20j    # 0x  hexadecimal represntation
print(type(c4))
print(c4)

#c5 = 20 + 0b101j --------> invalid because imaginary part can be only decimal or float no.
#                               but real no. can be int or float 

# but still if we want any int in imaginary then you can follow below rule

c5 = complex(0b1011,0xface)
print(type(c5))
print(c5)

print("\n")
p1=0b1011
p2=0o1234
p3=0xface
print(p1)   # o/p ---> 11
print(p2)   # o/p --->668
print(p3)   # o/p --->64206

#but what if i want o/p in bin oct and hex so follow below
print("\n")
v1=bin(11)
v2=oct(668)
v3=hex(64206)
print(v1,type(v1))   # o/p ---> 0b1011 <class 'str'>
print(v3,type(v2))   # o/p --->0xface <class 'str'>
print(v2,type(v3))   # o/p --->0o1234 <class 'str'>
