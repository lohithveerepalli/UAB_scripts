from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def login_to_canvas(username, password):
    # URL for Canvas login
    canvas_url = "https://padlock.idm.uab.edu/cas/login?service=https%3A%2F%2Fuab.instructure.com%2Flogin%2Fcas"
    
    # Initialize a Firefox browser instance (you can replace this with Chrome or any other browser)
    browser = webdriver.Firefox()
    browser.get(canvas_url)

    username_field = browser.find_element_by_id("BlazerID")  # Adjust the ID if it's different
    password_field = browser.find_element_by_id("password")  # Adjust the ID if it's different
    
    # Input the provided username and password
    username_field = browser.find_element(By.ID, "BlazerID")
    password_field = browser.find_element(By.ID, "password")
    
    # Submit the form (assuming the login button has a type of "submit")
    password_field.send_keys(Keys.RETURN)

    # Wait for manual verification or further actions
    input("Press Enter to close the browser after you're done...")

    # Close the browser
    browser.quit()

if __name__ == "__main__":
    user = input("Enter your Canvas username: ")
    pwd = input("Enter your Canvas password: ")
    login_to_canvas(user, pwd)
