fp=open("D:\Code\LearnPython\SampleText.txt")
print(fp.tell()) # Tells the position of pointer; returns location as int
print(fp.readline())
fp.seek(0) # puts file pointer at 0 position
print(fp.tell())
print(fp.readline())
print(fp.tell())
print(fp.readline())
fp.close()