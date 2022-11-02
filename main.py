from selenium import webdriver
from pushsafer import Client
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options

#Chrome options



client = Client("bjHKdba7y0Hj8LRlRs3i")


chromedriver_autoinstaller.install()
#Chrome options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--window-size=1920,1080")
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)







Url = ("https://www.mobile.de/")

driver.get(Url)

sleep(4.0)
buttonc = driver.find_element(By.XPATH , '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button')

buttonc.click()
sleep(2.0)
#Marke_input=input("Welche Marke? :")
Marke_push = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[1]/div/select').send_keys("Audi")
#Model_input = input("Welches Modell ? :")
Model_push = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[2]/div/select').send_keys("S3")
#KM_input = input("Wie viel Kilometer ? :")
KM_push = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[4]/div/div[1]/input').send_keys("100000")
#Price_input = input("Wie viel soll er kosten ? :")
Price_push = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[6]/div/div[1]/input').send_keys("35000")
#GPS_butt = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[7]/span/span')
#GPS_butt.click()
sleep(3.0)

# Funktion für die Plausibilisierung

span_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[8]/button/span/span/span')
valueget = (span_element.text[0])


if valueget >= "0":
    next_c = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[8]/button')
    next_c.click()
    sleep(8.0)

    get_URL = driver.find_element(By.XPATH, '//*[@id="main-header"]/div[2]/nav/div/ul[1]/li[3]/ul/li[1]/a').get_attribute("href")

    resp = client.send_message("NEW_Car", "Neues Auto", "a", "1", "4", "2", get_URL ,
                                 "Mobile öffnen!", "0", "2", "60", "600", "1", "", "", "")


else:
    print("Keine Ergebnisse")



