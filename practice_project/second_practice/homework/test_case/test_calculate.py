import pytest
import allure
from practice_project.second_practice.homework.calculate import Calculate
from practice_project.second_practice.homework.get_datas import get_datas

@pytest.fixture(scope='class')
def cal():
    print('开始计算')
    cal =Calculate()
    yield cal
    print('结束计算')

@allure.feature('测试计算器')
class TestCalculate:
    @pytest.mark.parametrize('a,b,expect',get_datas()['add_int']['datas'],ids =get_datas()['add_int']['ids'])
    @allure.story('测试整型相加')
    def test_add_int(self,cal,a,b,expect):
        # cal = Calculate()
        assert expect == cal.add(a,b)

    @pytest.mark.parametrize('a,b,expect', get_datas()['add_float']['datas'], ids=get_datas()['add_float']['ids'])
    @allure.story('测试浮点型相加')
    def test_add_float(self, cal, a, b, expect):
        # cal = Calculate()
        assert expect == round(cal.add(a, b),1)

    @pytest.mark.parametrize('a,b,expect', get_datas()['div_int']['datas'], ids=get_datas()['div_int']['ids'])
    @allure.story('测试整型相除')
    def test_div_int(self, cal, a, b, expect):
        # cal = Calculate()
        assert expect == cal.div(a, b)

    @pytest.mark.parametrize('a,b,expect', get_datas()['div_float']['datas'], ids=get_datas()['div_float']['ids'])
    @allure.story('测试浮点型相除')
    def test_div_float(self, cal, a, b, expect):
        # cal = Calculate()
        assert expect == round(cal.div(a, b), 2)

    @pytest.mark.parametrize('a,b', get_datas()['div_zero']['datas'], ids=get_datas()['div_zero']['ids'])
    @allure.story('测试被除数为0')
    def test_div_zero(self, cal, a, b):
    #python捕获指定异常：
        try:
            cal.div(a,b)
        except ZeroDivisionError:
            print('除数为0')








