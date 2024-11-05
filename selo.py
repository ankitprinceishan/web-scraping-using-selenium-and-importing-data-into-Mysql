from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Set up the Selenium WebDriver (make sure you have the appropriate driver installed)
driver = webdriver.Chrome()  # Or use the driver for your browser

# Navigate to the NSE page
driver.get('https://www.nseindia.com/market-data/live-equity-market')

# Wait for the page to load and find the data
stocks = []
rows = driver.find_elements(By.CSS_SELECTOR, 'tr')  # Adjust the selector if needed

for row in rows[1:]:  # Skip the header
    cols = row.find_elements(By.TAG_NAME, 'td')
    if cols:
        stock_data = {
            'Symbol': cols[0].text.strip(),
            'Last Price': cols[1].text.strip(),
            'Change': cols[2].text.strip(),
            'Percentage Change': cols[3].text.strip(),
        }
        stocks.append(stock_data)

# Convert to DataFrame
df = pd.DataFrame(stocks)

# Clean up
driver.quit()

# Check the DataFrame
print(response.text)
