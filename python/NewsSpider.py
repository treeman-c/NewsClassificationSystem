# encoding = "utf-8"
import io
import os.path
import sys
import time

import requests
import re
import jieba
import jieba.analyse
import pandas as pd
import lxml.etree as et


# 根据给定的url链接获取到文本
def GetText(purl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69',
        'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'
        # 'Cookie': 'BIDUPSID=A1D18A29D1DDDDD89C04884097F38872; PSTM=1642483744; BAIDUID=A1D18A29D1DDDDD8425653B90A3FD9BD:FG=1; __yjs_duid=1_bcf5e34f0e901389b138a17b4a4c838e1642730753996; BDUSS=YzZVJneUtldERYNFhoaGY5bkd6bnRDRjRzLTlKRGMxVExYN01HUkVsY2Y1UkZpRVFBQUFBJCQAAAAAAAAAAAEAAAAcMLFjuenL3tau19MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB9Y6mEfWOphbF; BDUSS_BFESS=YzZVJneUtldERYNFhoaGY5bkd6bnRDRjRzLTlKRGMxVExYN01HUkVsY2Y1UkZpRVFBQUFBJCQAAAAAAAAAAAEAAAAcMLFjuenL3tau19MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB9Y6mEfWOphbF; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_N2RkZDMxM2VhOTU1MDE3YmVmMDlkZWYzMmViOWE2NWFmMjhkZjQ5NzliN2UyNWJjZGU3MTI5ZDIwZWE1MjJmODg2OWI1MjgzZmUxZWU5YmYzNGVhYTU3YjkxNjRmMTcwNzNkMmFiNGI2NDFkMTZhMGFiYTczNjk3N2NhMTVmMDg4ZDIyYWM3NjMzZDk0ZTYzNTI4ODJhZWIwYmYyYWE4MQ==; H_PS_PSSID=35704_35104_34584_35491_35320_26350_35745; BAIDUID_BFESS=B267FCF5462AD4665973E7CCCDCE2F28:FG=1; delPer=0; PSINO=7; BA_HECTOR=8h8g812g20al8l0gcd1gv43rf0q'
    }
    try:
        resp = requests.get(url=purl, headers=headers)
        if resp.status_code == 404:
            time.sleep(3)
            return None
    except (requests.exceptions.ChunkedEncodingError, requests.ConnectionError,
            requests.exceptions.ReadTimeout) as e:
        return None
    resp.encoding = 'utf-8'  # 设置解析编码
    # xpath
    tree = et.HTML(resp.text)
    html = tree.xpath(
        '//div[@class=\"main\"]/div[@class=\"sidebar\"]/h2/div[@class=\"viewport\"]/div[@class=\"overview\"]//text()')
    if not html:
        html = tree.xpath(
            '//div[@class=\"post_main\"]/div[@class=\"post_content\"]/div[@class=\"post_body\"]//text()')
    str = ''
    for el in html:
        if '#' in el or 'if' in el:
            pass
        else:
            str += el
    html = str
    del str
    if html == '':
        return None
    return html


