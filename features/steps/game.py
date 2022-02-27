from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.utils import ChromeType
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

chrome_options = Options()
options = [
    "--headless",
    "--disable-gpu",
    "--window-size=1920,1200",
    "--ignore-certificate-errors",
    "--disable-extensions",
    "--no-sandbox",
    "--disable-dev-shm-usage"
]
for option in options:
    chrome_options.add_argument(option)

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)


# options =  webdriver.ChromeOptions()
# driver_path = '../chromedriver.exe'
# driver = webdriver.Chrome(driver_path, chrome_options=options)
driver.implicitly_wait(15)

@given('I set giova as name')
def step_impl(context):  
    driver.get('http://localhost:3000/')
    input=driver.find_element_by_id("name")
    input.send_keys("giova")

@given('Start a game')
def step_impl(context):    
    driver.find_element_by_id("loginBtn").click()

@when('Insert six wrong letters')
def step_impl(context):    
    letras=["k","q","y","x","z","j"]
    inputLetter= driver.find_element_by_id("inputLetter")
    btn=driver.find_element_by_id("btnTry")
    for i in letras:
        inputLetter.clear()
        inputLetter.send_keys(i)
        btn.click()

@then('I see a message that says Perdiste')
def step_impl(context):
    msg= driver.find_element_by_id("gameState").text
    assert "Perdiste" in msg  
    driver.quit()

@when('Insert correct letters')
def step_impl(context):    
    letras=["a","e","i","o","u","s","p","t","l","r","c","m"]
    while(check_exists(driver)):
        inputLetter= driver.find_element_by_id("inputLetter")
        inputLetter.clear()
        inputLetter.send_keys(letras[0])
        driver.find_element_by_id("btnTry").click()
        letras.pop(0)        

@then('I see a message that says Ganaste')
def step_impl(context):
    msg= driver.find_element_by_id("gameState").text
    assert "Ganaste" in msg 
    
def check_exists(driver):
    try:
        driver.find_element_by_id("inputLetter")
    except:        
        return False
    return True