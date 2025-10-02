from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ---------------------------------------- scraping --------------------------------------------------------------------

G_FORM_URL = 'YOUR GOOGLE FORM LINK '
SITE_URL = "https://appbrewery.github.io/Zillow-Clone/"

# sending request to get HTML :
response = requests.get(SITE_URL)
content = response.text

# creating soup for scraping:
soup = BeautifulSoup(content, "html.parser")
# print(soup.prettify())


# finding all links to the property:
links = [link.get('href') for link in soup.find_all('a', class_="property-card-link")]
# print(links)

# finding all price per month:
prices = [price.text.strip().split('+')[0].split('/')[0] for price in
          soup.find_all('span', class_='PropertyCardWrapper__StyledPriceLine')]
# print(prices)

# finding all the addresses:
addresses = [address.text.strip().replace('|', ',') for address in soup.find_all('address')]
# print(addresses)


# --------------------------------------------- bot --------------------------------------------------------------------

# initializing:
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)

# start:

driver.get(G_FORM_URL)

for i in range(len(links)):
    if i >= 0:

        # wait till page loads:
        print(f"saving results in sheet....{i + 1}")
        time.sleep(2)

        address_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div['
                                                      '2]/div/div[2]/div['
                                                      '1]/div/div/div[2]/div/div['
                                                      '1]/div/div['
                                                      '1]/input')

        price_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div['
                                                    '2]/div/div[2]/div['
                                                    '2]/div/div/div[2]/div/div['
                                                    '1]/div/div[1]/input')

        link_field = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div['
                                                   '2]/div/div[2]/div['
                                                   '3]/div/div/div[2]/div/div['
                                                   '1]/div/div[1]/input')

        submit_button = WebDriverWait(driver, 6).until(
            EC.presence_of_element_located((By.XPATH, './/span[text()="Submit"]')))

        address_field.send_keys(addresses[i])
        price_field.send_keys(prices[i])
        link_field.send_keys(links[i])
        submit_button.click()
        driver.find_element(By.LINK_TEXT, "Submit another response").click()

print("All results saved in sheet\n")
driver.quit()
