# House-Rent-Research-bot 🏡
This is a project is a web scraping + Google Forms automation bot that collects property data (links, prices, addresses) from a Zillow clone site and submits it into a Google Form using Selenium.

It combines **BeautifulSoup** for web scraping and **Selenium** for browser automation.

---

## 🚀 Features
- Scrapes property **links**, **prices**, and **addresses** from a Zillow clone site.
- Automatically submits the data into a **Google Form**.
- Handles multiple listings efficiently using Selenium.
- Waits for page elements to load before interacting, reducing errors.

---

## 📂 Project Structure
```
├── main.py # Main script for scraping and submitting to Google Form
├── requirements.txt # Python dependencies

```

## 🛠️ Requirements
- Python 3.8+
- Google Chrome browser
- ChromeDriver (matching your Chrome version)
- Python libraries:
  - beautifulsoup4
  - requests
  - selenium  

Install them with:
```bash
pip install -r requirements.txt
```
---

## 🔑 Setup

1️⃣ Open Project in PyCharm

  Launch PyCharm.

  Go to File → Open.

  Select your project folder (downloaded from repo) and click OK.

2️⃣ Create a Virtual Environment

  Go to File → Settings → Project: YourProjectName → Python Interpreter.

  Click the gear icon → Add.

  Select Virtualenv Environment:

  New environment (recommended)

  Location: leave default (e.g., .venv)

  Base interpreter: choose your Python 3.x installation

  Click OK to create the virtual environment.

3️⃣ Install Dependencies

  Open Terminal in PyCharm (bottom of IDE).

  Run:
  ```
  pip install spotipy beautifulsoup4 requests python-dotenv
  ```

  Or, if you want, you can create a requirements.txt file (with these 4 libraries) and run:
  ```
  pip install -r requirements.txt
  ```

4️⃣ Configure Run in PyCharm

  Go to Run → Edit Configurations → + → Python.

  Name it: Run House Rent Bot.

  ```
  Script path: main.py.
  ```
  Python interpreter: select the virtualenv you created.

  Working directory: project root.

  Click OK.

5️⃣ Run the Project

  Click the green Run button (top right) or press Shift + F10.
---
## 📌 Code
```
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


```
---
## 📌 Usage
1.The bot will:

  - Scrape all property links, prices, and addresses from the site.

  - Open the Google Form in Chrome.

  - Automatically fill in each form submission.

  - Click "Submit" and "Submit another response" for all entries.

2.After completion, Chrome will close automatically, and all results will be saved in the excel sheet which is linked with Google form

---
## ⚠️ Notes
  - Make sure your Google Form fields match the XPaths in the code. Adjust if necessary.

  - The script uses time.sleep and explicit waits to handle page load delays.

  - ChromeDriver must match your Chrome version to avoid errors.

---
## 🙌 Credits
- BeautifulSoup
 for scraping

- Selenium
 for browser automation

- Zillow clone site for demo data (App Brewery Zillow Clone)
