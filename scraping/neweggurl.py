from bs4 import BeautifulSoup
from urllib.request import urlopen

print('Insert Category URL'); category_url = input()
cat_client = urlopen(category_url)
cat_html = cat_client.read()
cat_client.close()
cat_page = BeautifulSoup(cat_html, 'html.parser')

#response = requests.post(post_url, son=product)
txt = open('urls.txt', 'w')

for item in cat_page.find_all("a", {'class': 'item-img'}):
    txt.write(item['href'] + '\n')

txt.close()

