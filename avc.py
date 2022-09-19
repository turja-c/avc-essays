import requests
from bs4 import BeautifulSoup
from fpdf import FPDF
from datetime import date


# Webpage connection
# YEAR = '2003'
# html = "https://avc.com/2003"

currYear = date.today().year

baseLink = "https://avc.com/"



for k in range(2003,currYear,1):
    link = baseLink + str(k)
    url_lists = link.join([link])
    print(url_lists)
    # print(link)

# req = requests.get(link)
# c = req.content
# soup=BeautifulSoup(c,"html.parser")

# ------------------------------------------------------------------------------


# url_list = ['https://avc.com/2003','https://avc.com/2004']

# for link in url_list:
#     result = requests.get(link)
#     src = result.content
#     soup = BeautifulSoup(src, 'lxml')


#     wegoList = soup.find_all("article")


    # for items in wegoList:
    #     title = items.find_all("a", {"class": "text-black",})
    #     content = items.find_all("div", {"class": "ContentArea",})

    #     for i in zip(title,content):
    #         print(i[0].get_text().strip(),('\n\n'),i[1].get_text().strip(),('\n\n'))
            # pdf.final("final.pdf")

# scrap_main(wegoList)


# ------------------------------------------------------------------------------

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
