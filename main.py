#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 12 17:41:33 2022

@author: zhangziqi
"""

import numpy as np
import pandas as pd
from selenium import webdriver
import time
import os
from urllib import request
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

os.chdir("/Users/zhangziqi/Documents/Stats/295/")

output = []

save_path = "likedin"


if ~ os.path.exists(save_path):

    url = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"
    driver = webdriver.Chrome('/Users/zhangziqi/Documents/Stats/295/chromedriver')
    driver.get (url)
    driver.maximize_window()
    driver.find_element_by_id("username").send_keys('#email')
    driver.find_element_by_id("password").send_keys('#key')
    driver.find_element_by_xpath('//button[@type = "submit"]').click()
    time.sleep(4)
    
    mian_soup = BeautifulSoup(driver.page_source, 'lxml')
    candidate_name = mian_soup.find_all("div", {"class": "t-16 t-black t-bold"}) 
    candidate_link = mian_soup.find_all("a", {"class" : "ember-view block"})
    output.append(candidate_name[0].get_text().strip())
    output.append("\n")
    output.append("https://www.linkedin.com" + candidate_link[0]['href'])
    output.append("\n")
    
    driver.find_element_by_xpath('//a[@href="/messaging/"]').click()
    time.sleep(2)
    scroll = driver.find_element_by_xpath("//ul[@class='list-style-none msg-conversations-container__conversations-list']")
    verical_ordinate = 100
    for i in range(0, 30):
        driver.execute_script("arguments[0].scrollTop = arguments[1]", scroll, verical_ordinate)
        verical_ordinate += 100
        time.sleep(0.1)
    buttons = driver.find_elements_by_xpath('//a[@class="ember-view msg-conversation-listitem__link msg-conversations-container__convo-item-link pl3"]')

    count = 1
    for i in range(len(buttons)):
        buttons[i].click()
        time.sleep(1)
        message_soup = BeautifulSoup(driver.page_source, 'lxml')
        
        names = message_soup.find_all("span", {"class": "msg-s-message-group__name t-14 t-black t-bold hoverable-link-text"}) 
        times = message_soup.find_all("time", {"class": "msg-s-message-group__timestamp white-space-nowrap t-12 t-black--light t-normal"}) 
        messg = message_soup.find_all("p", {"class": "msg-s-event-listitem__body t-14 t-black--light t-normal"}) 
        
        
        if len(names) > 0:
            output.append("Conversation " + str(count))
            output.append("\n")
            for j in range(len(names)):
                output.append(names[j].get_text().strip())
                output.append("\n")
                output.append(times[j].get_text().strip())
                output.append("\n")
                output.append(messg[j].get_text())
                output.append("\n")
            count += 1
            output.append("\n")
        
        
    
    res = " ".join(output)
        
with open("output", "w") as f:
    f.write(res)             
    
driver.close()
    
   
    
    
    
   

