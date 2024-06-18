
#练习3-1：姓名　将一些朋友的姓名存储在一个列表中，并将其命名为names。依次访问该列表中的每个元素，从而将每个朋友的姓名打印出来。
list_name = ['Zhang', 'Liu', 'Li', 'Zhao']
print(list_name[0])
print(list_name[1])
print(list_name[2])
print(list_name[3])

#练习3-2：问候语　继续使用练习3-1中的列表，但不打印每个朋友的姓名，而为每人打印一条消息。每条消息都包含相同的问候语，但抬头为相应朋友的姓名。
print(f'Hello {list_name[0]}, How are you?')
print(f'Hello {list_name[1]}, How are you?')
print(f'Hello {list_name[2]}, How are you?')
print(f'Hello {list_name[3]}, How are you?')

#练习3-3：自己的列表　想想你喜欢的通勤方式，如骑摩托车或开汽车，并创建一个包含多种通勤方式的列表。根据该列表打印一系列有关这些通勤方式的宣言，下面是一个例子。
commuting_mode = ['walk', 'bike', 'subway', 'public transit', 'taxi']
print(f'I {commuting_mode[0]}, {commuting_mode[1]}, take the {commuting_mode[2]} to work every day')