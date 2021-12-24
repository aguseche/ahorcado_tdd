from behave import *
from selenium import webdriver

options =  webdriver.ChromeOptions()
driver_path = 'C:/Users/Usuario/py/Agiles/ahorcado_tdd/features/chromedriver.exe'
driver = webdriver.Chrome(driver_path, chrome_options=options)
driver.implicitly_wait(15)

@given('I am on the login page')
def step_impl(context):  
    driver.get('http://localhost:3000/')
    
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
    assert msg is not " "
    driver.quit()