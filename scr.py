import urllib.request as req
from bs4 import BeautifulSoup as soup
import re

my_url = "https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/bd/bd1819a"
base_url = "https://www.aph.gov.au"

#get page
page = req.urlopen(my_url)
page_html = page.read()
page.close()

#html parsing
page_soup = soup(page_html, "html.parser")

x = list(set([link.get('href') for link in page_soup.find_all(href=re.compile("epub"))]))

print(len(x))

for url in x:
    name = re.split('\.' ,re.split('\/', url)[-1])[0]
    furl = re.sub(url, "%20", " ")
    try:
        print("getting " + base_url+url)
        req.urlretrieve(base_url+furl, name)
    except:
        print(name + " couldn't be downloaded")

print("done")
