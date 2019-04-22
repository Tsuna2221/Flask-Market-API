from bs4 import BeautifulSoup
from urllib.request import urlopen


category_url = 'https://www.newegg.com/Nintendo-Switch-Systems/SubCategory/ID-3732?Tid=252379'
cat_client = urlopen(category_url)
cat_html = cat_client.read()
cat_client.close()
cat_page = BeautifulSoup(cat_html, 'html.parser')

#response = requests.post(post_url, son=product)
txt = open('urls.txt', 'a')

for item in cat_page.find_all("a", {'class': 'item-img'}):
    txt.write(item['href'] + '\n')

txt.close()

