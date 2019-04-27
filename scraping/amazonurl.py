from selenium import webdriver

b = webdriver.Chrome('C:\\Users\\tsuna\\Google Drive\\DEV\\chromedriver')
txt = open('amazon.txt', 'a')

print('Insert URL containing octopus classes: '); url = input()

b.get(url)

elements = b.find_elements_by_class_name('s-line-clamp-2')
try:
    for e in elements:
        txt.write(e.find_element_by_tag_name("a").get_attribute('href') + '\n')

    print('Success... Type any key to exit.')
    input()
except:
    print('Scrapping failed... Type any key to exit.' )
    input()

txt.close()
b.quit()
quit()