from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://worldpopulationreview.com/country-rankings/gun-deaths-by-country'

page = requests.get(url)

soup = BeautifulSoup(page.text, features= 'html.parser')

table = soup.select_one('table')


df = pd.read_html(str(table))[0]

#PRINT OUT THE TABLE
print(df.to_string())


# VISUALIZATION
# BY USING MATPLOTLIB

import matplotlib.pyplot as plt

# Data
countries = ['Brazil', 'United States', 'Mexico', 'India', 'Colombia',
             'Venezuela', 'Philippines', 'Guatemala', 'Nigeria', 'Iraq']
total_deaths = [49437, 37040, 22118, 14712, 13171, 10599, 9268, 5982, 5103, 4424]

# Plot
plt.figure(figsize=(10, 6))
plt.bar(countries, total_deaths, color='skyblue')
plt.xlabel('Country')
plt.ylabel('Total Deaths')
plt.title('Total Deaths by Country')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
