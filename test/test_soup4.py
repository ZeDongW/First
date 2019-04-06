from urllib import request
import bs4
import re
url="http://www.baidu.com"
req = request.Request(url)
req.add_header("user-anget","Mozilla/5.0")
response = request.urlopen(req)
print(response.getcode())

html_doc=response.read()

soup = bs4.BeautifulSoup(html_doc, "html.parser", from_encoding="utf-8")

print(html_doc.decode("utf-8"))
print("获取所有的链接")
links = soup.find_all('a')

for link in links:
    print(link.name, link['href'], link.get_text())

print("获取贴吧的链接")
tieba = soup.find('a',href="http://tieba.baidu.com/f?kw=&fr=wwwt")
print(tieba.name, tieba['href'], tieba.get_text())

print("获取地图的链接")
map = soup.find('a',href=re.compile(r"map"))
print(map.name, map['href'], map.get_text())