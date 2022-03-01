from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
# driver_path = 'features/chromedriver.exe'
# driver = webdriver.Chrome(driver_path, chrome_options=options)
driver.implicitly_wait(10)

@given('I set damian as name')
def step_impl(context):  
    driver.get('https://ahorcado-agiles.netlify.app/')
    input=driver.find_element_by_id("name")
    input.send_keys("damian")

@given('Start a gamee')
def step_impl(context):    
    driver.find_element_by_id("loginBtn").click()

@when('Insert letter a')
def step_impl(context):    
    inputLetter= driver.find_element_by_id("inputLetter")
    inputLetter.send_keys("a")

@when('Try letter')
def step_impl(context): 
    driver.find_element_by_id("btnTry").click()

@then('Letter shows in word')
def step_impl(context):
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "palabra"),"a"))
    msg= driver.find_element_by_id("palabra").text
    print(msg)
    assert "a" in msg    

@when('Insert letter x')
def step_impl(context):    
    inputLetter= driver.find_element_by_id("inputLetter")
    inputLetter.send_keys("x")


@then('Letter shows in incorrect array')
def step_impl(context):
    WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element((By.ID, "letrasIncorrectas"),"x"))
    msg= driver.find_element_by_id("letrasIncorrectas").text
    assert "x" in msg    
    driver.quit()
    
