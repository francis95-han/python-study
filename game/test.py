import requests
from bs4 import BeautifulSoup


def mul(n):
    if n>0:
        return (mul(n-1)+1)*2
    else:
        return 1
# print(mul(9))


url= 'http://ctf5.shiyanbar.com/jia/'
def greb(url):
    res =requests.get(url,allow_redirects=False)
    res.encoding='utf-8'
    # print(res.text)
    soup =BeautifulSoup(res.text,'html')
    print(soup.select('#templatemo_content'))
greb(url)