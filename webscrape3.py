from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

tbody = doc.tbody
trs = tbody.contents
prices = {}

for tr in trs[:10]: 
    name, price = tr.contents[2:4]
    fixed_name = name.p.string
    fixed_price = price.span.string

    prices[fixed_name] = fixed_price
    #prices = ','.join(f'{key}: {value}' for key, value in prices)
    #tried getting the output for the prices to not include the {}, but cannot figure it out. 
    #please make contribution if you are aware how to make this happen 
print(prices)

