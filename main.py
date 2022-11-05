from selenium import webdriver
from pushsafer import Client
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#
#Chrome options#
client = Client("bjHKdba7y0Hj8LRlRs3i")
#push
#
chromedriver_autoinstaller.install()
#Chrome options

options1 = webdriver.ChromeOptions() #try

options1.add_argument("--disable-extensions")
options1.add_experimental_option("useAutomationExtension", False)
options1.add_argument("--proxy-bypass-list=*")
#options1.add_argument("--disable-gpu")
#options1.add_argument("--headless")
options1.add_argument("--window-size=1920,1080")
#options1.add_argument("no-sandbox")
options1.add_argument('user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/107.0.5304.88 Safari/537.36')
options1.add_argument('--ignore-certificate-errors')
options1.add_argument('--allow-running-insecure-content')
driver = webdriver.Chrome(options=options1)







Url = ("https://suchen.mobile.de/fahrzeuge/search.html?dam=0&sb=rel&vc=Car")

driver.get(Url)
#buttonc = driver.find_element(By.XPATH, '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button')
#buttonc.click()
sleep(3.0)
def Try():
    try:
        buttonc = driver.find_element(By.XPATH, '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button')
        buttonc.click()
    except:
        return
Try()
#buttonc = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/button')
#buttonc.click()


def AUDISEARCH():


    def audisel():                      #Marke_input=input("Welche Marke? :")
        WebDriverWait(driver,5).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="selectMake1-ds"]'))).click()
        clic_Marke = driver.find_element(By.XPATH, '//*[@id="selectMake1-ds"]/option[12]')
        clic_Marke.click()
    audisel()


    sleep(2.0)
    #Marke_push.click()
    def models3():          #Model_input = input("Welches Modell ? :")
        Model_push = driver.find_element(By.XPATH , '//*[@id="selectModel1-ds"]')
        #Model_push.click()
        Model_push.send_keys("S3")
    models3()
    def kms3():#KM_input = input("Wie viel Kilometer ? :")
        KM_push = driver.find_element(By.XPATH , '//*[@id="maxMileage"]')
        KM_push.send_keys("100000")
    kms3()
    def prices3():#("Wie viel soll er kosten ? :") (5000€) Click
        Price_push = driver.find_element(By.XPATH , '//*[@id="payment-filters"]/div[2]/div/div[2]/div/div[2]/select/option[11]')
        Price_push.click()
        sleep(1.0)
        Price_push.click()
        
    prices3()
    
    sleep(1.0)

    # Funktion für die Plausibilisierung
    def prufung():
        span_element = driver.find_element(By.XPATH, '//*[@id="dsp-upper-search-btn"]')
        global valueget
        valueget = (span_element.text[0])
        sleep(3.0)
        

    prufung()

      
    def returnthevalue():
        if  valueget > "0":
          next_c = driver.find_element(By.XPATH, '//*[@id="dsp-upper-search-btn"]')
          next_c.click()
          sleep(5.0)

              

          get_URL = driver.current_url

          resp = client.send_message("NEW_Car", "Neues Auto", "a", "1", "4", "2",get_URL,
            "Mobile öffnen!", "0", "2", "60", "600", "1", "", "", "")





        else:
            print("Keine Ergebnisse")



    returnthevalue()

AUDISEARCH()
