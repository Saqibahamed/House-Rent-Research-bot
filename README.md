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
## 📌 Usage
1.The bot will:

  - Scrape all property links, prices, and addresses from the site.

  - Open the Google Form in Chrome.

  - Automatically fill in each form submission.

  - Click "Submit" and "Submit another response" for all entries.

2.After completion, Chrome will close automatically, and all results will be saved in the excel sheet which is linked with Google form

