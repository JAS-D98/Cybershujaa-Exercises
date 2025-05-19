'''
  Title: Web Scraping Project
  Name: Jasper Wambugu
  Date: 19 May 2025
  Web Scraping a database of NHL team stats since 1990.
'''
from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.scrapethissite.com/pages/forms/'
page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
print(soup)

#Extract the table with the Hockey Scores
hockey_table = soup.find('table', class_='table')
print(hockey_table)

#Extract the column headings
table_titles = hockey_table.find_all('th')
hockey_table_title = [title.text.strip() for title in table_titles]
print(hockey_table_title)

#Save the column headings onto a Pandas DataFrame
df = pd.DataFrame(columns=hockey_table_title)
# df

#Extract the data row by row. First get all rows, then loop through each while stripping and saving data into the DataFrame
table_data = hockey_table.find_all('tr')
for row in table_data[1:]:
  raw_data = row.find_all('td')
  each_raw_data = [data.text.strip() for data in raw_data]
  print(each_raw_data)

  #saving each row data as it is generated into the pandas data frame
  length = len(df)
  df.loc[length] = each_raw_data

# #Inspect the resulting DataFrame
# df

# #Save to a .csv file in the current folder
df.to_csv(r'./Hockey.csv')