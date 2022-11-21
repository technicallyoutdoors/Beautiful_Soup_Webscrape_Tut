#beautiful soup only works with python interpreter from version python 3.10.5
from bs4 import BeautifulSoup
import requests 

url = "https://www.newegg.com/gigabyte-geforce-rtx-3090-gv-n3090aorusx-wb-24gd/p/N82E16814932386?Item=9SIAYTVFU57355&Description=gpu%20rtx&cm_re=gpu_rtx-_-9SIAYTVFU57355-_-Product&cm_sp=SP-_-1272231-_-0-_-3-_-9SIAYTVFU57355-_-gpu%20rtx-_-gpu|rtx-_-1" 

result = requests.get(url)

doc = BeautifulSoup(result.text, "html.parser")



prices = doc.find_all(text="$")

parent = prices[0].parent
print(parent) 
strong = parent.find("strong")
print(strong.string)

