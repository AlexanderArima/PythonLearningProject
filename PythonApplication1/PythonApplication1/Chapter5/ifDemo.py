
# 使用if语句，如果品牌是首字母大写，则输出首字母大写，否则输出首字母小写
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# 检查元素是否包括在列表中
cars = ['audi', 'bmw', 'subaru', 'toyota']
if 'toyota' in cars:
    print('toyota in cars')
else:
    print('toyota not in cars')
    
# 检查元素是否不包括在列表中
cars = ['audi', 'bmw', 'subaru', 'toyota']
if 'dongfeng' not in cars:
    print('dongfeng not in cars')
else:
    print('dongfeng in cars')

# 使用if-elif-else语句，根据年龄输出门票价格
age = 60
price = 0
if age <= 4:
    price = 0
elif age <= 18:
    price = 25
elif age <= 65:
    price = 40
else:
    price = 20
print(f'your admission cost is ${price}')

# 使用if语句，根据顾客点的配料打印一条消息，如果顾客点了配料，则打印一条消息，否则打印一条不同的消息
requested_toppings = ['mushrooms', 'french fries', 'green peppers']
if 'mushrooms' in requested_toppings:
    print('Adding mushrooms')
if 'extra cheese' in requested_toppings:
    print('Adding extra cheese')
if 'green peppers' in requested_toppings:
    print('Adding green peppers')
    
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f'Adding {requested_topping}')
    print('\nFinished making your pizza!')
else:
        print('Are you sure you want a plain pizza?')