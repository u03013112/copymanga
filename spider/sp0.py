from selenium import webdriver
from selenium.webdriver.remote.webdriver import  WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

class SP0:
    # name获得请在 https://copymanga.org/ 点击感兴趣的作品后获得uri后缀
    def __init__(self,name):
        print('爬取目录的类,name是',name)
        self.url = 'https://copymanga.org/comic/'+name
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
            # driver.get("http://www.python.org")
            print(driver.title)

            # 这里直接等待一会，等待章节部分刷出来
            time.sleep(3)
            # iframe = driver.find_element_by_xpath("//iframe[@id='play']")
            # wait(driver, 10).until(
            #     EC.presence_of_element_located(iframe)
            # )
            
            es = driver.find_elements(by=By.XPATH,value='//div[@id="default全部"]/ul/a')
            
            print(len(es))
            for e in es:
                url2 = e.get_attribute('href')
                text = e.get_attribute('text')
                # print(text,url2)
                r = {'title':text,'url':url2}
                ret.append(r)
        except :
            print("xpath error")
        finally:
            driver.quit()
        return ret
if __name__=='__main__':  
    s = SP0('r402')
    ret = s.sp()
    print(ret)