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
wait = WebDriverWait(browser,10)
# wait until everything is loaded
wait.until(EC.presence_of_element_located((By.TAG_NAME,"html")))

html = browser.find_element(By.TAG_NAME, 'html')


# ============================================================= #
# ========================= Functions ========================= #
# ============================================================= #
def neutraliseTarget(hexNum):
    # hex : [leftKeyInput, rightKeyInput]
    conversion = {
        "0":["",""], "1":["f","k"], "2":["d","j"], "3":["df","jk"],
        "4":["s","h"], "5":["sf","hk"], "6":["sd","hj"], "7":["sdf","hjk"],
        "8":["a","g"], "9":["af","gk"], "A":["ad","gj"], "B":["adf","gjk"],
        "C":["as","gh"], "D":["asf","ghk"], "E":["asd","ghj"], "F":["asdf","ghjk"]
    }
    html.send_keys(''.join([conversion[byte][(index + 1) // len(hexNum)] for index, byte in enumerate(hexNum)]))


# ============================================================= #
# =========================== Game ============================ #
# ============================================================= #
time.sleep(4)
html.send_keys(Keys.ENTER)

while "game-over" not in browser.find_element(By.TAG_NAME, 'html').get_attribute('class'):  # Thinking waves
    try:
        enemies = [enemy for enemy in browser.find_elements(By.CLASS_NAME, 'enemy')
                   if "under-attack" not in enemy.get_attribute('class')]
        if len(enemies) > 0:
            for enemy in enemies:
                neutraliseTarget(enemy.text)
    # Ignore enemies who's targetted but haven't been hit
    except StaleElementReferenceException:
        time.sleep(0.001)
        
# Data recording
score = browser.find_element(By.ID, 'score').text
file_path = rf"{os.getcwd()}\bot\MEGA-edByte\log.txt"
with open(file_path, 'a') as f:
    f.write(f"{score}\n")