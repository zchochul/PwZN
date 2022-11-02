import requests
from bs4 import BeautifulSoup
import json
import sys

req = requests.get("https://www.fizyka.pw.edu.pl/index.php/Pracownicy/Lista-pracownikow/Pracownicy-badawczo-dydaktyczni")

#print(req.status_code)#status strony
#print(req.text)#tekst strony
#print(req.request.headers) #User-agent - co robi zapytanie, w tym przypadku zapytanie z pythona, czasem blokuja strony jak widza cos co nie jest przegladarka

soup = BeautifulSoup(req.text, 'html.parser')


people = soup.find('div', {'class' : 'class-folder'})
#print(people.text)

pracownicy = []
for person in people.find_all('h2'):
    data = person.find('a')
    pracownicy.append((data.text.strip()).splitlines())
    

#tu opcja jakby sie chcialo bez tytulow naukowych
#osoby = []
#for i in pracownicy:
#    osoby.append(( i[1], i[2]))
if (len(sys.argv) != 2):
    print('Podano niewlasciwa ilosc argumentow', len(sys.argv))
    plik_nazwa = 'Scrapping.json'
else:
    print('Podano wlasciwa ilosc argumentow')
    plik_nazwa = sys.argv[1]

with open(plik_nazwa, 'w') as f:
    json.dump(pracownicy, f)