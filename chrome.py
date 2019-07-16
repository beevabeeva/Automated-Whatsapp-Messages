import time
import datetime as dt
import json
import os
import requests
import shutil
from PIL import Image
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from urllib.parse import urlencode
try:
    from bs4 import BeautifulSoup
except ModuleNotFoundError:
    print("Beautiful Soup Library is reqired to make this library work(For getting participants list for the specified group).\npip3 install beautifulsoup4")

#import pyautogui

#pyautogui.PAUSE = 1 

# Save browser info
info = open("info.txt","w+")

browser = webdriver.Chrome()  # we are using chrome as our webbrowser

# connect to specific instance of chrome
url = browser.command_executor._url
info.write(url+"\n")
# info.write()
session_id = browser.session_id
info.write(session_id)
print("hello teepa"+url+"<--url| session_id--> "+session_id)
# timeout = 10  # The timeout is set for about ten seconds
browser.get("https://web.whatsapp.com/")
# WebDriverWait(self.browser,wait).until(EC.presence_of_element_located(
# (By.CSS_SELECTOR, '._2zCfw')))
info.close() 

