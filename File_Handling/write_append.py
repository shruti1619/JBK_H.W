fd=open("newfile.txt","w")  # open file in write mode

data="This is first line\n"
fd.write(data)   # write data to file

data="This is second line\n"
fd.write(data)   # write data to file

fd=open("newfile.txt","a+")  # open file in append and read mode

data=fd.read()   # read entire file content
print("File content before appending:\n",data)
