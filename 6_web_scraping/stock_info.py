"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""
#1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
#   Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.

def get_most_active_stocks():
    page = 'https://finance.yahoo.com/markets/stocks/most-active/'
    response = requests.get(page)
    soup = BeautifulSoup(response.text, 'html')
    stocks =[]
    limit = 5
    for a_tag in soup.find_all('a', href=True):
        if '/quote/' in a_tag['href']:
            company_name_span = a_tag.find('span', class_='symbol')
            if company_name_span:
                company_name = company_name_span.text
                stocks.append(company_name)
                if len(stocks) >= limit:
                    break
    return stocks
details = []
def most_young_ceo():
    stocks1=get_most_active_stocks()
    for k in stocks1:
        profile_page = f'https://finance.yahoo.com/quote/{k}/profile/'
        headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
        response = requests.get(profile_page, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        country_parent = soup.find('div', class_="address yf-wxp4ja")
        if country_parent:
            divs = country_parent.find_all('div')
        country = divs[-1].text.strip()
        Employees = soup.find('strong').text.strip()
        count = 0
        table = soup.find('table')
        for row in table.find_all('tr')[1:]:
            cols = row.find_all('td')
            CEO_Name = cols[0].text.strip()
            Name = cols[1].text.strip()
            CEO_Year_Born = cols[4].text.strip()
                        # volume = cols[6].text.strip()
            if count==0:
                details.append({
                        "Name": Name,
                        "Country": country,
                        "Employees": Employees,
                        "CEO_Name": CEO_Name,
                        "CEO_Year_Born": CEO_Year_Born,
                        })
                count+=1
            else:
                break
        # print(row)
    return details
def tabulate():
    details = most_young_ceo()
    df = pd.DataFrame(details)
    sorted_df = df.sort_values("CEO_Year_Born", ascending=False)
    return sorted_df
tabulate()

#2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab. Sheet's fields: Name, Code, 52-Week Change, Total Cash

import requests
from bs4 import BeautifulSoup
import pandas as pd
details1 = []

def scrap_page():
    page = 'https://finance.yahoo.com/markets/stocks/52-week-gainers/?start=0&count=100'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
    response = requests.get(page, headers=headers)
    soup = BeautifulSoup(response.text, 'html')
    stocks2 = []
    table = soup.find('table', class_="markets-table")
    # print(table)
    # limit = 10
    for row in table.find_all('tr')[1:11]:
        link = row.find('a')  # Finding the link in the row
        if link:
            company_code_span = link.find('span', class_="symbol")
            company_name_span = link.find('span', class_="longName")
            
            # Extract company code and name
            company_code = company_code_span.text.strip() if company_code_span else "N/A"
            company_name = company_name_span.text.strip() if company_name_span else "N/A"
        cols = row.find_all('td')
        Week_Change = cols[8].text.strip().replace(',', '').replace('%', '')
        Total_Cash = cols[6].text.strip()
            # CEO_Year_Born = cols[4].text.strip()
                        # volume = cols[6].text.strip()
        details1.append({
                "Name": company_name,
                "code": company_code,
                "52-week change": Week_Change,
                "Total cash": Total_Cash,
                        # "CEO_Year_Born": CEO_Year_Born,
                })
        # limit-=1
        # if limit==0:
        #     break
    
  
    return details1
def weekchange():
    details1 = scrap_page()
    df = pd.DataFrame(details1)
    df['52-week change'] = pd.to_numeric(df['52-week change'], errors='coerce')

    sorted_df = df.sort_values(by="52-week change", ascending=False)
    top_10 = sorted_df.head(10)
    return top_10
    
            
# weekchange()        
weekchange()
            
#3

# 3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
#     Blackrock Inc is an investment management corporation.
#     Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
#     All fields except first two should be taken from Holders tab.

import requests
from bs4 import BeautifulSoup
profile_page = f'https://finance.yahoo.com/quote/BLK/holders/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
        }
response = requests.get(profile_page, headers=headers)
soup = BeautifulSoup(response.text, 'lxml')
with open("webpage_content.txt", "w", encoding="utf-8") as file:
    file.write(response.text)
print("HTML content saved to webpage_content.txt")
import pandas as pd
from bs4 import BeautifulSoup
with open("webpage_content.txt", "r", encoding="utf-8") as file:
    html_content = file.read()
soup = BeautifulSoup(html_content, 'html.parser')
table_section = soup.find('section', {'data-testid': 'holders-top-institutional-holders'})
table = table_section.find('table')
headers = [header.text for header in table.find_all('th')]
rows = []
for row in table.find_all('tr')[1:]:  # Skip the header row
    columns = row.find_all('td')
    rows.append([col.text.strip() for col in columns])
df = pd.DataFrame(rows, columns=headers)
print(df)