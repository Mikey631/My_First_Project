from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(r'C:\Users\Evaax\eclipse-workspace\Example\PythonScripts\chromedriver.exe')

browser.get('https://na01.safelinks.protection.outlook.com/?url=https%3A%2F%2Fwww.myworkday.com%2Fumiami%2Femail%2Finst%2F9193%24604734%2Frel-task%2F2997%241605.htmld&data=02%7C01%7Cm.martinez28%40med.miami.edu%7C8bddb1d9cb9e4389a39a08d4f178df26%7C2a144b72f23942d48c0e6f0f17c48e33%7C0%7C0%7C636398948823561548&sdata=FlYpmDVSKrIhIxLflXmhu%2FroHRwJF0EQNiKw4UoeoEo%3D&reserved=0')

Cur_url = browser.current_url
if  Cur_url == 'https://caneid.miami.edu/cas/login?service=https%3A%2F%2Fcaneid.miami.edu%2Fidp%2FAuthn%2FMCB%2FRemoteUser': 
    print('redirected')
    
    UserName = browser.find_element_by_css_selector('#nameInitialFocus')
    UserName.send_keys('m.martinez28')
    PassWord = browser.find_element_by_css_selector('#wrap > div.container > div > form > input:nth-child(7)')
    PassWord.send_keys('4r5ry7y7M$#')
    
    elem1 = browser.find_element_by_css_selector('#wrap > div.container > div > form > button')
    elem1.click()
else:
    print('error')
    
#browser.get(browser.current_url)
#wait = WebDriverWait(browser, 10)
#element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,"#login-form > fieldset:nth-child(11) > div.row-label.push-label > button")))
#print('found?')
#element.click()
WebDriverWait(browser, 15)
elem2 = browser.find_element_by_css_selector('#login-form > fieldset:nth-child(11) > div.row-label.push-label > button')
elem2.click()
