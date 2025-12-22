s1='shruti'
s2="morey"
print(s1+s2)  #concatenation of two string provids o/t shrutimorey
#print(s1+10)  #TypeError: can only concatenate str (not "int") to str
# var=10
# print(s1+var) #TypeError: can only concatenate str (not "int") to str

list1=[1,2,3]
list2=[4,5,6]
# 1. To check Addition of str and list
#print(s1+list1) #TypeError: can only concatenate str (not "list") to str

# 2. To check Addition of list and list
print(list1+list2)  #o/t: [1, 2, 3, 4, 5, 6]

# 3. To check addition of list and int
#print(list1+10.1)  #TypeError: can only concatenate list (not "int") to list

'''complex1=2+3j
complex2=4+5j
print(complex1+complex2)   #o/t: (6+8j)
print(complex1*complex2)   #o/t: (-7+22j)
print(complex1-complex2)   #o/t: (-2-2j)
#print(complex1/complex2)   #o/t: (0.61-0.08j)
#print(complex1+s1)      #TypeError: unsupported operand type(s) for +: 'complex' and 'str'
print(complex1+10)     #o/t: (12+3j)
#print(complex1+list1)   #TypeError: unsupported operand type(s) for +: 'complex' and 'list'
'''
t1=(1,2,3)
t2=(4,5,6)
print(id(t1))  #2066259766512
# 1.To check additon of tuples
print(t1+t2)  #o/t: (1, 2, 3, 4, 5, 6)
print(id(t1+t2))  #2045124649472
print(id(t1))  #2066259766512
# 2.To check addition of tuple and int
#print(t1+10)  #TypeError: can only concatenate tuple (not "int") to tuple
# 3.To check addition of tuple and list
#print(t1+list1)  #TypeError: can only concatenate tuple (not "list") to tuple
# 4. To check addition of tuple and str
#print(t1+s1)  #TypeError: can only concatenate tuple (not "str") to tuple

'''set1={1,2,3,6}
set2={4,5,6}
#print(set1 + set2) #TypeError: unsupported operand type(s) for +: 'set' and 'set'
print(set1.union(set2))  #o/t: {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))  #o/t: set(6)
#print(set1+10)  #TypeError: unsupported operand type(s) for +: 'set' and 'int'
#print(set1+s1)  #TypeError: unsupported operand type(s) for +: 'set' and 'str'
#print(set1+list1)  #TypeError: unsupported operand type(s) for +: 'set' and 'list'     
print(set1 - set2)  #o/t: {1, 2, 3}
print(set2 - set1)  #o/t: {4, 5}
print(set1+t1)    #TypeError: unsupported operand type(s) for +: 'set' and 'tuple'
'''
dict1={1:"apple",2:"banana",3:"mango"}
dict2={4:"brocoli",5:"bringal",6:"coliflower"}
#print(dict1 + dict2)  #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print(dict2)  #o/t: None 
print(dict1)
a=dict1.update(dict2)
print(a)  #o/t: None
print(dict1)  #o/t: {1: 'apple', 2: 'banana', 3: 'mango', 4: 'brocoli', 5: 'bringal', 6: 'coliflower'}
print(dict2)  #o/t: {4: 'brocoli', 5: 'bringal', 6: 'coliflower'}
print(dict1.update({7:"grapes"}))  #o/t: None
print(dict1)  #o/t: {1: 'apple', 2: 'banana', 3: 'mango', 4: 'brocoli', 5: 'bringal', 6: 'coliflower', 7: 'grapes'}
#print(dict1+10)  #TypeError: unsupported operand type(s) for +: 'dict' and 'int'
#print(dict1+s1)  #TypeError: unsupported operand type(s) for +: 'dict' and 'str'
#print(dict1+list1)  #TypeError: unsupported operand type(s) for +: 'dict' and 'list'   
#print(dict1+t1)    #TypeError: unsupported operand type(s) for +: 'dict' and 'tuple'


