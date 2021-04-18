# #定义函数
# def function1 (a,b,c):
#     """
#     函数的作用
#     :return:
#     """
#     #缩进快捷键：tab键
#     #pycharm 快捷键 ctrl+d:复制一行
#     print('这是一个函数',a)
#     print(f'这是一个函数{b}')
#     print('这是一个函数',c)
#     return  0
# #函数的调用
# function1(4,5,6)

# '''
# 默认参数
#默认参数在定义函数的时候使用k=v
# '''
# def function2(a=1):
#     print(a)
#
# function2(2)


'''
关键字参数要放在位置参数之后
关键字参数在调用函数的时候使用k=v
'''

# def function3(a,b,c,d):
#     print(f'这是一个关键字{a}')
#     print(f'这是一个关键字{b}')
#     print(f'这是一个关键字{c}')
#     print(f'这是一个关键字{d}')
#
# function3(1,c=2,d=3,b=4)

'''
lambda:定义简单的函数
'''

function4=lambda x,y:x+y
print(function4(2,4))

#相当于

def function5(x,y):
    return  x+y
print(function5(2,4))
