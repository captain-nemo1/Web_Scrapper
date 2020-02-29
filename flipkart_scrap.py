#a simple flipkart price scrapper, only works for pages like https://www.flipkart.com/search?sid=czl&otracker=CLP_Filters&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000
from bs4 import BeautifulSoup
import requests

filename="data.txt"#stores data in a file called data.txt
f=open(filename,"w")
#enter url here in get
url=requests.get("https://www.flipkart.com/search?sid=czl&otracker=CLP_Filters&p%5B%5D=facets.price_range.from%3DMin&p%5B%5D=facets.price_range.to%3D20000")
soup=BeautifulSoup(url.text,"lxml")#lxml parser used
for name in soup.find_all('div',class_='_1-2Iqu row'):
    print(name.div.div.text)#name of the stuff
    try:
        price=name.find('div',class_='_1vC4OE').text #price of the stuff
    except:
        price="Not Given"
    print(price)    
    f.write(str(name.div.div.text)+" "+str(price)+"\n")#writes to the file