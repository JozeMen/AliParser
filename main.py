import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://aliexpress.ru/category/202000005/home-appliances.html?spm=a2g2w.home.category.3.75df59310RSNkB"
r = requests.get(URL_TEMPLATE)
FILE_NAME= "test.xlsx"
columns = []
def parse(url = URL_TEMPLATE):
     resultList = {"text": []}
     soup = bs(r.text, "html.parser")
     vacancies_names = soup.find_all('div', class_='product-snippet_ProductSnippet__container__lido9p product-snippet_ProductSnippet__horizontal__lido9p product-snippet_ProductSnippet__imageSizeS__lido9p product-snippet_ProductSnippet__hideOptions__lido9p product-snippet_ProductSnippet__hideCashback__lido9p product-snippet_ProductSnippet__hideSubsidy__lido9p product-snippet_ProductSnippet__hideAd__lido9p product-snippet_ProductSnippet__hideActions__lido9p product-snippet_ProductSnippet__hideSponsored__lido9p product-snippet_ProductSnippet__hideGroupLink__lido9p')
     for name in vacancies_names:
          print(name.text + '\n')
          resultList["text"].append(name.text)
          columns = [name.get_text(strip=True)]
     return resultList

df = pd.DataFrame(data=parse(), columns=columns)
df.to_excel(FILE_NAME, index= False)
