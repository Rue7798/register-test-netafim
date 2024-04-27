from behave import *
from playwright.sync_api import sync_playwright, expect
import behave_webdriver



browser= sync_playwright().start().chromium.launch(headless=False)
context =  browser.new_context()
page = context.new_page()
page.goto('http://automationexercise.com')
username="Rue"


@given('the user is on the homepage')
def userOnHomepage(context):
     expect(page.locator('id=slider')).to_be_visible()

@when('the user clicks on the "Signup / Login" button')
def userClicksSignup(context):
    page.locator('[href*="/login"]').click()

@then('the "New User Signup!" is displayed')
def userSignupVisible(context):
    expect(page.get_by_text("New User Signup!")).to_be_visible()
    
@when ('the user enters their name and email address')
def enterNameEmail(context):
     page.locator('input[data-qa="signup-name"]').fill(username)
     page.locator('input[data-qa="signup-email"]').fill("Rue2365@gmail.com")


@when ('clicks the "Signup" button')
def clickSignupBtn(context):
     page.get_by_role("button", name="Signup").click()

@then('the "ENTER ACCOUNT INFORMATION" page is displayed')
def accInfoVisible(context):
     expect(page.get_by_text("Enter Account Information")).to_be_visible

@when ('the user fills in the account information')
def fillAccInfo(context):
    page.locator('id=id_gender2').click()
    page.locator('input[data-qa="name"]').fill(username)
    page.locator('input[data-qa="password"]').fill("R123!")
    page.locator('select[data-qa="days"]').select_option(['6'])
    page.locator('select[data-qa="months"]').select_option(['9'])
    page.locator('select[data-qa="years"]').select_option(['1992'])

      
@when ('user selects the checkboxes')
def selectCheckbock(context):
    page.locator('id=newsletter').check()
    page.locator('id=optin').check()
    
@when ('user fills in the personal information')
def fillPersoanlInfo(context):
     page.locator('input[data-qa="first_name"]').fill("Rue")
     page.locator('input[data-qa="last_name"]').fill("Rue")
     page.locator('input[data-qa="company"]').fill("Netafim")
     page.locator('input[data-qa="address"]').fill("Northern Israel")
     page.locator('input[data-qa="address2"]').fill("Haifa")
     page.locator('select[data-qa="country"]').select_option(['Israel'])
     page.locator('input[data-qa="state"]').fill("Northern District")
     page.locator('input[data-qa="city"]').fill("Haifa")
     page.locator('input[data-qa="zipcode"]').fill("3478403")
     page.locator('input[data-qa="mobile_number"]').fill("0541234567")

  
@when ('user clicks the "Create Account" button')
def clickBtn(context):
     page.locator('button[data-qa="create-account"]').click()

    
@then ('the "ACCOUNT CREATED!" message is visible')
def AccCreatedMsg(context):
     expect(page.locator('[data-qa="account-created"]')).to_be_visible()

    
@when ('the user clicks the "Continue" button')
def ClickContinueBtn(context):
     page.locator('a[data-qa="continue-button"]').click()
    
@then ('the "Logged in as username" is visible')
def LoggedMsgVisible(context):
     expect(page.get_by_text(username)).to_be_visible()

    
@when ('the user clicks the "Delete Account" button')
def ClickDeleteBtn(context):
     page.locator('[href*="/delete_account"]').click()



@then ('the "ACCOUNT DELETED!" message is displayed')
def AccDeletedMsg(context):
     expect(page.locator('[data-qa="account-deleted"]')).to_be_visible()

    
@then ('the user clicks the "Continue" button')
def ClickContinueBtn(context):
     page.locator('a[data-qa="continue-button"]').click()

    

async def after_all(context):
     page.close()
     browser.close()
    
    
