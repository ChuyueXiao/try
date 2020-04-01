'''# 使用#selenium登陆博客 发表评论
# 从selenium模块中调用webdriver模块
from selenium import  webdriver
import time

driver = webdriver.Chrome()  # 声明浏览器为本地的Chrome
driver.get('https://wordpress-edu-3autumn.localprod.oc.forchange.cn/wp-login.php')  # 访问页面
time.sleep(1)  # 暂停1秒，等待浏览器缓冲

username = driver.find_element_by_id('user_login')  # 定位到输入用户名的位置
username.send_keys('sarahpractice')  # 输入用户名
password = driver.find_element_by_id('user_pass')  # 定位到输入密码的位置
password.send_keys('930930')  # 输入密码
login = driver.find_element_by_id('wp-submit')  # 定位到登录按钮的位置
login.click()  # 点击登录
time.sleep(2)  # 等待两秒

article = driver.find_element_by_partial_link_text('三')  # 根据链接的部分文字"三"，定位到这个链接
article.click()  # 点击链接
time.sleep(1)
comment = driver.find_element_by_id('comment')  # 定位到评论区
comment.send_keys('6666selenium')  # 输入评论内容
submit = driver.find_element_by_id('submit')  # 定位到"发表评论"的按钮
submit.click()  # 点击“发表评论”按钮
driver.close()


# 只使用Selenium打印 《Python 之禅》
from selenium import  webdriver # 从selenium库中调用webdriver模块
import time

driver = webdriver.Chrome() # 声明浏览器对象
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(1)

teacher = driver.find_element_by_id('teacher')  # 找到【请输入你喜欢的老师】下面的输入框位置
teacher.send_keys('必须是吴枫呀')
assistant = driver.find_element_by_name('assistant')  # 找到【请输入你喜欢的助教】下面的输入框位置
assistant.send_keys('都喜欢')
button = driver.find_element_by_class_name('sub')  # 找到【提交】按钮
button.click()
time.sleep(1)

contents = driver.find_elements_by_class_name('content')  # 定位到Python之禅所在的标签
for content in contents:
    title = content.find_element_by_tag_name('h1').text  # 提取标题
    chan = content.find_element_by_tag_name('p').text  # 提取正文
    print(title + '\n' + chan + '\n')  # 打印标题与正文
driver.close()
'''

# 使用selenium 和 beautifulSoup 配合打印《Python 之禅》
from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://localprod.pandateacher.com/python-manuscript/hello-spiderman/')
time.sleep(2)

teacher = driver.find_element_by_id('teacher')
teacher.send_keys('必须是吴枫呀')
assistant = driver.find_element_by_name('assistant')
assistant.send_keys('都喜欢')
button = driver.find_element_by_class_name('sub')
button.click()
time.sleep(1)

pageSource = driver.page_source  # 获取页面信息
soup = BeautifulSoup(pageSource,'html.parser')  # 使用bs解析网页
contents = soup.find_all(class_="content")  # 找到源代码《Python之禅》中文版和英文版所在的元素
for content in contents:  # 遍历列表
    title = content.find('h1').text # 提取标题
    chan = content.find('p').text.replace('  ','') # 提取Python之禅的正文，并且去掉文字前面的所有空格
    print(title + chan + '\n') # 打印Python之禅的标题与正文
driver.close()