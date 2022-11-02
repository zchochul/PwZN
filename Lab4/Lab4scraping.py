import requests
from bs4 import BeautifulSoup
import json

req = requests.get("https://www.imdb.com/name/nm0001569/")

#print(req.status_code)#status strony
#print(req.text)#tekst strony
#print(req.request.headers) #User-agent - co robi zapytanie, w tym przypadku zapytanie z pythona, czasem blokuja strony jak widza cos co nie jest przegladarka
soup = BeautifulSoup(req.text, 'html.parser')

films = soup.find('div', {'class' : 'filmo-category-section'})
#print(films.text)

chuck_fims = []

for film in films.find_all('div', {'class' : 'filmo-row'}):
    span = film.find('span')
    title = film.find('a')
    #print(span.text.strip(), title.text.strip(), title['href'])
    chuck_fims.append((span.text.strip(), title.text.strip(), title['href']))

#print(chuck_fims)

with open('Lab4scrapping.json', 'w') as f:
    json.dump(chuck_fims, f)