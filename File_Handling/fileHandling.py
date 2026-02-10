# fd=open("db.txt","r")
# print("\nFIle opened successfully")

with open("db.txt","r") as fd:
    # no need to close file manually, it will close automatically
    print("\nFile opened successfully using with statement")
    print(fd.tell())  # it will return current position of file pointer
    
    data=fd.read(10)
    print("\nit is getting 10 characters :",data)
    print(fd.tell())  # it will return current position of file pointer after #                   reading 10 characters
    fd.seek(5)        # it will set the file pointer to 5th position
    print(data)
    print(fd.tell())  # it will return current position of file pointer after #                   setting to 5th position