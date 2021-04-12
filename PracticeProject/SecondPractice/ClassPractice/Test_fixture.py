import pytest

#pytest.fixture(autouse=false)（默认）:只给加了fixture的方法执行，pytest.fixture(autouse=True):全部方法执行
#@pytest.fixture(autouse=True)
#@pytest.fixture(scope='module'):作用域为模块级别

@pytest.fixture()
def login():
    print('这里是登陆操作')
    token = 'sbjcd, hc'
    #yield:激活了teardown操作
    yield token
    print('这里是登出操作')
@pytest.fixture()
def conntectdb():
    print('这里是连接数据库')

def test_search(login):
    print('搜索')
def test_cart(login):
    print('购物车')
#通过名字直接调用,可以再方法里打印返回值,多个fixture的时候，按照传入顺序依次执行
# def test_order(login,conntectdb):
#      print(login)
#      print('下单')

#通过装饰器调用,无法打印返回值（返回的是方法的内存地址，表示调用了）
# @pytest.mark.usefixtures('login')
# def test_order():
#     print(login)
#     print('下单')