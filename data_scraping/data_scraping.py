# Import Libraries
import requests
from bs4 import BeautifulSoup

# Set the URL you want to webscrape from
url = 'https://www.geeksforgeeks.org/puzzle-1-how-to-measure-45-minutes-using-two-identical-wires/'

# Connect to the URL
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

title = soup.find('h1', {'class':'entry-title'}).text
question = soup.find('div', {'class':'entry-content'}).findAll('p')[0].text
answer = soup.find('div', {'class':'entry-content'}).findAll('p')[2].text


print('Title: '+title)
print('\nQuestion: '+question)
print('\n '+answer)

