import requests
from tabulate import tabulate
from bs4 import BeautifulSoup
tabulate.PRESERVE_WHITESPACE = False
import csv

itemList = []
col_names = [
    "ItemName",
    "Price"
]

html = requests.get("https://www.aldi.us/en/weekly-specials/this-weeks-aldi-finds/").text
soup = BeautifulSoup(html, 'html.parser')
items = soup.find_all(class_="ratio-container m-ratio-57x25 box--description m-no-ratio-on-phone")

for item in items:
    try:
        itemName       = (str(item.find("div", class_="box--description--header").contents[2]).split("\n")[0]).strip()
        dollarAmount   = str(item.find("span", class_="box--value").contents[0])
        decimalAmount  = str(item.find("span", class_="box--decimal").contents[0])
        cost           = dollarAmount + decimalAmount
        itemprops      = [itemName , cost]
        itemList.append(itemprops)

    except:
        print(itemName + cost)
        print(f"\n")


print("Now printing in table view")
print(tabulate(itemList, headers=col_names, tablefmt="grid", showindex="always"))