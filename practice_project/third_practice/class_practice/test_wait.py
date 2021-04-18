"""
1.强制等待 ：time.sleep---设置固定的线程休眠时间。
2.隐式等待：self.driver.implicitly_wait(3)---隐式等待是全局的是针对所有元素，设置等待时间如3秒，如果3秒内出现，则继续向下，否则抛异常。可以理解为在3秒以内，不停刷新看元素是否加载出来。
3.显示等待： 显示等待需要用到两个类：WebDriverWait和expected_conditions两个类，WebDriverWait()中的until()和until_not()方法以及expected_conditions类

各种类，达到某种条件，返回True和False（常用：1.presence_of_element_located：判断某个元素是否被加到了DOM树里，并不代表该元素一定可见 2.visibility_of_element_located
判断某个元素是否可见，可见代表元素非隐藏，并且元素的宽和高都不等于0）。---显示等待必须在每个需要等待的元素前面进行声明。

链接：https://blog.csdn.net/Wuli_SmBug/article/details/82053372?utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control&dist_request_id=1329188.13191.16178947135333697&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7EBlogCommendFromMachineLearnPai2%7Edefault-1.control
"""


from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import By
from  selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestWait:
     def setup(self):
         self.driver = webdriver.Chrome()
         self.driver.get('https://ceshiren.com')
         self.driver.maximize_window()
         #隐式等待：全局的，默认每隔0.5秒扫一次
         self.driver.implicitly_wait(3)
     def test_wait(self):
         #强制等待
         #sleep (2)
         self.driver.find_element_by_xpath('//*[@class="active"]').click()
         #显示等待:也可以自己写条件--#设置等待
            # wait = WebDriverWait(driver,10,0.5)
            # #使用匿名函数
            # wait.until(lambda diver:driver.find_elements('By.xpath,'//*[@class="d-button-label"]'))>=1

         WebDriverWait(self.driver,10).until(expected_conditions.presence_of_all_elements_located((By.XPATH,'//*[@class="d-button-label"]')))
         self.driver.find_element_by_xpath('//*[@class="d-button-label"]').click()
         #sleep(2)

     def teardown(self):
         self.driver.quit()

