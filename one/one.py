from urllib import request
import requests
import bs4
from PIL import Image
from io import BytesIO
import time
import re
url="http://wufazhuce.com/"
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

print("获取当前页面信息")
now = soup.find('div', class_="item active")
new = now.find('a')['href']

new_req = request.Request(new)
new_req.add_header("user-anget","Mozilla/5.0")
new_response = request.urlopen(new_req)
print(new_response.getcode())

new_html=new_response.read()

new_soup = bs4.BeautifulSoup(new_html, "html.parser", from_encoding="utf-8")

print("获取图片信息")
img2 = new_soup.find('div', class_="one-imagen")
img = img2.find('img')
html = requests.get(img.get('src'))
folder_path = './photo'
img_name = folder_path + str(1) + '.png'
image = Image.open(BytesIO(html.content))
image.save('E:/1.png')
# print(img_response)


# new = now.find('a')['href']
# print("获取贴吧的链接")
# tieba = soup.find('a',href="http://tieba.baidu.com/f?kw=&fr=wwwt")
# print(tieba.name, tieba['href'], tieba.get_text())
#
# print("获取地图的链接")
# map = soup.find('a',href=re.compile(r"map"))
# print(map.name, map['href'], map.get_text())