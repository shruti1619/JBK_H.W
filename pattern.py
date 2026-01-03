n=6
# for rows in range(1,n+1):
#     for cols in range(1,rows):
#         print("* ",end="")
#     print()    
  
# for rows in range(6,1,-1):
#     for cols in range(1,rows):
#         print("* ",end="")
#     print()
    


# for i in range(1, n + 1):
#     # First loop: print spaces
#     for j in range(n - i):
#         print(' ', end='')   # end='' prevents newline

#     # Second loop: print stars
#     for k in range(i):
#         print('*', end='')

#     # Move to the next line after spaces + stars
#     print()
    
    
# for i in range(1, n + 1):
#     # First loop: print spaces
#     for j in range(n - i):
#         print(' ', end='')   # end='' prevents newline
    
#     # Second loop: print stars
#     for k in range(i):
#         print('* ', end='')

#     # Move to the next line after spaces + stars
#     print()


for i in range(n,0,-1):
     # First loop: print spaces
    for j in range(n - i):
        print(' ', end='')   # end='' prevents newline
        
    # Second loop: print stars
    for k in range(i):
        print(' * ', end='')

    # Move to the next line after spaces + stars
    print()

    
    
# height = 5
# for i in range(height, 0, -1):
#     print('*' * i)


# height = 5
# for i in range(1, height + 1):
#     print(' ' * (height - i) + '*' * i)







