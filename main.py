from selenium import webdriver
from pushsafer import Client
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

###
# Chrome options#
client = Client("bjHKdba7y0Hj8LRlRs3i")
# push#
##
chromedriver_autoinstaller.install()
# Chrome options

options1 = webdriver.ChromeOptions()  # try

options1.add_argument("--disable-extensions")
options1.add_experimental_option("useAutomationExtension", False)
options1.add_argument("--proxy-bypass-list=*")
options1.add_argument("--disable-gpu")
# options1.add_argument("--headless")
options1.add_argument("--window-size=1920,1080")
options1.add_argument("no-sandbox")
options1.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                      '(KHTML, like Gecko) Chrome/107.0.5304.88 Safari/537.36')
options1.add_argument('--disable-blink-features=AutomationControlled')
options1.add_argument('--ignore-certificate-errors')
options1.add_argument('--allow-running-insecure-content')
driver = webdriver.Chrome(options=options1)
driver2 =webdriver.Chrome(options=options1)

Url = ("https://suchen.mobile.de/fahrzeuge/search.html?dam=0&sb=rel&vc=Car")

driver.get(Url)
# buttonc = driver.find_element(By.XPATH, '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button')
# buttonc.click()
sleep(2.5)


def Try():
    try:
        buttonc = driver.find_element(By.XPATH, '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button')
        buttonc.click()
    except:
        pass


Try()


# buttonc = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[1]/button')
# buttonc.click()


def AUDISEARCH():
    def audisel():  # Marke_input=input("Welche Marke? :")
        title = driver.title
        print(title)
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="selectMake1-ds"]'))).click()
        clic_Marke = driver.find_element(By.XPATH, '//*[@id="selectMake1-ds"]/option[12]')
        clic_Marke.click()

    audisel()

    sleep(3.0)

    # Marke_push.click()
    def models3():  # Model_input = input("Welches Modell ? :")
        Model_push = driver.find_element(By.XPATH, '//*[@id="selectModel1-ds"]')
        # Model_push.click()
        Model_push.send_keys("S3")

    models3()

    def kms3():  # KM_input = input("Wie viel Kilometer ? :")
        KM_push = driver.find_element(By.XPATH, '//*[@id="maxMileage"]')
        KM_push.send_keys("100000")

    kms3()
    sleep(1.0)

    def prices3():  # ("Wie viel soll er kosten ? :") (5000???) Click
        #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="payment-filters"]/div[2]/div/div[2]/div/div[1]/input'))).click()
        #sel = Select(driver.find_element(By.XPATH, '//*[@id="payment-filters"]/div[2]/div/div[2]/div/div[2]/select'))
        #sel.select_by_visible_text("5.000 ???")
        
      
        
        needthisaswell = driver.find_element(By.XPATH, '//*[@id="payment-filters"]/div[2]/div/div[2]/div/div[2]/select/option[11]')
        needthisaswell.click()
        
        sleep(1.0)
        #clickit = driver.find_element(By.XPATH, '//*[@id="form-dsp"]/div[2]/div/div[1]/div[2]/div[1]/div[2]/div/a')
        #clickit.click()
    
        

    prices3()

    sleep(1.0)
    sleep(1.0)

      
        #span_element = driver.find_element(By.XPATH, '//*[@id="dsp-upper-search-btn"]')
        #global valueget
        #valueget = (span_element.text[0])
        #sleep(6.0)
      
        #print(valueget)

    
    #driver.refresh()
    sleep(5.0)
    sleep(1.0)

      
      
      

    def returnthevalue(): 
      
        driver.find_element(By.XPATH, '//*[@id="dsp-upper-search-btn"]').click()
        sleep(2.5)
        sleep(1.0)
        URL2 = driver.current_url
        #driver2.get(URL2)
        driver.get(URL2)
        sleep(3.0)
        sleep(1.0)
        
        title = driver.title
        #title2 = driver2.title
        
        print(title)
        print(URL2)
        
        
        

        sleep(2.0)
        sleep(1.0)
        eleget2 = driver.find_element(By.XPATH, '//*[@id="minisearch-search-btn"]').text[0]
    
        print(eleget2)
        if eleget2 != "0":
          sleep(1.5)
          get_URL = driver.current_url
          sleep(1.5)
          sleep(1.0)
          client.send_message("AUDI!", "Neuer Audi", "a", "1", "4", "2", get_URL,
                                "Mobile ??ffnen!", "0", "2", "60", "600", "1", "", "", "")
          driver.close()
          driver2.close()
        
        else:
          print("keine Ergebnisse!")
          driver.close()
          driver2.close()

          

        
        
        
   
        
        
             

    returnthevalue()


