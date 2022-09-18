import requests
from bs4 import BeautifulSoup
from fpdf import FPDF

# Webpage connection
html = "https://avc.com/category/web3"
r=requests.get(html)
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
            final = print(i[0].get_text().strip(),('\n\n'),i[1].get_text().strip(),('\n\n'))
            pdf.final("final.pdf")

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
# movie_name = results.find('h3').find('a')
# movie_year = results.find('h3').find('span')
# #use the strip function to trim any extra spaces or lines
# print(movie_name.text.strip() +movie_year.text.strip()) 
# main_content = results.find('div', class_='lister')
# noOfReviews = main_content.find('span')
# print(noOfReviews.text)

# #find all function will return the list of all those divs, we will iterate each item to extract data from nested tags.

# reviewsList = main_content.find_all('div', class_='lister-item')
# print(reviewsList)

# for review in reviewsList:
#      #just for adding a line 
#     print(" ")  
#     #The div contains the user reviews
#     listContent = review.find('div', class_='lister-item-content')
#     reviewTitle = listContent.find('a', class_='title')
#     print('Review Title:', reviewTitle.text.strip())
#     rating = listContent.find('span', class_='rating-other-user-rating')  #rating span
#     #To avoid NoneType objects
#     if rating==None:
#         continue
#     #the actual rating text
#     ratingText = rating.find_all('span')  
#     print("Rating: ",ratingText[0].text.strip())
#     userName = listContent.find('span', class_='display-name-link')
#     print('Username: ', userName.text)
#     reviewDate = listContent.find('span', class_='review-date')
#     print('Review Date:', reviewDate.text)
#     reviewContent = listContent.find('div', class_='text')
#     print('Review:',reviewContent.text)


# with open("output1.html", "w", encoding='utf-8') as reviewsList:
#     reviewsList.write(str(soup))