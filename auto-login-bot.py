#make env for selenim first if you using linux then fill all details
from selenium import webdriver

def startBot(username, password, url):
    
    path_to_chromedriver = "fill your chromedriver path here"

    
    driver = webdriver.Chrome(executable_path=path_to_chromedriver)

    #dont fill any thing here
    driver.get(url)

    
    username_field = driver.find_element_by_name("username_field_name")
    username_field.send_keys(username)

    password_field = driver.find_element_by_name("password_field_name")
    password_field.send_keys(password)

    
    login_button = driver.find_element_by_css_selector("login_button_css_selector")
    login_button.click()

#fill this with your choice 
username = "YourUsername"
password = "YourPassword"
url = "URL_of_the_login_page_where_you want_to autologin"


startBot(username, password, url)