AUDISEARCH()

driver = webdriver.Chrome(options=options1)
driver2 =webdriver.Chrome(options=options1)

driver.get(Url)
def SEATSEARCH():
    def seatsel():  # Marke_input=input("Welche Marke? :")
        #WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="selectMake1-ds"]'))).click()
        clic_Marke2 = driver.find_element(By.XPATH, '//*[@id="selectMake1-ds"]/option[104]')
        clic_Marke2.click()

    seatsel()

    sleep(2.0)
    sleep(1.0)
    sleep(1.0)

    # Marke_push.click()
    def mleon():  # Model_input = input("Welches Modell ? :")
        Model_push1 = driver.find_element(By.XPATH, '//*[@id="selectModel1-ds"]')
        # Model_push.click()
        Model_push1.send_keys("Leon")
        sleep(1.0)
        sleep(1.0)
        sleep(1.0)

    mleon()

    def kms2():  # KM_input = input("Wie viel Kilometer ? :")
        KM_push1 = driver.find_element(By.XPATH, '//*[@id="maxMileage"]')
        KM_push1.send_keys("100000")
        sleep(1.0)
        sleep(1.0)
        sleep(1.0)

    kms2()

    def prices4():  # ("Wie viel soll er kosten ? :") (5000???) Click
        needthisaswell3 = driver.find_element(By.XPATH,
                                             '//*[@id="payment-filters"]/div[2]/div/div[2]/div/div[2]/select/option[8]')
        needthisaswell3.click()
        sleep(1.0)
        sleep(1.0)
    prices4()
    
    def psvon():  # ("Wie viel von 150PS
        needthisaswell2 = driver.find_element(By.XPATH,
                                             '//*[@id="minPowerAsArray-s"]/option[10]')
        needthisaswell2.click()
        sleep(1.0)
        sleep(1.0)
    psvon()
    
    def psbis():  # ("Wie viel PS 250PS
        needthisaswell1 = driver.find_element(By.XPATH,
                                             '//*[@id="maxPowerAsArray-s"]/option[12]')
        needthisaswell1.click()
        sleep(1.5)
        sleep(1.0)
        sleep(1.0)
        sleep(1.0)

        sleep(1.0)
    psbis()
    
    def returnthevalue1():
        sleep(1.0)
        try:
          buttonc = driver.find_element(By.XPATH, '//*[@id="mde-consent-modal-container"]/div[2]/div[2]/div[1]/button')
          buttonc.click()
        except:
          
          pass
        driver.find_element(By.XPATH, '//*[@id="dsp-upper-search-btn"]').click()
        sleep(2.5)
        URL2 = driver.current_url
        #driver2.get(URL2)
        driver.get(URL2)
        sleep(3.0)
        sleep(1.0)
        title = driver.title
        #title2 = driver2.title
        
        print(title)
        print(URL2)
        
        
        

        sleep(2.0)
        eleget2 = driver.find_element(By.XPATH, '//*[@id="minisearch-search-btn"]').text[0]
    
        print(eleget2)
        if eleget2 != "0":
          sleep(1.5)
          get_URL = driver.current_url
          sleep(1.5)
          client.send_message("SEAT!", "Neuer SEAT!", "a", "1", "4", "2", get_URL,
                                "Mobile ??ffnen!", "0", "2", "60", "600", "1", "", "", "")
          driver.close()
          driver2.close()
        
        else:
          print("keine Ergebnisse!")
          driver.close()
          driver2.close()

          

        
        
        
   
        
        
             

   
        
        
             

    returnthevalue1()

    
SEATSEARCH()
