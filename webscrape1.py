from bs4 import BeautifulSoup
import re 

with open("index2.html", "r") as f:
    doc = BeautifulSoup(f, "html.parser")

#tags = doc.find_all(text=re.compile("\$.*"), limit =1) #find the tags in all the docs with anything that has a dollar sign and limits that result to 1 
tags = doc.find_all("input", type="text")
for tag in tags:
    tag['placeholder'] = 'I changed you'

with open("changed.html", "w") as file:
    file.write(str(doc))
    

