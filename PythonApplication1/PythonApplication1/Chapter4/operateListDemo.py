

magicians = ['alice', 'david', 'carolina']
for item in magicians:
    print(item)

for item in magicians:
    print(f"{item.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {item.title()}.\n")
    
print("Thank you everyone, that was a great magic show!")

for value in range(1,6):
    print(value)

numbers = list(range(1, 10))
print(numbers)

# 依次打印2的平方的数组
squares = []
for value in range(1,11):
    squares.append(2 ** value)
print(squares) 
print(f"最大值：{max(squares)}")
print(f"最小值：{min(squares)}")
print(f"总和：{sum(squares)}")

# 列表解析
squares2 = [value ** 2 for value in range(1,11)]
print(squares2)








