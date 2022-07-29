import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.aldi.us/en/weekly-specials/this-weeks-aldi-finds/").text
soup = BeautifulSoup(html, 'html.parser')
#items = soup.find_all('h4') # this returned all telsa listings, but not in the VSC window
items = soup.find_all(class_="ratio-container m-ratio-57x25 box--description m-no-ratio-on-phone")
for item in items:
    try:
        itemName      = str(item.find("div", class_="box--description--header").contents[2]).split("\n")[0]
        dollarAmount  = str(item.find("span", class_="box--value").contents[0])
        decimalAmount = str(item.find("span", class_="box--decimal").contents[0])
        print(itemName + dollarAmount + decimalAmount)
        print(f"\n")
    except:
        print("No data found for " + itemName)




#for item in items:
    #contents = item.contents.replace(" ", "")
    #print(type(item))
    #print(type(item.contents)[0])
    #print(contents)
#    print(item)




#import requests
#from bs4 import BeautifulSoup
#
#
#vgm_url = 'https://www.vgmusic.com/music/console/nintendo/nes/'
#html_text = requests.get(vgm_url).text
#soup = BeautifulSoup(html_text, 'html.parser')
#
#soup.find_all(class_"box--price")


