
# 第三章 列表简介
bicycles = ['trek', 'connodale', 'redline', 'specialized']

# 访问数组元素
print(bicycles)
print(bicycles[0])
print(bicycles[0].title())

# 访问列表的最后一个元素使用下标：-1
print(bicycles[-1])

# 在字符串中输出列表
print(f"My first bicycle was a {bicycles[0].title()}.")

# 修改，添加，删除列表
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles)
motorcycles[0] = 'honda'

motorcycles.append('ducati')
print(motorcycles)
del motorcycles[-1]

# 在指定位置插入元素
motorcycles.insert(0, 'ducati')
print(motorcycles);

# 删除指定下标的元素
del motorcycles[0]
print(motorcycles);

# 第二种方法删除元素，pop()，该方法会删除数组中的最后一个元素，并将它作为返回值返回
popped_motorcycles =motorcycles.pop();
print('弹出的值：' + popped_motorcycles)
print('数组的值：')
print(motorcycles)
print(f'The last element is {popped_motorcycles}')
motorcycles.append(popped_motorcycles)

# pop方法还可以传入一个参数，用来删除指定的下标的元素
first_motorcycles = motorcycles.pop(0)
print('弹出的值：' + first_motorcycles)
print('数组的值：')
print(f'The first element is {first_motorcycles}')
motorcycles.insert(0, first_motorcycles)

# 第三种方法是按照指定的元素值删除元素，但只能删除一个
too_expensive = "ducati";
motorcycles.append(too_expensive)
motorcycles.remove(too_expensive)
print(f'{too_expensive.title()} is too expensive for me')