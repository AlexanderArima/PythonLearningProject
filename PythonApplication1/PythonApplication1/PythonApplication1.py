
msg = "Hello World";
print(msg);

num = 1;
print("num的类型：" + str(type(num)))
num = 10.1;
print("num的类型：" + str(type(num)))
num = "abc";
print("num的类型：" + str(type(num)))

# 在输出单引号时，在前面加一个反斜线进行转义即可
print("I\'m a coder")

# 在输入一个很长的字符串时可以使用反斜线进行换行处理
print("I\'m a coder \
I\'m a human")

# 使用三个双引号或单引号可以表示一个长字符串，被它包含的字符串可以是单引号或双引号，字符串换行，输出的结果也是换号的
print("""I'm a coder
I'm a human""")

# 当需要输出反斜线时，在字符串的前面加一个r
print(r"E:\\PythonLearningProject");