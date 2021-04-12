import sys

# import sys
# sys.path.append("../LearnCode/PracticeProject/SecondPractice/ClassPractice")

import pytest

# from PracticeProject.SecondPractice.ClassPractice.Calculator import Calculator

#from .Calculator import  calculator
# from PracticeProject.SecondPractice.ClassPractice.Calculator import calculator
# import sys
#print(f'目录：{sys.path}')
from PracticeProject.SecondPractice.ClassPractice.Calculator import calculator


class TestCal:

    #方法级别
    # def setup(self0):
    #     print('开始计算')
    # def teardown(self):
    #     print('结束计算')

    #类级别
    def setup_class(self0):
        print('开始计算')
        print(f'目录：{sys.path}')
    def teardown_class(self):
        print('结束计算')

    #pytest.mark.parametrize():参数化
    @pytest.mark.parametrize('a,b,expect',[(1,2,3),(2,3,5)],ids=['int1','int2'])
    def test_add_int(self,a,b,expect):
        cal = calculator()
        assert expect == cal.add(a,b)

    @pytest.mark.parametrize('a,b,expect',[(0.2,0.3,0.5),(0.1,0.2,0.3)],ids=['float1','float2'])
    def test_add_float(self,a,b,expect):
        cal = calculator()
        #round（）：保留几位小数
        assert expect == round(cal.add(a,b),2)

    def test_div(self):
        cal =calculator()
        #python捕获指定异常：
        # try:
        #     cal.div(1,0)
        # except ZeroDivisionError:
        #     print('除数为0')

        #python捕获所有异常：
        # try:
        #     cal.div(1,'hh')
        # except :
        #     print('除数为0')

        #pytest捕获异常：
        with pytest.raises(ZeroDivisionError):
            cal.div(1, 0)


