import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy import optimize
from datetime import datetime, timedelta
import requests
import time
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os






driver = webdriver.Firefox()  
wait = WebDriverWait(driver, 10)
driver.get("https://www.instagram.com/accounts/hide_story_and_live_from/")
driver.fullscreen_window()

def input(elem, text):
    elem.clear()
    elem.send_keys(text)
    return



button = driver.find_element(By.CSS_SELECTOR, 'button._a9--._ap36._a9_1')
button.click()
time.sleep(2)
email = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password = wait.until(EC.presence_of_element_located((By.NAME, "password")))

input(email, "")
input(password, "")

button = wait.until(EC.presence_of_element_located((By.XPATH, "//button[.//div[text()='Anmelden']]")))
button.click()
time.sleep(4)
button = wait.until(EC.presence_of_element_located((By.XPATH, "//div[text()='Jetzt nicht' and @role='button']")))
button.click()
time.sleep(1)
user_containers = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"][tabindex="0"]')

# Schleife durch alle Benutzer-Container


time.sleep(1)
try:
    # Warte, bis die Buttons sichtbar sind
    wait = WebDriverWait(driver, 10)
    user_containers = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[role="button"][tabindex="0"]')))

    index = 0
    last_length = 0

    while True:
        if index >= len(user_containers):
            # Aktualisiere die Liste der user_containers
            user_containers = driver.find_elements(By.CSS_SELECTOR, 'div[role="button"][tabindex="0"]')

            # Wenn die Länge der Liste nicht zunimmt, beende die Schleife
            if len(user_containers) == last_length:
                break
            last_length = len(user_containers)

        # Weiter mit dem nächsten user_container
        while index < len(user_containers):
            user_container = user_containers[index]
            index += 1
            print(f"press {index}/{last_length}")
            try:
                # Button innerhalb des Containers finden und klicken
                button = user_container.find_element(By.CSS_SELECTOR, '[aria-label="Kontrollkästchen aktivieren/deaktivieren."]')
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", button)
                button.click()
                # Optional: Wartezeit zwischen den Klicks
                driver.implicitly_wait(2)
            except Exception as e:
                print(f"Fehler beim Klicken des Buttons: {e}")

except Exception as e:
    print("Error: ", e)
finally:
    print("done")
    time.sleep(10)
    driver.quit()
    
print("done mit error")
time.sleep(10)
driver.quit()