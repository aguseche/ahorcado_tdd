from behave import *
from selenium import webdriver

# options =  webdriver.ChromeOptions()

driver_path = 'features/chromedriver.exe'
driver = webdriver.Chrome(driver_path)
driver.implicitly_wait(15)

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
    msg= driver.find_element_by_id("palabra").text
    assert "a" in msg    

@when('Insert letter x')
def step_impl(context):    
    inputLetter= driver.find_element_by_id("inputLetter")
    inputLetter.send_keys("x")


@then('Letter shows in incorrect array')
def step_impl(context):
    msg= driver.find_element_by_id("letrasIncorrectas").text
    assert "x" in msg    
    driver.quit()
    
