from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

page=requests.get(url)
soup=BeautifulSoup(page.text, 'html')

# print(soup)

company_tables=soup.find_all('table')
# print(company_tables)

profit_table=soup.find_all('table')[2]
# print(profit_table)

profit_table_header=profit_table.find_all('th')
# print(profit_table_header)

header=[header.text.strip() for header in profit_table_header]
# print(header)

df=pd.DataFrame(columns=header)

rows=profit_table.find_all('tr')
# print(rows)

for row in rows[1:]:
    row_data=row.find_all('td')
    # print(row_data)
    if len(row_data) == len(header):
        profit_row_data=[row.text.strip() for row in row_data]
        print(profit_row_data)
        length=len(df)
        df.loc[length]=profit_row_data

df.to_csv(r'./Most-Profitable-Countries-2024.csv', index=False)
    