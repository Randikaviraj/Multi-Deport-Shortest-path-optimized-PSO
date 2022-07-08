import requests
from bs4 import BeautifulSoup
import re

x=requests.get("https://www.google.com/search?q=from+kegalle+to+dehiwala+distance&client=ubuntu&channel=fs&biw=1294&bih=177&ei=z0K2YtinGMHLpgfYmLbADQ&ved=0ahUKEwiYy8Snmcf4AhXBpekKHViMDdgQ4dUDCA0&oq=from+kegalle+to+dehiwala+distance&gs_lcp=Cgdnd3Mtd2l6EAw6BwgAEEcQsAM6BAghEApKBAhBGABKBAhGGABQ5hBYkRRgqiVoAnABeACAAesBiAHQA5IBAzItMpgBAKABAcgBCMABAQ&sclient=gws-wiz")
soup=BeautifulSoup(x.text,'lxml')
spans=soup.find('span',string= re.compile('[0-9]*\.[0-9]+ km'))
print(spans)