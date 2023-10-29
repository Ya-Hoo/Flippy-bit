# ============================================================= #
# ========================== Library ========================== #
# ============================================================= #
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
import time, os


# ============================================================= #
# ======================= Load browser ======================== #
# ============================================================= #
browser = webdriver.Chrome()
url = "https://flippybitandtheattackofthehexadecimalsfrombase16.com/"
browser.get(url)
browser.maximize_window()
wait=WebDriverWait(browser,10)
wait.until(EC.presence_of_element_located((By.TAG_NAME,"html")))

html = browser.find_element(By.TAG_NAME, 'html')


# ============================================================= #
# ========================= Functions ========================= #
# ============================================================= #
def neutraliseTarget(hexNum):
    keys = "asdfghjk"
    bin_val = ""
    conversion = {
        "0":"0000",
        "1":"0001",
        "2":"0010",
        "3":"0011",
        "4":"0100",
        "5":"0101",
        "6":"0110",
        "7":"0111",
        "8":"1000",
        "9":"1001",
        "A":"1010",
        "B":"1011",
        "C":"1100",
        "D":"1101",
        "E":"1110",
        "F":"1111",
    }
    for byte in hexNum:
        bin_val += conversion[byte]
    
    # Work from backwards
    for i in range(1, len(bin_val)+1):
        if bin_val[-i] == '1':
            key = keys[-i]
            html.send_keys(key)
            time.sleep(0.01) # Another stroke prevention


# ============================================================= #
# =========================== Game ============================ #
# ============================================================= #
time.sleep(4)
html.send_keys(Keys.ENTER)

# Bot's brain
while "game-over" not in browser.find_element(By.TAG_NAME, 'html').get_attribute('class'):
    try:
        enemies = [enemy for enemy in browser.find_elements(By.CLASS_NAME, 'enemy')
                    if "under-attack" not in enemy.get_attribute('class')]
        if len(enemies) > 0:
            for enemy in enemies:
                neutraliseTarget(enemy.text)
    except StaleElementReferenceException:  # Ignore enemies who's targetted but haven't been hit
        time.sleep(3)


# Data recording
score = browser.find_element(By.ID, 'score').text
file_path = rf"{os.getcwd()}\bot\KILO-edByte\log.txt"
with open(file_path, 'a') as f:
    f.write(f"{score}\n")