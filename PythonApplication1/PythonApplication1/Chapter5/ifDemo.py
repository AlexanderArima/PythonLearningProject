
# 使用if语句，如果品牌是首字母大写，则输出首字母大写，否则输出首字母小写
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())