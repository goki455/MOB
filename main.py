from selenium import webdriver
from pushsafer import Client
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

#Chrome options



client = Client("bjHKdba7y0Hj8LRlRs3i")


chromedriver_autoinstaller.install()
#Chrome options

options1 = webdriver.ChromeOptions() #try

options1.add_argument("--disable-extensions")
options1.add_experimental_option("useAutomationExtension", False)
options1.add_argument("--proxy-bypass-list=*")
options1.add_argument("--disable-gpu")
options1.add_argument("--headless")
options1.add_argument("--window-size=1920,1080")
options1.add_argument("no-sandbox")
options1.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36')
options1.add_argument('--ignore-certificate-errors')
options1.add_argument('--allow-running-insecure-content')
driver = webdriver.Chrome(options=options1)







Url = ("https://www.mobile.de/")

driver.get(Url)
#buttonc = driver.find_element(By.XPATH, '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button')
#buttonc.click()
sleep(10.0)
def Try():
    try:
        buttonc = driver.find_element(By.XPATH, '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button')
        buttonc.click()
    except:
        return
Try()
#buttonc = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/button')
#buttonc.click()
sleep(5.0)


sleep(5.0)
#Marke_input=input("Welche Marke? :")
WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[1]/div'))).click()

#Marke_pusc = driver.find_element(By.CSS_SELECTOR , '#root > div.hp7JS > div > article.RSseD._3LZ_7._2iEKW > section > div > div.UiAUP > div > div:nth-child(1) > div > select')
Marke_push = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[1]/div')
ActionChains(driver).move_to_element(Marke_push).click(Marke_push).perform()

sleep(5.0)
Marke_push.send_keys("Audi")
sleep(5.0)
Marke_push.click()

#Model_input = input("Welches Modell ? :")
Model_push = driver.find_element(By.CSS_SELECTOR , '#root > div.hp7JS > div > article.RSseD._3LZ_7._2iEKW > section > div > div.UiAUP > div > div:nth-child(2) > div > select')
Model_push.click()
Model_push.send_keys("S3")

#KM_input = input("Wie viel Kilometer ? :")
KM_push = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[4]/div/div[1]/input')
#KM_push.click()
KM_push.send_keys("100000")
#Price_input = input("Wie viel soll er kosten ? :")
Price_push = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[6]/div/div[1]/input')
#Price_push.click()
Price_push.send_keys("9000")
#GPS_butt = driver.find_element(By.XPATH , '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[7]/span/span')
#GPS_butt.click()
sleep(3.0)

# Funktion für die Plausibilisierung

span_element = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[8]/button/span/span/span')
valueget = (span_element.text[0])
sleep(4.0)

if valueget >= "0":
    sleep(8.0)
    next_c = driver.find_element(By.XPATH, '//*[@id="root"]/div/div/article[1]/section/div/div[2]/div/div[8]').click()
    sleep(8.0)
    driver.find_element(By.XPATH, '//*[@id="main-header"]/div[2]/nav/div/ul[1]/li[3]/ul/li[1]/a').get_attribute("href")

    resp = client.send_message("NEW_Car", "Neues Auto", "a", "1", "4", "2", driver.find_element(By.XPATH, '//*[@id="main-header"]/div[2]/nav/div/ul[1]/li[3]/ul/li[1]/a').get_attribute("href") ,
                                 "Mobile öffnen!", "0", "2", "60", "600", "1", "", "", "")


else:
    print("Keine Ergebnisse")
