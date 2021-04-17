'''
range用法
'''
# result =0
# for i in range(1,101):
#     # print(i)
#     result = result +i
# print(result)

result =0
for i in range(1,101,4):
    print(i)
    result = result +i
print(result)

'''
猜数字游戏
'''
# import random
# person_number=0
# computer_number=random.randint(1,101)
# print(computer_number)
#
# while True:
#     person_number=int(input('请输入数字\n'))
#     if computer_number>person_number:
#         print('大一点')
#     elif computer_number<person_number:
#         print('小一点')
#     else:
#         print('猜对啦')
#         break

