from bs4 import BeautifulSoup
from urllib.request import urlopen
import moment, datetime, requests, json
import re

post_url = "http://127.0.0.1:5000/products/insert"
text = open('amazon.txt', 'r')

print("Opening Urls")
for url in text.readlines():
    client = urlopen(url)
    html = client.read()
    client.close()
    page = BeautifulSoup(html, 'html.parser')

    print("Getting Title..."); title = page.find('div', {'id': 'imgTagWrapperId'}).img['alt']
    print(url)

    print("Getting Company...")
    def company():
        try:
            if page.find('div', {'id': 'mbc'}) is not None: 
                return page.find('div', {'id': 'mbc'})['data-brand'] 
            else: 
                return page.find('a', {'id': 'bylineInfo'}).text.replace('by', '').strip()
        except:
            print('Company not Found. Insert Company: '); return input()

    print('Getting Prices...')
    def price():
        try:
            if page.find('input', {'id': 'attach-base-product-price'}) is not None: 
                return int(page.find('input', {'id': 'attach-base-product-price'})['value'].replace('.', ''))
            else: 
                return int(page.find('span', {'class': 'price-large'}).text.strip() + "99") 
        except:
            print('Price not Found. Insert a price: '); return int(input())

    print('Getting Rating...') 
    def rating():
        try:
            rating = page.find('span', {'id': 'acrPopover'})
            if rating != None:
                return int(rating['title'][0])
            else:
                return 0
        except:
            print('Company not Found. Insert Rating: '); return input()

    print("Getting Descriptions...")
    def description():
        desc_string = ""

        try:
            for p in page.find("div", {"id":"productDescription"}).findAll('p'):
                desc_string += p.text.strip() + '\n'
        except:
            print('Could not find a <p> description')

        return desc_string

    print('Getting Images...'); images = []; images.append(page.find('div', {'id': 'imgTagWrapperId'}).img['data-old-hires'])

    #Input Category Info
    print(title + " - " + company())
    print('Insert Category: '); category = input()
    if category != '!pass':
        print('Insert Sub-Category: '); sub = input()
        print('Insert Type Category: '); type_cat = input()

        obj = {
            'title': title,
            'company': company(),
            'price': price(),
            'price_percentage': 0,
            'quantity': 100,
            'num_of_shares': 0,
            'images': images,
            'about': {
                'description': description(),
                'release_date': moment.now().format("D-M-YYYY"),
                'rating': rating()
            },
            'category': {
                'category_name': category,
                'sub_category': {
                    'name': sub,
                    'type': type_cat
                }
            }
        }

        response = requests.post(post_url, json=obj)

        print(response.text)
