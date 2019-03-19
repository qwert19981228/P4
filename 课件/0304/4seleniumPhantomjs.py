from selenium import webdriver
import time
# 初始化浏览器
browser = webdriver.PhantomJS()

# 发送请求
browser.get('http://www.baidu.com')



# 向表单中输入内容
browser.find_element_by_id('kw').send_keys('美女高清大图')
# 单机搜索按钮
browser.find_element_by_id('su').click()
time.sleep(3)
# 截图 图片必须是png
browser.save_screenshot('baidu.png')

# 获取源代码
html = browser.page_source
print(html)


# 关闭浏览器
browser.quit()