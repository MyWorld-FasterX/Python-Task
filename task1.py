import requests
from bs4 import BeautifulSoup
baseurl="https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage=1"

headers={
    'User-Agent':'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Mobile Safari/537.36'
}
for x in range(1,3):
    r=requests.get(f'https://www.midsouthshooterssupply.com/dept/reloading/primers?currentpage={x}')
    soup=BeautifulSoup(r.content,'lxml')
    product_List=soup.find_all('div',class_='product-container')
    product_Links=[]
    for item in product_List:
        for link in item.find_all('a',href=True):
            product_Links.append(baseurl + link['href'])

#test_link='https://www.midsouthshooterssupply.com/item/00123wmglp/winchester-usa-ready-match-large-pistol-primers-1000-count'

for link in product_Links:
    r=requests.get(link,headers=headers)
    soup1=BeautifulSoup(r.content, 'lxml')
    try:
        name=soup1.find('a',class_='catalog-item-name').text.strip()
    except:
        name="no name"

    price= soup1.find('span',class_='price').text.strip()
    stock=soup1.find('span',class_='out-of-stock').text.strip()
    manf=soup1.find('span',class_='product-id').text.strip()

    product={
    'name':name,
    'price':price,
    'stock':stock,
    'manufacturer:':manf
    }
    print(product)