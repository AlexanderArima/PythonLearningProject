
#练习3-4：嘉宾名单　如果你可以邀请任何人一起共进晚餐（无论是在世的还是故去的），你会邀请哪些人？请创建一个列表，其中包含至少三个你想邀请的人，然后使用这个列表打印消息，邀请这些人来与你共进晚餐。
list_guest = ['An', 'Bi', 'Cai', 'Du']
print(f"I'm going to invite {list_guest[0].title()}, {list_guest[1].title()}, {list_guest[2].title()}, {list_guest[3].title()} to a banquet")

#练习3-5：修改嘉宾名单　你刚得知有位嘉宾无法赴约，因此需要另外邀请一位嘉宾。
removed_guest = 'An'
list_guest.remove(removed_guest)
print(f'The {removed_guest} can not attend the banquet')
append_guest = 'Fa'
list_guest.append(append_guest)
print(f"I'm going to invite {list_guest[0].title()}, {list_guest[1].title()}, {list_guest[2].title()}, {list_guest[3].title()} to a banquet")

#练习3-6：添加嘉宾　你刚找到了一个更大的餐桌，可容纳更多的嘉宾。请想想你还想邀请哪三位嘉宾。
print('I find a bigger desk')
name1 = 'Gao'
name2 = 'He'
name3 = 'Jin'
list_guest.insert(0, name1)
list_guest.insert(2, name2)
list_guest.append(name3)
print(f'{name1}, Could you want attend the banquet?')
print(f'{name2}, Could you want attend the banquet?')
print(f'{name3}, Could you want attend the banquet?')
print(list_guest)

#练习3-7：缩减名单　你刚得知新购买的餐桌无法及时送达，因此只能邀请两位嘉宾。
name4 = 'Bi'
name5 = 'Cai'
print(f'I can only invite {name4} and {name5} to the banquet')
popped_guest = list_guest.pop(0)
print(f'I am sorry {popped_guest} can not attend the banquet')
popped_guest = list_guest.pop(1)
print(f'I am sorry {popped_guest} can not attend the banquet')
popped_guest = list_guest.pop(-1)
print(f'I am sorry {popped_guest} can not attend the banquet')
popped_guest = list_guest.pop(-1)
print(f'I am sorry {popped_guest} can not attend the banquet')
popped_guest = list_guest.pop(-1)
print(f'I am sorry {popped_guest} can not attend the banquet')
print(f'{list_guest[0]} and {list_guest[1]}, you are still on the invitation list')
del list_guest[0]
del list_guest[0]
print(list_guest)