import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from datetime import date


currYear = date.today().year
# Webpage connection
# YEAR = '2003'
# html = "https://avc.com/2003"

baseLink = "https://avc.com/"
for k in range(2003,currYear,1):
    link = baseLink + str(k)
    print(link)

r=requests.get(link)
c=r.content
soup=BeautifulSoup(c,"html.parser")
pdf = FPDF()

wegoList = soup.find_all("article")

def scrap_main(wegoList):
    for items in wegoList:
        title = items.find_all("a", {"class": "text-black",})
        content = items.find_all("div", {"class": "ContentArea",})
        # date = items.find_all("div", {"class": "text-content short-text",})
        for i in zip(title,content):
            print(i[0].get_text().strip(),('\n\n'),i[1].get_text().strip(),('\n\n'))
            # pdf.final("final.pdf")

scrap_main(wegoList)

# nextpage = soup.find_all("div", class_="Pagination-right")
# for link in nextpage:
#     if soup.findAll('a') == 'href':
#         print(link.get('href'))
# print(nextpage)
# for items in nextpage:
#     findolder = items.find_all("div", {"class": "Pagination-right"})
#     print(findolder)
# except:
#     pass
