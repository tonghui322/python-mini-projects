import requests as rq
from bs4 import BeautifulSoup

# 定义网址变量
url = input("Enter Link:")

# 工具方法 找到网址内容
def get_content(param_url):
    # 取内容
    _content = rq.get(url)
    return _content

url_content = get_content(url)
print(url_content)

#从内容中提取所有超链接

def get_url_content_a(param_url_contemt):
    #正则取出超链接
    soup = BeautifulSoup(param_url_contemt.text,"html.parser")
    print(soup)
    _a_array = []
    for link in soup.find_all("a"):
        _a_array.append(link.get("href"))
    return _a_array

a_array = get_url_content_a(url_content)

print(a_array)