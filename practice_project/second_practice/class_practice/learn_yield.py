#yield关键字，一般用户生成器

def provider():
    for i in range(0,10):
        print('开始')
        yield i  #相当于return操作，返回数据，并且记录了上一次的数据，下一次继续在此处执行
        print('结束')

p = provider()
print(next(p))
print(next(p))
print(next(p))