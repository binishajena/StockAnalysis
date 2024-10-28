
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

class StockSearchAgent:
    def __init__(self, driver_path):
        # WebDriver
        self.driver = webdriver.Chrome(executable_path=driver_path)

    def search_top_stocks(self, url="https://finance.yahoo.com/"):
        # finance website
        self.driver.get(url)
        time.sleep(3)  # Wait for the page to load
        
        try:
            top_stocks_button = self.driver.find_element(By.LINK_TEXT, "Top Gainers")
            top_stocks_button.click()
            time.sleep(3)  # Wait for the page to load after clicking
            
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            top_stocks = self.extract_top_stocks(soup)
            
            return top_stocks
        
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        finally:
            self.driver.quit()
    
    def extract_top_stocks(self, soup):
        stock_list = []
        try:
            rows = soup.find_all('tr', {'class': 'simpTblRow'})
            for row in rows[:10]:  # Get top 10 rows
                stock_info = row.find_all('td')
                if len(stock_info) > 1:
                    symbol = stock_info[0].text.strip()
                    name = stock_info[1].text.strip()
                    price = stock_info[2].text.strip()
                    change = stock_info[3].text.strip()
                    percent_change = stock_info[4].text.strip()
                    
                    stock_list.append({
                        "Symbol": symbol,
                        "Name": name,
                        "Price": price,
                        "Change": change,
                        "Percent Change": percent_change
                    })
            return stock_list
        except Exception as e:
            print(f"Failed to extract stocks: {e}")
            return []

# Usage Example
if __name__ == "__main__":
    driver_path = "C:\\Users\\Binisha\\Downloads\\chromedriver.exe"
    agent = StockSearchAgent(driver_path)
    top_stocks = agent.search_top_stocks()
    if top_stocks:
        for stock in top_stocks:
            print(stock)
