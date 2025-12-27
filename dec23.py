jay=22
viru=22
basanti=21
print(bool(jay))        #o/t: True
print((viru >=jay))       #o/t: True
print((basanti>viru and basanti > jay))      #o/t: False
print((basanti<viru or jay==viru))      #o/t: True
print((not(basanti<viru)))      #o/t: False
print(bool(jay - viru))      #o/t: False
print(bool(jay + basanti - viru))      #o/t: True
print((jay > basanti or viru <basanti))  #o/p: True
print((not(jay<basanti and jay<viru)))  #o/p: True

# COMPARISON OPERATORS
a = 20
a += 30
print(a)

b=0
for i in range(11):
    b += i
print(i)
