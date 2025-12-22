#bytes and bytearray in python
b=bytes(5)
print(type(b))

b1=b'hello'
print(type(b1))

ba=bytearray("hello world","utf-8")
print(type(ba))
ba.append(66)
print(ba)
ba.replace(b'h',b'H')
print(ba)

var=None
print(var)
print(type(var))

print(print(print("python223")))