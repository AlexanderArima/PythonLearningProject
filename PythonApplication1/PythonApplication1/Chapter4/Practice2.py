
for item in range(1,21):
    print(item)

# 打印1-1000000，并输出最大值、最小值、总和
numbers = list(range(1, 1000001))
#for item in numbers:
    #print(item)
print(f"数组的最大值：{max(numbers)}")
print(f"数组的最小值：{min(numbers)}")
print(f"数组的总和：{sum(numbers)}")

# 打印奇数
num2 = list(range(1, 20, 2))
print(num2)

# 打印3-30内能被3整除的数
num3 = list(range(3, 31, 3))
print(num3)

# 打印1-10的立方
num4 = list(range(1, 11))
for item in num4:
    print(item ** 3)
    
# 立方解析
num5 = [value ** 3 for value in range(1, 11)]
print(num5)

# 使用元祖
num6 = ("青椒肉丝", "番茄鸡蛋", "麻婆豆腐", "清蒸鲈鱼", "红烧肉")
print(num6)

# 尝试修改元祖中的元素
# num6[0] = "鱼香肉丝";    # 元祖中的元素不能修改
# print(num6)

# 给元祖重新赋值
num6 =  ("青椒肉丝", "番茄鸡蛋", "麻婆豆腐", "清蒸鲈鱼", "鱼香肉丝")
print(num6)