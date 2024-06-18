
# 练习3-8：放眼世界　想出至少5个你渴望去旅游的地方。
list_city = ['WeiHai', 'DaLian', 'DaLi', 'MeiShan', 'TaiBei']
print(list_city)
print(sorted(list_city))
print(list_city)
print(sorted(list_city, reverse=True))
print(list_city)

print('使用reverse()永久性改变列表排序')
list_city.reverse()
print(list_city)

print('再次使用reverse()让列表顺序还原')
list_city.reverse()
print(list_city)

print('使用sort()永久性改变列表排序，让它正序排序')
list_city.sort()
print(list_city)

print('使用sort()永久性改变列表排序，让它倒序排序')
list_city.sort(reverse=True)
print(list_city)
