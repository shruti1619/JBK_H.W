try:
    fd=open("db.txt","r")
    print("\nFIle opened successfully")
    # for i in fd:    # it will read line by line
    #     print(i)
    
    # data=fd.read()   # it will read entire file content
    # print(data)

    data1=fd.read(10)
    print("\nit is getting 10 word :",data1)  
    
    data2=fd.readline()  # it will read only one line
    print("\nReading only one line :",data2)
    
    data3=fd.readlines()  # it will read all lines and store in list
    print("\nReading all lines and store in list :",data3)

except FileNotFoundError as e:
    print("check file name carefully :",e)
    
finally:
    fd.close()       # it will execute always whether exception occurs or not
    print("\nFile closed successfully\n")