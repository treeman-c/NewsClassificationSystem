
import os.path
import time
from selenium.webdriver.chrome.service import Service
import pandas as pd
from selenium import webdriver

driver = webdriver.Edge(service=Service(r'E:\WebDriver\msedgedriver.exe'))  # 这里浏览器驱动器的文件路径，我这里是edge最新的驱动器


# 根据给定的url地址，获取该页面的所有文章链接
def crawUrl(url):
    # try:
    driver.get(url)
    driver.refresh()
    # for i in range(1, 100):
    #
    #     # print('i===', i)
    #     element = driver.find_element_by_xpath('//*[@class="xpage-more-btn"]')
    #     driver.execute_script("arguments[0].click();", element)
    driver.execute_script('document.documentElement.scrollTop=100000')
    time.sleep(2)
    a = driver.find_elements_by_xpath('//a')  # 根据标签查找
    # except Exception:
    #     print('出现异常了')
    #     return None
    urls = []
    for floderurl in a:

            result = floderurl.get_attribute("href")
            urls.append(result)

    print("最终的uRL：", urls)
    return urls


# 根据给定的url链接获取到文本
def crawText(purl):
    text = ''
    try:
        driver.get(purl)
        text = driver.find_element_by_xpath('//*[@id="content"]/div[@class="post_body"]').text
    except Exception:
        return None
    print(text)

    return text


# 保存和加载数据
def save(lists):
    new = pd.DataFrame({
        '文本类别': lists['文本类别'],
        '文本内容': lists['文本内容']
    })
    if not os.path.exists('newdata.csv'):
        with open('newdata.csv') as f:
            pass
    old = pd.read_csv('newdata.csv', encoding='utf-8', engine='python')
    new = pd.concat([new, old])
    new.drop_duplicates(subset=['文本内容'], keep='first', inplace=True)
    new.to_csv('newdata.csv', index=None, encoding='utf-8')


def Transfrom(lists):
    label = []
    text = []
    for categ in lists:
        urls = lists[categ]
        for url in urls:
            temp = crawText(url)
            if temp is not None:
                label.append(categ)
                text.append(temp)
    dict = {
        '文本类别': label,
        '文本内容': text
    }
    return dict

    #  "政治": crawUrl('http://cpc.people.com.cn/')
    #    "军事": crawUrl('http://www.xinhuanet.com/milpro/'),


#   "军事": crawUrl('http://military.people.com.cn/'),
if __name__ == '__main__':
    lists = {
        '航空': crawUrl('https://news.163.com/air/'),

    }

    lists = Transfrom(lists)
    print(lists)
    save(lists)

    driver.quit()
