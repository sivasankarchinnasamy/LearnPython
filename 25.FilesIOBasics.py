#  File IO Basics
# ----------------------------------------------
# "r" - Open file for reading - (Default Mode)
# "w" - Open a file for writing
# "x" - Create file if not exists
# "a" - Add more content to a file - Append
# "t" - text mode - (Default Mode)
# "b" - Binary mode
# "+" - Read & Write
# ----------------------------------------------

# fP= open("SampleText.txt",'x')  # Creates file if it does not exists
# print(fP.readlines)
# fP.close()

fp = open("D:\Code\LearnPython\SampleText.txt",'r+')
# print(fp.readline()) # Reads only one line
# print(fp.readlines()) # Reads lines 2 & 3 as list of string - Only line 2 & 3 gets printed as above statement takes line 1.
# print(fp.read()) # Reads complete file

# print(fp.read(15))  # Prints first 15 char
# print(fp.read(10))  # Prints next 10 chars
# print(fp.read(10))  # Prints next 10 chars

# for line in fp.read():
#     print(line) # prints line char by char in new line

for line in fp: # Iterate file pointer to read by line
    # print(line) # This prints extra new line character
    print(line, end="")
fp.close()