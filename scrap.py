import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for the NSE stock data (example for NIFTY 50)
url = 'https://www.nseindia.com/market-data/live-equity-market'

# Create a session to handle cookies
session = requests.Session()

# Set headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
}

# Make the request
response = session.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the relevant data
    # This will vary based on the actual structure of the HTML
    stocks = []
    for row in soup.find_all('tr')[1:]:  # Skip the header row
        cols = row.find_all('td')
        stock_data = {
            'Symbol': cols[0].text.strip(),
            'Last Price': cols[1].text.strip(),
            'Change': cols[2].text.strip(),
            'Percentage Change': cols[3].text.strip(),
        }
        stocks.append(stock_data)

    # Convert to DataFrame
    df = pd.DataFrame(stocks)

    # Print or save the DataFrame
    print(df)
else:
    print(f"Failed to retrieve data: {response.status_code}")
