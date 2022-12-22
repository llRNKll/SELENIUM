'''
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

website = "https://www.somoynews.tv/"
path = "E:\Selenium\Drivers\chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

Container = "//*[@id="app"]/div/div[3]/div[2]/div[5]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div"  //div[@class="container grid-list-xs pa-0"]
title = "//*[@id="app"]/div/div[3]/div[2]/div[5]/div/div/div/div[1]/div[1]/div[1]/div/div[2]/div/div/div/div/div[2]/div/a/span"
location = "//*[@id="app"]/div/div[3]/div[2]/div[5]/div/div/div/div[1]/div[1]/div[3]/div/div[2]/div/div/div/div/div[1]/div[1]/div[1]/a/span"
body = "//*[@id="app"]/div/div[3]/div[2]/div[5]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/a/span"
link = "//*[@id="app"]/div/div[3]/div[2]/div[5]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div[3]/div/div/a"

containers =driver.find_elements(by="xpath", value= )

'''
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.somoynews.tv/"
path = "E:\Selenium\Drivers\chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value= '//div[@class="container grid-list-xs pa-0"]')

titles = []
locations = []
bodies = []
links = []


for container in containers:
    title1 = container.find_element(by="xpath", value= '//div[@class="pt-2 pt-md-3 pb-0 pb-md-3 col-sm-12 col-md-12 col-lg-12 col-12"]').text
    location1 = container.find_element(by="xpath", value= '//div[@class="py-0 col-md-7 col-12').text
    body1 = container.find_element(by="xpath", value= '//div[@class="d-none d-sm-flex"]').text
    link1 = container.find_element(by="xpath", value= '//div[@class="container grid-list-xs pa-0"]/div/div/div/div/div/a').get_attribute("href")

    title2 = container.find_element(by="xpath", value= '//div[@class="pa-0 mb-0 mb-md-2 col col-12"]').text
    location2 = container.find_element(by="xpath", value= '//div[@class="d-flex pa-0 col col-12"]').text
    body2 = container.find_element(by="xpath", value= '//div[@class="pa-0 mb-3 col col-12"]').text
    link2 = container.find_element(by="xpath", value= '//div[@class="container grid-list-xs pa-0"]/div/a').get_attribute("href")

    titles.append(title1,title2)
    locations.append(location1,location2)
    bodies.append(body1,body2)
    links.append(link1,link2)

my_dict = {'titles' : titles, 'location' : locations , 'body' : bodies , 'link' : links}
somoy_tv = pd.DataFrame(my_dict)
somoy_tv.to_csv('somoy.csv')

driver.quit()
'''

#containers =driver.find_elements(by="xpath", value= )

'''
M_Container = "//div[@class="row"]"
M_title = "//div[@class="pt-2 pt-md-3 pb-0 pb-md-3 col-sm-12 col-md-12 col-lg-12 col-12"]"
M_location = "//div[@class="py-0 col-md-7 col-12"]"
M_body = "//div[@class="d-none d-sm-flex"]"
M_link = "//div[@class="container grid-list-xs pa-0"]/div/div/div/div/div/a"

Container = "//div[@class="container grid-list-xs pa-0"]"
title = "//div[@class="pa-0 mb-0 mb-md-2 col col-12"]"
location = "//div[@class="d-flex pa-0 col col-12"]"
body = "//div[@class="pa-0 mb-3 col col-12"]"
link = "//div[@class="container grid-list-xs pa-0"]/div/a"
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd

website = "https://www.somoynews.tv/"
path = "E:\Selenium\Drivers\chromedriver"

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

containers = driver.find_elements(by="xpath", value= '//div[@class="container grid-list-xs pa-0"]')

titles = []
locations = []
bodies = []
links = []


for container in containers:
    

    title2 = container.find_element(by="xpath", value= '//div[@class="pa-0 mb-0 mb-md-2 col col-12"]').text
    location2 = container.find_element(by="xpath", value= '//div[@class="d-flex pa-0 col col-12"]').text
    body2 = container.find_element(by="xpath", value= '//div[@class="pa-0 mb-3 col col-12"]').text
    link2 = container.find_element(by="xpath", value= '//div[@class="container grid-list-xs pa-0"]/div/a').get_attribute("href")

    titles.append(title2)
    locations.append(location2)
    bodies.append(body2)
    links.append(link2)

my_dict = {'titles' : titles, 'location' : locations , 'body' : bodies , 'link' : links}
somoy_tv = pd.DataFrame(my_dict)
somoy_tv.to_csv('somoy.csv')

driver.quit()