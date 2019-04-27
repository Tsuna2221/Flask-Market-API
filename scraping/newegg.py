from bs4 import BeautifulSoup
from urllib.request import urlopen
import moment, datetime, requests, json
import re

post_url = "http://127.0.0.1:5000/products/insert"
text = open('urls.txt', 'r')

print("Opening Urls")
for url in text.readlines():
    client = urlopen(url)
    html = client.read()
    client.close()
    page = BeautifulSoup(html, 'html.parser')

    #Get data from script
    result = []
    scripts = page.findAll('script')
    script_variations = len(scripts)

    print("Getting Scripts...")
    for var in range(script_variations):
        if 'product_title' in str(scripts[var]):
            script_string = str(scripts[var]).strip()
            pattern = re.compile(r"[a-z_]+[:]+[\[']+[\w\s\d\-\.\"\'\/,';#&]+[']+[\]]")

            for item in pattern.findall(script_string):
                fetch_array = ['product_category_name', 'product_subcategory_name', 'product_title', 'product_manufacture', 'product_sale_price']
                for fetch in fetch_array: 
                    if fetch in item:
                        fetch_pattern = re.compile(r"'+[\w\s\d\-\.\"\'\/,;#&]+'")
                        result.append(fetch_pattern.search(item).group().replace("'", ''))

            #Input Category Info
            print(result)
            print('Category: '); category = input()
            print('Sub-Category: '); sub = input()
            print('Type Category: '); type_cat = input()

            #Get description
            print("Getting Descriptions...")
            def description():
                desc_string = ""

                try:
                    for p in page.find("div", {"class":"itmDesc"}).findAll('p'):
                        desc_string += p.text.strip() + '\n'
                except:
                    print('Could not find a <p> description. Insert a Description: '); desc_string = input()

                return desc_string

            #Get OG image
            print("Getting Images...")
            images = []
            images.append(page.find('meta', {'property': 'og:image'})['content'])

            #Get ratings
            print("Getting Ratings...")
            def rating():
                try:
                    return page.find('a', {'class': 'itmRating'}).i['title'][0]
                except:
                    return 0

            obj = {
                'title': result[2],
                'company': result[3],
                'price': int(result[4].replace('.', '')),
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

            print(obj)

            response = requests.post(post_url, json=obj)

            print(response.text)
    