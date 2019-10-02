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


###########################################################
## to get all the title & answers from a given web page  ##
###########################################################
# Set the URL you want to webscrape from
# url = 'https://www.geeksforgeeks.org/puzzle-1-how-to-measure-45-minutes-using-two-identical-wires/'

# # Connect to the URL
# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")

# title = soup.find('h1', {'class':'entry-title'}).text
# question = soup.find('div', {'class':'entry-content'}).findAll('p')[0].text
# answer = soup.find('div', {'class':'entry-content'}).findAll('p')[2].text

# print('Title: '+title)
# print('\nQuestion: '+question)
# print('\n '+answer)


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



###########################################
## to get unique email subject lines  #####
###########################################
sub_list = []
f = open('grpn.txt', 'r')
while True:
	line = f.readline()
	sub_list.append(line.strip())
	if ("" == line):
		break;

sub_list = set(sub_list)

f = open('grpn_final.txt', 'a')
for i,val in enumerate(sub_list):
    f.write('\n{}'.format(val))