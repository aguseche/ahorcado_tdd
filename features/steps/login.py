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
driver.implicitly_wait(10)

@given('I am on the login page')
def step_impl(context):  
    driver.get('https://ahorcado-agiles.netlify.app/')
    
@when('I set "{name}" as name')
def step_impl(context,name):    
    input=driver.find_element_by_id("name")
    input.send_keys(name)

@when('I press the login button')
def step_impl(context): 
    driver.find_element_by_id("loginBtn").click()

@then('I see a message that says "{msg}"')
def step_impl(context,msg):    
    error=driver.find_element_by_id("errorLogin").text
    assert msg in error

@when('I set Agustin as name')
def step_impl(context):    
    input=driver.find_element_by_id("name")
    input.send_keys("Agustin")

@then('Start the game')
def step_impl(context):    
    msg=driver.find_element_by_id("palabra").text
    assert msg != " "
    driver.quit()