from time import sleep

from  selenium import webdriver
from selenium.webdriver.common.by import By


class PositionedElement():
    def search_xpath(self):
        self.drvier =webdriver.Chrome()
        self.drvier.get('https://www.baidu.com/')
        self.drvier.maximize_window()
        #通过id定位输入框
        a = self.drvier.find_element(By.ID,'kw').send_keys('元素定位')
        # 通过class定位输入框
        b = self.drvier.find_element(By.CLASS_NAME, 's_ipt')
        # 通过name定位输入框
        c = self.drvier.find_element(By.NAME, 'wd')
        #通过xpath定位输入框
        d = self.drvier.find_element(By.XPATH,'//*[@id="kw"]')
        e = self.drvier.find_element(By.XPATH, '//*[@class="s_ipt"]')
        f = self.drvier.find_element(By.XPATH, '//*[@name="wd"]')

        #通过xpath定位“百度一下”
        #$x('//*[@id="s_btn_wr"]')
        g = self.drvier.find_element(By.XPATH,'//*[@class="bg s_btn_wr"]').click()

        # 通过xpath定位“图片”
        m = self.drvier.find_element(By.XPATH, '//*[@class="s_tab_inner"]/a[3]').click()

    def search_css_selector(self):
        self.drvier = webdriver.Chrome()
        self.drvier.get('https://www.baidu.com/')
        self.drvier.maximize_window()

        #通过css_selector--class定位“百度一下”   .class
        #x('.btn self-btn bg s_btn')
        q= self.drvier.find_element(By.CSS_SELECTOR,'#kw').send_keys('元素定位')
        # CSS_SELECTOR如果属性有空格，换成.（点号）
        h = self.drvier.find_element(By.CSS_SELECTOR,'.bg.s_btn_wr')
        i= self.drvier.find_element(By.CSS_SELECTOR, '[class="bg s_btn_wr"]').click()

        # 通过css_selector--id定位“百度一下”     #id
        j = self.drvier.find_element(By.CSS_SELECTOR, '#su')
        k = self.drvier.find_element(By.CSS_SELECTOR, '[id=su]')

        # 通过css_selector定位“网页”
        l = self.drvier.find_element(By.CSS_SELECTOR, '.s_tab_inner b')

        #通过css_selector定位“资讯”----a:nth-child(number）,number代表：a元素父级元素的第几个孩子
        #空格代表id='s_tab_inner'下的所有元素
        sleep(2)
        m = self.drvier.find_element(By.CSS_SELECTOR, '.s_tab_inner  a:nth-child(2)')
        # >代表id='s_tab_inner'下的（一级）子元素
        n = self.drvier.find_element(By.CSS_SELECTOR, '.s_tab_inner>a:nth-child(2)')
        sleep(2)
        # 通过css_selector定位“更多”  a:nth-last-child(number）,number代表：a元素父级元素的倒数第几个孩子
        o = self.drvier.find_element(By.CSS_SELECTOR, '.s_tab_inner a:nth-last-child(1)').click()
        sleep(2)

        # 通过css_selector定位“地图”  a:nth-last-child(number）,number代表：a元素父级元素的倒数第几个孩子
        p = self.drvier.find_element(By.CSS_SELECTOR, '.s_tab_inner a:nth-last-child(2)')

if __name__ =='__main__':
    a = PositionedElement()
    # a.search_xpath()
    a.search_css_selector()






