
# 以特殊方式跟管理员打招呼
list_user=['admin', 'aaa', 'bbb', 'ccc', 'ddd']
user_name = 'admin'
for user in list_user:
    if user_name not in list_user:
        # 如果用户名不在列表中，打印消息
        print('Sorry,you have not been registered yet.')
        break;
    
    if 'admin' == user_name:
        print('Hello admin,would you like to see a status report?')
    else:
        print(f'Hello {user_name},thank you for logging in again.')
    break

# 检查用户名
current_users = ['admin', 'aaa', 'bbb', 'ccc', 'ddd', '微风', '夏天']
new_users = ['AAA', 'eee', 'fff', 'ggg', 'admin', '微风', '冬天']
print('\n列表循环开始')
for new_user in new_users:
    for current_user in current_users:
        # 将用户名转换为小写，然后进行比较
        flag = '0'
        if new_user.lower() == current_user.lower():
            flag = '1'
            break;
     
    # 内层循环结束后，如果用户名已被使用，打印一条消息
    if flag == '1':
        print(f'{new_user}，已被使用')
    else:
        print(f'{new_user}，尚未被注册');

print('列表循环完毕\n')

# 序数
list_num = list(range(1, 11))
for num in list_num:
    if num == 1:
        print('1st')
    elif num == 2:
        print('2nd')
    elif num == 3:
        print('3rd')
    else:
        print(f'{num}th')
print('循环完毕\n')