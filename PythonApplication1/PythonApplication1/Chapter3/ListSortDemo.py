
# 列表排序，sort方法是永久性的
list_cars = ['bmw', 'audi', 'toyota', 'subaru']
list_cars.sort()
print(list_cars)

# 倒序排序
list_cars.sort(reverse=True)
print(list_cars)
list_cars = ['bmw', 'audi', 'toyota', 'subaru']

# 非永久性的排序
print('非永久性的排序：')
print(sorted(list_cars))
print('原列表：')
print(list_cars)

# 让列表倒序，永久性
print('让列表倒序：')
list_cars.reverse()
print(list_cars)
list_cars.reverse()
print(list_cars)

# 获取列表元素个数
print(f'数组长度：{len(list_cars)}')