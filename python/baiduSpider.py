import io
import os.path
import sys
import time

import requests
import pandas as pd
import lxml.etree
import re as et
from selenium import webdriver

driver = webdriver.Edge(r'E:\WebDriver\msedgedriver.exe')  # 这里浏览器驱动器的文件路径，我这里是edge最新的驱动器


# 根据给定的url地址，获取该页面的所有文章链接
def crawUrl(url):
    try:
        driver.get(url)
        a = driver.find_elements_by_xpath('//a')  # 根据标签查找
    except Exception:
        return None
    urls = []
    for floderurl in a:
        if len(floderurl.text)>6:
            result = floderurl.get_attribute("href")
            urls.append(result)

    print("最终的uRL：",urls)
    return urls


# 根据给定的url链接获取到文本
def crawText(purl):

    try:
        driver.get(purl)
        text = driver.find_element_by_xpath('//*[@id="container"]').text
    except Exception :
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


#
if __name__ == '__main__':
    lists = {
             '军事': crawUrl('https://news.baidu.com/mil'),
             '国际': crawUrl('https://news.baidu.com/guoji')
    }

    lists = Transfrom(lists)
    print(lists)
    save(lists)

    driver.quit()