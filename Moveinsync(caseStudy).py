from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

# Open the website
driver.get("https://demoqa.com/login")

try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "login")))

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    username_input = driver.find_element(By.ID, "userName")
    username_input.clear()
    username_input.send_keys("pasumarthykomal")  

    password_input = driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys("Pkomal@06#")  

    login_button = driver.find_element(By.ID, "login")
    login_button.click()


    WebDriverWait(driver, 10).until(EC.url_changes(driver.current_url))

  
    print("Login successful!")

except Exception as e:
    print("An error occurred:", e)
finally:
    driver.quit()