# 根据给定的url地址，获取该页面的所有文章链接
def Geturl(purl):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69',
        'Accept': 'image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8'
        # 'Cookie': 'BIDUPSID=A1D18A29D1DDDDD89C04884097F38872; PSTM=1642483744; BAIDUID=A1D18A29D1DDDDD8425653B90A3FD9BD:FG=1; __yjs_duid=1_bcf5e34f0e901389b138a17b4a4c838e1642730753996; BDUSS=YzZVJneUtldERYNFhoaGY5bkd6bnRDRjRzLTlKRGMxVExYN01HUkVsY2Y1UkZpRVFBQUFBJCQAAAAAAAAAAAEAAAAcMLFjuenL3tau19MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB9Y6mEfWOphbF; BDUSS_BFESS=YzZVJneUtldERYNFhoaGY5bkd6bnRDRjRzLTlKRGMxVExYN01HUkVsY2Y1UkZpRVFBQUFBJCQAAAAAAAAAAAEAAAAcMLFjuenL3tau19MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAB9Y6mEfWOphbF; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; ab_sr=1.0.1_N2RkZDMxM2VhOTU1MDE3YmVmMDlkZWYzMmViOWE2NWFmMjhkZjQ5NzliN2UyNWJjZGU3MTI5ZDIwZWE1MjJmODg2OWI1MjgzZmUxZWU5YmYzNGVhYTU3YjkxNjRmMTcwNzNkMmFiNGI2NDFkMTZhMGFiYTczNjk3N2NhMTVmMDg4ZDIyYWM3NjMzZDk0ZTYzNTI4ODJhZWIwYmYyYWE4MQ==; H_PS_PSSID=35704_35104_34584_35491_35320_26350_35745; BAIDUID_BFESS=B267FCF5462AD4665973E7CCCDCE2F28:FG=1; delPer=0; PSINO=7; BA_HECTOR=8h8g812g20al8l0gcd1gv43rf0q'
    }
    try:
        resp = requests.get(purl, headers=headers)
    except ConnectionError:
        print('网页链接错误')
        return
    resp.encoding = 'utf-8'  # 设置解析编码
    html = resp.text
    match = re.findall('(<a.*?>.*?<\\/a>)', html, re.I)  # 提取页面的所有a标签
    reurl = re.compile('href=\"(http.*?)\".*?>[\u4E00-\u9FA5]{6,}', re.I)  # 提取标签中的所有标题大于6个字的链接
    urls = []
    # 一下内容进一步筛选，文章标题大于等于十个字的链接提取到链接数组里
    for m in match:
        # 如果列表为空([])则为false
        if reurl.findall(m):
            urls.append(reurl.findall(m)[0])  # 保存链接
        else:
            continue
    return urls


# 获取文本关键字
def Getpaper(text):
    # 正则
    delOrther = re.compile(r'[\s]*', re.I)  # 去除空格回车制表符等其他字符
    text = delOrther.sub('', text)
    if text == '':
        return None
    delOrther = re.compile(r"[^a-zA-Z0-9\u4E00-\u9FA5]")
    text = delOrther.sub('', text)  # 去除非汉字字母数字的符号
    if text is None:
        return None
    return text


# 获取停用词文本
def GetStopword():
    stopword = []
    with open("./stopwords/baidu_stopwords.txt", 'r', encoding='utf-8') as f:
        for item in f:
            stopword.append(item.strip())
    return stopword


# 使用停用词文本去除文本的停用词
def DelStopword(df):
    stopworlds = GetStopword()  # 百度停用词对新闻过滤效果较好
    df['keyword'] = df['文本内容'].apply(lambda x: " ".join([w for w in list(jieba.cut(x)) if w not in stopworlds]))
    print('已去除停用词')
    return df


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
    new = new.append(old)
    new.drop_duplicates(subset=['文本内容'], keep='first', inplace=True)
    new.to_csv('newdata.csv', index=None, encoding='utf-8')


def Transfrom(lists):
    label = []
    text = []
    for categ in lists:
        urls = lists[categ]
        for url in urls:
            temp = GetText(url)
            if temp:
                temp = Getpaper(temp)
            if temp is not None:
                label.append(categ)
                text.append(temp)
    dict = {
        '文本类别': label,
        '文本内容': text
        }
    return dict


# 获取训练需要的数据集
def GetData():
# if __name__=='__main__':
    # 爬取网易新闻
    lists = {'体育': Geturl('https://sports.163.com/'),
             '军事': Geturl('https://war.163.com/'),
             '航空': Geturl('https://news.163.com/air/'),
             '政治': Geturl('https://gov.163.com/'),
             '国际': Geturl('https://news.163.com/world/')}
    lists = Transfrom(lists)
    save(lists)

