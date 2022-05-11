from selenium import webdriver
from selenium.webdriver.remote.webdriver import  WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

class SP1:
    # 爬取指定一集
    def __init__(self,url):
        print('爬取图片')
        self.url = url
    def sp(self):
        ret = []
        option = webdriver.FirefoxOptions()
        option.add_argument("-headless")
        option.set_preference('permissions.default.image', 2)
        option.set_preference('permissions.default.stylesheet',2)
        driver = WebDriver(
            command_executor='http://192.168.40.62:4444/wd/hub',
            options=option,
            desired_capabilities=DesiredCapabilities.FIREFOX
        )
        driver.set_page_load_timeout(10)
        driver.set_script_timeout(10)
        try:
            driver.get(self.url)
            print(driver.title)

            # 这里直接等待一会，等待章节部分刷出来
            time.sleep(1)
            # 这是要滚动一下才能触发下面的图片
            for i in range(0,1000):
                driver.execute_script('window.scrollTo(0,'+str(i)+')')
                time.sleep(0.003)

            es = driver.find_elements(by=By.XPATH,value='//li/img')
            
            print(len(es))
            for e in es:
                url2 = e.get_attribute('data-src')
                # print(url2)
                ret.append(url2)
        except :
            print("xpath error")
        finally:
            driver.quit()
        return ret
if __name__=='__main__':  
    s = SP1('https://copymanga.org/comic/r402/chapter/664974f8-92a6-11e9-8d6f-024352452ce0')
    ret = s.sp()
    print(ret)