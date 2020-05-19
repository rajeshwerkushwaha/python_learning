# Import Libraries
import requests
from bs4 import BeautifulSoup

###########################################
## to get all the names & profile links  ##
###########################################
# f = open('linkedin1.htm', 'r')
# response = f.read()
# soup = BeautifulSoup(response, "html.parser")
# objects = soup.find_all('a', {'class':'title'})
# for obj in objects:
#     print(obj.text+ '<===>'+ 'https://www.linkedin.com/'+obj['href'])


##########################################################
# to get all the title & answers from a given web page  ##
##########################################################
#Set the URL you want to webscrape from
url = 'https://www.yelp.ie/search?cflt=restaurants&find_loc=Dublin'

# Connect to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")


for item in soup.select("#wrap > div:nth-child(4) > div.lemon--div__373c0__1mboc.spinnerContainer__373c0__dHYYg.verticalFilterPanelEnabled.border-color--default__373c0__3-ifU.background-color--white__373c0__2uyKj > div > div.lemon--div__373c0__1mboc.leftRailContainer__373c0__390Ky.border-color--default__373c0__3-ifU > div.lemon--div__373c0__1mboc.leftRailMainContent__373c0__4Lx_e.padding-r5__373c0__126QE.padding-b5__373c0__3XORh.padding-l5__373c0__2Dc5X.border-color--default__373c0__3-ifU > div.lemon--div__373c0__1mboc.leftRailSearchResultsContainer__373c0__GUx8Y.border-color--default__373c0__3-ifU > div:nth-child(2) > ul > li"):
	print('Image Link: ', item.img['src'])
	print('Name: ', item.select('a[class="lemon--a__373c0__IEZFH link__373c0__1G70M link-color--inherit__373c0__3dzpk link-size--inherit__373c0__1VFlE"]')[0].text)
	print('Ratings: ', item.select('span[class="lemon--span__373c0__3997G text__373c0__2Kxyz reviewCount__373c0__2r4xT text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-"]')[0].text)
	print('Address: ', item.select('address')[0].text)
	print('Phone: ', item.select('p[class="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--right__373c0__1f0KI text-size--small__373c0__3NVWO"]')[0].text)
	print('Price Range: ', item.select('span[class="lemon--span__373c0__3997G text__373c0__2Kxyz priceRange__373c0__2DY87 text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa- text-bullet--after__373c0__3fS1Z"]')[0].text)
	print('Description: ', item.select('p[class="lemon--p__373c0__3Qnnj text__373c0__2Kxyz text-color--black-extra-light__373c0__2OyzO text-align--left__373c0__2XGa-"]')[0].text)
	print("==================================================================================================================================")


https://www.google.com/search?safe=active
&sxsrf=ALeKk02VM76gF9Z315iMPYKpKiPvandsbg%3A1589708819353
&source=hp&ei=EwjBXrCWE_WO1fAP0a-WiA8
&q=%22current.*+Amazon%22+site%3Alinkedin.com%2Fin+developer
&oq=%22current.*+Amazon%22+site%3Alinkedin.com%2Fin+developer
&gs_lcp=CgZwc3ktYWIQA1DJDFjJDGCfFWgAcAB4AIABI4gBI5IBATGYAQCgAQKgAQGqAQdnd3Mtd2l6
&sclient=psy-ab&ved=0ahUKEwjw6-LrzrrpAhV1RxUIHdGXBfEQ4dUDCAc
&uact=5

###########################################
## to get all the email subject lines #####
###########################################
# f = open('emails1.html', 'r')
# response = f.read()
# soup = BeautifulSoup(response, "html.parser")
# objects = soup.find_all('span', {'class':'bqe'})
# sub_list = []
# for obj in objects:
#     sub_list.append(obj.text)
# sub_list = set(sub_list)

# # append mode
# f = open('flipkart.txt', 'a')

# for i,val in enumerate(sub_list):
#     f.write('\n{}'.format(val))


