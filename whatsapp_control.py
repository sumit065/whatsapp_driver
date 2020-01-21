#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Send multiple messages to a participant

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
# Replace below path with the absolute path of the \
#chromedriver in your computer
driver = webdriver.Chrome('/home/sumit/Downloads/chromedriver')

driver.get("https://web.whatsapp.com/")
# time.sleep()
wait = WebDriverWait(driver, 60)

target = '"Pratap"'

string = 'Hello'

x_arg = '//span[contains(@title,' + target + ')]'
group_title = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
group_title.click()

message = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]

i = 200
while i >= 0:
    message.send_keys(string + str(i))
    sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
    sendbutton.click()
    i -= 1

driver.close()


# In[13]:


#Create Multiple Groups, Exit and Delete the group

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

import time
import sys

driver = webdriver.Chrome('/home/sumit/Downloads/chromedriver')
wait = WebDriverWait(driver, 60)

actionChains = ActionChains(driver)

driver.get("https://web.whatsapp.com/")

i = 0  #Number of groups to  be created
n = 5
  
while i < n:

    print("creating group " + str(i+1) + " of " + str(n))

    x_arg = '//*[@id="side"]/header/div[2]/div/span/div[3]/div/span'
    menu_button = wait.until(EC.presence_of_element_located((By.XPATH, x_arg)))
    menu_button.click()

    new_gr = '//*[@id="side"]/header/div[2]/div/span/div[3]/span/div/ul/li[1]/div'
    wait.until(EC.presence_of_element_located((By.XPATH, new_gr))).click()

    participants = ["Priyadarshi", "Vaibhav"]
    
    contact_search_box = driver.find_elements_by_xpath('//input[@placeholder="Type contact name"]')[0]
    contact_search_box.send_keys(participants[0])

    search_result_xarg = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div/span'
    wait.until(EC.presence_of_element_located((By.XPATH, search_result_xarg))).click()

    contact_search_box = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[1]/div/div/input')[0]
    contact_search_box.send_keys(participants[1])
    
    search_result_xarg = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div/span'
    wait.until(EC.presence_of_element_located((By.XPATH, search_result_xarg))).click()

    next_button_xarg = '//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/span'
    wait.until(EC.presence_of_element_located((By.XPATH, next_button_xarg))).click()

    gr_name_box = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/div[2]/div/div[2]/div/div[2]')[0]
    gr_name_box.send_keys('G1')

    final_tick_button_xarg = driver.find_elements_by_xpath('//*[@id="app"]/div/div/div[2]/div[1]/span/div/span/div/div/span/div/div')[0]
    final_tick_button_xarg.click()

    in_group_menu_button_xarg = '//*[@id="main"]/header/div[3]/div/div[3]'
    wait.until(EC.presence_of_element_located((By.XPATH, in_group_menu_button_xarg))).click()


    exit_xarg = '//*[@id="main"]/header/div[3]/div/div[3]/span/div/ul/li[5]/div'
    wait.until(EC.presence_of_element_located((By.XPATH, exit_xarg))).click()

    time.sleep(0.3)
    driver.find_elements_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')[0].click()


    # current_group = '//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div/div[2]/div[1]/div[1]/span'
    # wait.until(EC.presence_of_element_located((By.XPATH, current_group)))
    # e = driver.find_elements_by_xpath(current_group)[0]
    # actionChains.context_click(e).perform()

    you_left_xarg = '//*[@id="main"]/div[3]/div/div/div[2]/div[3]/div'   
    wait.until(EC.presence_of_element_located((By.XPATH, you_left_xarg)))
    time.sleep(2)
    in_gr_menu_button_xarg = '//*[@id="main"]/header/div[3]/div/div[2]/div'
    wait.until(EC.presence_of_element_located((By.XPATH, in_gr_menu_button_xarg))).click()


    del_gr = '//*[@id="main"]/header/div[3]/div/div[2]/span/div/ul/li[4]/div'
    wait.until(EC.presence_of_element_located((By.XPATH, del_gr))).click()

    time.sleep(0.3)
    conf_delete = driver.find_elements_by_xpath('//*[@id="app"]/div/span[2]/div/div/div/div/div/div/div[2]/div[2]')[0]
    conf_delete.click()
    
    time.sleep(3)
    i = i + 1




