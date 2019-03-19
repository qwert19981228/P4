from selenium import webdriver
import time

# 添加请求头
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)

# 初始化浏览器
browser = webdriver.PhantomJS(desired_capabilities=dcap)

# 请求地址
browser.get('https://weibo.com/')

time.sleep(10)
browser.save_screenshot('weibo1.png')
browser.find_element_by_id('loginname').send_keys('17611593298')
browser.find_element_by_name('password').send_keys('zhy123g123j')
browser.find_element_by_css_selector('a[class="W_btn_a btn_32px"]').click()
time.sleep(10)
browser.save_screenshot('weibo2.png')
html = browser.page_source
print(html)

browser.quit()



