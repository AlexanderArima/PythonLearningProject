
num = list(range(1, 11))
print(num[3:])  # �ӵ��ĸ�Ԫ�ؿ�ʼ��ӡ�����

# ������Ƭ
# ����ǰ����Ԫ��
for item in num[:3]:
    print(item)
    
# ģ���ҳ����
num2 = list(range(1, 101))

# ���ʵ�1-10��Ԫ��
print(num2[0 : 10])

# ���ʵ�11-20��Ԫ��
print(num2[10: 20])

# �����б�
num3 = num2[:]
print(num3)