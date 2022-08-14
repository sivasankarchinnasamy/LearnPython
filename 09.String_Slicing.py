# String Slicing & other functions

# Defualt when nothing put -> [0:len(str):1]

myStr = "Siva is a good boy"
print("First 4 chars of string: "+ myStr[0:4]) # String starting from 0 (left) to right 4 (excluding 4)
print("Full string: "+myStr[0:len(myStr)])

print("Full string: "+myStr[0:100]) # This will work

# Advanced Slicing
print(myStr[0:4:2]) # From substring 0-3-> Siva -> Select alternate chars in 2. ie-> S
print(myStr[0::2]) # From full string alternate chars in 2


# -ve indices
#--------------------------------------------------
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |10 |11 |
#--------------------------------------------------
# | M | o | n | t | y |   | P | y | t | h | o | n |
#--------------------------------------------------
# |-12|-11|-10|-9 |-8 |-7 |-6 |-5 |-4 |-3 |-2 |-1 | 
#--------------------------------------------------

str1 = "Monty Python"
print(str1[-12:-10]) # Start @ -12 and go b4 -10 -> -12 & -11 printed

# String reversal
print(str1[::-1]) # First reverses string and gets each char
print(str1[::-2])  # First reverses string and gets each alternate char

