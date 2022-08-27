# Handle both read & write

'''
'w' vs 'a' mode :
'w' mode - write() func cleans file every time and writes to file; we cannot use read() func in this mode
'a' mode - write() func appends content to end of file; we cannot use read() func in this mode
'r+' mode - write() func works as append, i.e write() does not clean file; we can use read() func in this mode
'''
fp = open("D:\Code\LearnPython\SampleText.txt","a")
fp.write("\nThis is an append statement")
fp.close()

fp = open("D:\Code\LearnPython\SampleText.txt","w")
fp.write("\nThis is an write statement") # Cleans file first then adds this line
a = fp.write("\nThis is another write statement") # No: of char written
print("Number of chars written: ",a)
fp.close()


fp = open("D:\Code\LearnPython\SampleText.txt","r+") # Best mode for file I/O
print(fp.read())
fp.write("\nThis is the third statement")
print(fp.read())

