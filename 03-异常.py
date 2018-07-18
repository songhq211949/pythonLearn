
#异常的表现，哲学无用为大用
try:
    print("---test1----")
    a=1/0
    open("123.txt","r")
    print("----test1----")
except FileNotFoundError :
    print("没有文件找到")
except Exception as yichang:
    print(yichang)
print("处理异常之后的方法")