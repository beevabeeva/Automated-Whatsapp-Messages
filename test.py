
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




from whatsapp import WhatsApp
whatsapp = WhatsApp()
print(whatsapp.send_message("Niambh","teepa!"))  
# whatsapp.close()


