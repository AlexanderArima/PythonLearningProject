
# ʹ��if��䣬���Ʒ��������ĸ��д�����������ĸ��д�������������ĸСд
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# ���Ԫ���Ƿ�������б���
cars = ['audi', 'bmw', 'subaru', 'toyota']
if 'toyota' in cars:
    print('toyota in cars')
else:
    print('toyota not in cars')
    
# ���Ԫ���Ƿ񲻰������б���
cars = ['audi', 'bmw', 'subaru', 'toyota']
if 'dongfeng' not in cars:
    print('dongfeng not in cars')
else:
    print('dongfeng in cars')

# ʹ��if-elif-else��䣬�������������Ʊ�۸�
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

# ʹ��if��䣬���ݹ˿͵�����ϴ�ӡһ����Ϣ������˿͵������ϣ����ӡһ����Ϣ�������ӡһ����ͬ����Ϣ
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