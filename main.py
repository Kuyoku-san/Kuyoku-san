from bs4 import BeautifulSoup
import requests
import colorama
 
"extrai todo conteudo do site"
site = requests.get("https://earth.google.com/web/@-12.57601305,-55.51452328,12415.99193201a,11577298.77262831d,60y,0.68315478h,8.03632946t,0r").content

"baixa o html do site"
soup = BeautifulSoup(site, 'html.parser')


temperatura = soup.find("span", class_="_block _margin-b-5 -gray")



"transforma o html em string"
print(soup.prettify())

