#pip install BeautifulSoup4

from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text,'html')

print(soup)

soup.find('table')

soup.find('table', class_ = 'wikitable sortable')

table = soup.find_all('table')[1]   #find_all()-scans the entire document looking for results

print(table)

world_titles = table.find_all('th') # scraping first table

world_titles

world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)

import pandas as pd

df = pd.DataFrame(columns= world_table_titles)

df

#extracting column data - tr
column_data = table.find_all('tr')

column_data

for row in column_data[1:]:  # for removing empty column list we use [1:]
  row_data = row.find_all('td')
  #print(row_data)    extracting row data - td

  individual_row_data = [data.text.strip() for data in row_data]
  #print(individual_row_data)

  length = len(df)
  df.loc[length] = individual_row_data

print(df)

df.to_csv(r'D:\webscraping\output\Companies.csv',index = False)

