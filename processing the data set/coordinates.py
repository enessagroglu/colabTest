from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


street_names = []
coordinates = []
neigbourhood_and_street = {}

coordinat_path = '/html/body/div[1]/div[2]/div[10]/div[1]/div[1]/div[1]/div/div[1]/div/div/div[3]/div[2]/span[2]/div/div/div/div[1]'


def get_coordinates(url):
    coordinates = []  # Initialize the coordinates list here
    # Set up the Selenium driver
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)  # Wait for the initial page to load

    for neighbourhood, streets in neigbourhood_and_street.items():
        for street in streets:
            full_address = f"{neighbourhood}/{street}"  # Concatenate neighbourhood and street
            
            # Find the search box and enter the full address
            search_box = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/header/div/div/div/form/div[1]/div/span/span/input')
            search_box.send_keys(full_address)
            driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/header/div/div/div/form/div[2]/button').click()
            
            # Wait for the results
            time.sleep(5)
            
            try:
                # Fetch the coordinate data
                coordinate_data = driver.find_element(by=By.XPATH, value=coordinat_path)
                coordinates.append({"address": full_address, "coordinate": coordinate_data.text})
                driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[2]/div[3]/header/div/div/div/form/div[4]/button').click()
            except Exception as e:
                print(f"{full_address} için sonuç bulunamadı.", e)
            
            # Reset the search for the next address
            driver.get(url)
            time.sleep(3)  # Wait for the page to reload
    
    driver.quit()  # Close the driver after all addresses are processed
    return coordinates

def get_coordinates_to_csv(coordinates):
    df = pd.DataFrame(coordinates)
    df.to_csv("./data/coordinates.csv", index=False)

def get_streets_csv():
    df = pd.read_csv("./data/streets.csv")
    # columns names are neighbourhood and street. neighbourhood should be key and street should be value with list
    for index, row in df.iterrows():
        if row[0] in neigbourhood_and_street:
            neigbourhood_and_street[row[0]].append(row[1])
        else:
            neigbourhood_and_street[row[0]] = [row[1]]
    
    



get_streets_csv()
url = "https://yandex.com.tr/maps"
coordinates = get_coordinates(url)
get_coordinates_to_csv(coordinates)

