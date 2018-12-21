import urllib.request as req
from bs4 import BeautifulSoup as soup
import re

epub_get = True
pdf_get = False

invar = 50

my_url = "https://www.aph.gov.au/Parliamentary_Business/Bills_Legislation/bd/bd1819a"
base_url = "https://www.aph.gov.au"

#get page
page = req.urlopen(my_url)
page_html = page.read()
page.close()

#html parsing
page_soup = soup(page_html, "html.parser")

table = page_soup.find(id="libraryDataTable")
tbody = table.tbody

pat = "tr"

for row in tbody.find_all(pat):
    text = row.get_text("\n", strip=True) 
    fields = re.split(re.compile("\n"), text)
    epub = [link.get('href') for link in row.find_all(href=re.compile("epub"))]
    pdf = [link.get('href') for link in row.find_all(href=re.compile("pdf"))]

    name, number, date = fields
    epub_url = re.sub(" ", "%20", base_url+epub[0])
    pdf_url = pdf[0]

    #print("number: " + number +"\nname: " + name + "\ndate: " + date + "\nepub: " + epub_url + "\npdf:  " + pdf_url)
    if pdf_get and int(number) > invar:
        try:
            pdf_name = str(number) + " "+ name  + " " + "(" + date + ")" + ".pdf"
            req.urlretrieve(pdf_url, pdf_name)
        except:
            print("error")

    if epub_get and int(number) > invar:
        try:
            epub_name = number + " "+ name  + " " + date + ".epub"
            req.urlretrieve(epub_url, epub_name)
        except:
            print("error")

