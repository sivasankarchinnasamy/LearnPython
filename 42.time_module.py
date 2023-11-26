import time

print(time.time()) # returns time as tiks(seconds)
print(time.localtime(time.time())) # returs local time as tuple
print(time.asctime(time.localtime(time.time()))) # returns local time in readble string format
time.sleep(2) # program execution stops for 2 seconds
