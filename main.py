from bs4 import BeautifulSoup as BS
import requests

url = "https://lalafo.kg/"
response = requests.get(url)
html = response.text

soup = BS(html, "html.parser")

# div = soup.find("div")
# print(div)

# div = soup.find_all('p')
# for p in div:
#     print(p.text)


link = soup.find("a")
href = link.get("href")
print(href)





# title = soup.find("title").text
# links = soup.find_all("a")
# print("mesta", title)
# print("cillka na starnitsa: ")
