from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def fetch_label(driver, value):
    return driver.wait.until(EC.visibility_of_element_located((By.XPATH, value)))

def get_streets(url, cadde_tag, sokak_tag):
    # Set up the Selenium driver
    driver = webdriver.Chrome()
    # Open the URL
    driver.get(url)
    time.sleep(3)

    # Get the cadde names
    cadde_names = driver.find_elements(by=By.XPATH, value=cadde_tag)
    cadde = []

    for cadde_name in cadde_names:
        cadde.append(cadde_name.text)
        
    # split cadde by \n
    cadde = cadde[0].split("\n")
    # if "ile başlayan" is in the list, remove the element
    cadde = [i for i in cadde if "ile başlayan" not in i]
    print(cadde)
    
    # Get the street names
    street_names = driver.find_elements(by=By.XPATH, value=sokak_tag)

    street = []

    for street_name in street_names:
        street.append(street_name.text)
        
    # split street by \n
    street = street[0].split("\n")
    # if "ile başlayan" is in the list, remove the element
    street = [i for i in street if "ile başlayan" not in i]
    print(street)



    # Close the driver
    driver.quit()
    
    return cadde, street
