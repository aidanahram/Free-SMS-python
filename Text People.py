#!/usr/bin/env python
# coding: utf-8

# In[11]:


import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import requests
import bs4
from bs4 import BeautifulSoup
import time
import pyautogui

carriers = {
    'att':    '@txt.att.net',
    'tmobile': '@tmomail.net',
    'verizon':  '@vtext.com',
    'sprint':   '@page.nextel.com'
}

def login(username, passw):
    url = "https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
    bot.get(url)
    time.sleep(3)
    email = bot.find_element_by_class_name('zHQkBf')
    email.send_keys(username)
    next_click = bot.find_element_by_class_name('CwaK9')
    next_click.click()
    time.sleep(1)
    password = bot.find_element_by_class_name('zHQkBf')
    password.send_keys(passw)
    next_click = bot.find_element_by_class_name('CwaK9')
    next_click.click()

def send_text(number, carrier, msg):
    #click compose/ new message
    new_msg = bot.find_element_by_class_name('T-I-KE')
    new_msg.click()
    #click the to section
    to = bot.find_element_by_class_name('vO')
    to.send_keys(number + carriers[carrier])
    #click the message
    message = bot.find_element_by_class_name('editable')
    message.send_keys(msg)
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'enter')
    
bot = webdriver.Chrome()
login('YOUR_USERNAME', 'YOUR_PASSWORD')
time.sleep(3)
send_text('NUMBER', 'CARRIER', 'MESSAGE')





