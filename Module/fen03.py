from collections import defaultdict,namedtuple,OrderedDict,deque,ChainMap
d={'a':2}
d['a'] += 1
print(d)

d.setdefault('b',0)
d['b'] += 1
print(d)

# d['b'] += 1   it will give key error if key not present
d1=defaultdict(int)
d1['b'] += 1
d1['a'] += 2
print(d1)

d2=defaultdict(list)
d2['marks'].append(90)
print(d2)

# already story keys in order of insertion but still we can use OrderedDict
d3={}
d3['name']='John'
d3['roll']=101
d3['marks']= [90,85,88]
print(d3)

od=OrderedDict()
od['name']='John'
od['roll']=101
od['marks']= [90,85,88]
print(od)

student= namedtuple('Student',['name','roll','marks'])
p1 = student('John',101,96)  
print(p1.name)
print(type(p1))

q=deque()
q.append(10)
q.append(20)    
q.appendleft(5)

print(q)

d4= {'a':1,'b':2}
d5= {'b':3,'c':4}
cm=ChainMap(d4,d5)
print(cm)
