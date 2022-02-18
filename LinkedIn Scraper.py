#Importing the required libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from bs4 import BeautifulSoup

driver = webdriver.Chrome("chromedriver")

#Getting the career guide page
driver.get("https://www.careerguide.com/career-options")

soup = BeautifulSoup(driver.page_source,'html.parser')

#Scraping the desired career
careers = soup.find_all('a', {'title': 'Airline Pilot'})
keywords = []
for i in careers:
    keywords.append(i.text)


#Opening linkedIn's login page
driver.get("https://linkedin.com/uas/login")
  
#Waiting for the page to load
sleep(5)
  

username = driver.find_element_by_id("username")
  
#Entering Email Address/Username
username.send_keys("email address/username")  
  

pw = driver.find_element_by_id("password")
  
#Entering password
pw.send_keys("password")        
  
#Clicking on the log in button
driver.find_element_by_xpath("//button[@type='submit']").click()
jobs = driver.find_element_by_xpath("//a[@data-link-to='jobs']/span")
jobs.click()
sleep(5)

#Finding the keywords/location search bars:
search_bars = driver.find_elements_by_class_name('jobs-search-box__text-input')
search_keywords = search_bars[0]

#Searching scraped jobs
search_keywords.send_keys(keywords)
driver.find_element_by_xpath("/html/body/div[6]/header/div/div/div/div[2]/button[1]").click()

#Scraping the required details
title = driver.find_elements(By.CLASS_NAME,"job-card-list__title")
#Job Title
job_title = []
for i in title:
    job_title.append(i.text)


company = driver.find_elements(By.CLASS_NAME,"job-card-container__link")
#Company Name
comp_name = []
for i in company:
    comp_name.append(i.text)


location = driver.find_elements(By.CLASS_NAME,"job-card-container__metadata-item")
#Location
loc_name = []
for i in location:
    loc_name.append(i.text)
