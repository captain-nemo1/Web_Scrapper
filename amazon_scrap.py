#amazon scrapper, only works for pages like https://www.amazon.in/s?bbn=1389401031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cp_36%3A1318505031&dc&fst=as%3Aoff&qid=1582959937&rnid=1318502031&ref=lp_1389401031_nr_p_36_2
from bs4 import BeautifulSoup
import requests
#stores result in file named help.txt
filename="help.txt"
f=open(filename,"w")
#using user agent cause amazon does allow scrapers
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246'
headers = {'User-Agent': user_agent}

#enter url here
url=requests.get("https://www.amazon.in/s?bbn=1389401031&rh=n%3A976419031%2Cn%3A%21976420031%2Cn%3A1389401031%2Cp_36%3A1318505031&dc&fst=as%3Aoff&qid=1582959937&rnid=1318502031&ref=lp_1389401031_nr_p_36_2", headers=headers)
soup=BeautifulSoup(url.text,"lxml")
for link in soup.find_all('div', class_="a-spacing-medium"):
    try:
        name=link.find('span',class_="a-size-medium").text
        price=link.find('span',class_="a-offscreen").text
        print(str(name)+" "+ str(price))
        f.write(str(name)+" "+ str(price)+"\n")
    except:
        pass    
f.close()    