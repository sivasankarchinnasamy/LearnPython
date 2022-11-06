# No need to close the file when using With Block
with open("D:\Code\LearnPython\SampleText.txt") as fp:
    print(fp.readline())
