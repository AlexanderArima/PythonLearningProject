
num = list(range(1, 11))
print(num[3:])  # 从第四个元素开始打印到最后

# 遍历切片
# 访问前三个元素
for item in num[:3]:
    print(item)
    
# 模拟分页访问
num2 = list(range(1, 101))

# 访问第1-10个元素
print(num2[0 : 10])

# 访问第11-20个元素
print(num2[10: 20])

# 复制列表
num3 = num2[:]
print(num3)