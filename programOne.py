triSize = int(input('Enter triangle size: ')) 

# Checks the user input, in case it is negative.
if(triSize <= 0):
  print('Please enter a value > 0.  Exiting...\n')

# Printing first row
print('*')

# Triangles that have a size of 3 or < will not need spaces
row = 1 
if(triSize < 4): 
  # Iterating through number of rows until end is reached
  while(row < triSize):
    # Number of asterisks is equal to current row + 1
    print('* ' * (row + 1))
    row += 1
# Triangles with a size > 3 will contain spaces between the asterisks
else:
  numSpaces = 1
  # Iterating through middle rows where the number of spaces increases by 2 each iteration
  while(row < triSize - 1): 
    print('*' + ' ' * numSpaces + '*')
    numSpaces += 2
    row += 1
  # Printing the bottom row 
  print('* ' * (row + 1))