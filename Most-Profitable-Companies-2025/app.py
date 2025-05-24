from bs4 import BeautifulSoup
import requests
import pandas as pd

url='https://www.forbesindia.com/article/explainers/top-10-largest-companies-world-market-cap/86341/1'


try:
    page=requests.get(url)
    soup=BeautifulSoup(page.text, 'html.parser')
    # print(soup)

    profit_tables=soup.find_all('table')[0]
    # print(profit_tables)

    table_titles=profit_tables.find_all('th')
    headers=[headers.text.strip() for headers in table_titles]
    # print(headers)
    df=pd.DataFrame(columns=headers)

    rows=profit_tables.find_all('tr')
    # print(rows)
    for row in rows:
        profit_table_rows=row.find_all('td')
        # print(profit_table_rows)
        if len(profit_table_rows) == len(headers):
            stripped_rows=[stripped_rows.text.strip() for stripped_rows in profit_table_rows]
            # print(stripped_rows)
            length=len(df)
            df.loc[length]=stripped_rows

    df

    df.to_csv(r'./Top-10-Most-Profitable-Companies-2025.csv', index=False)

except Exception as e:
    print(f'Error {e}')