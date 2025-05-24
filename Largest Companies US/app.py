from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page=requests.get(url)

soup=BeautifulSoup(page.text, 'html')
# print(soup)

tables=soup.find_all('table')[0]
# print(tables)

world_title=tables.find_all('th')
# print(world_title)

world_table_titles=[title.text.strip() for title in world_title]
# print(world_table_titles)

df=pd.DataFrame(columns=world_table_titles)

table_data=tables.find_all('tr')
for row in table_data[1:]:
    row_data=row.find_all('td')
    if len(row_data) == len(world_table_titles):
        each_raw_data=[data.text.strip() for data in row_data]
        print(each_raw_data)
        length=len(df)
        df.loc[length]=each_raw_data



df 

df.to_csv(r'./Top_World_Companies.csv', index=False)