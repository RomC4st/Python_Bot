from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
from os.path import join, dirname
import os
import sys

# load dotenv path 
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# change download directory
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' :os.getenv("DOWNLOAD_DIR") }
chrome_options.add_experimental_option('prefs', prefs)
# execute webdriver in silent mode
chrome_options.headless = True
# initialize chrome webdriver with options
driver = webdriver.Chrome(os.getenv("WEBDRIVER_PATH"),chrome_options=chrome_options)

# define ID 
usernameStr = os.getenv("ID_USERNAME")
passwordStr = os.getenv("ID_PASSWORD")

# start bot
driver.get((os.getenv("TARGET_URL")))
try:
  username = driver.find_element_by_id('user')
  username.send_keys(usernameStr)
  password = driver.find_element_by_id('password')
  password.send_keys(passwordStr)
  signInButton = driver.find_element_by_id('login')
  signInButton.click()
  acceptCondition = WebDriverWait(driver, 10).until(
  EC.presence_of_element_located((By.ID, 'sncmp-popup-ok-button')))
  acceptCondition.click()
  # file download
  driver.get(os.getenv("DOWNLOAD_LINK"))  
except:
  print('An exception occured')
  sys.exit()

print('ok')
sys.exit()
