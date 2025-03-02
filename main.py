from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from time import sleep
from info2 import * 
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(status, mailUser, mailPass):
    try:
        if status:
            NewStatus = "\n".join(status)
            mail = SMTP("smtp.gmail.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login(mailUser, mailPass)
            mesaj = MIMEMultipart()
            mesaj["From"] = mailUser
            mesaj["To"] = "YOUR_MAIL_ADDRESS"
            mesaj["Subject"] = "Pasaport Randevusu"
            body = NewStatus
            body_text = MIMEText(body, "plain")
            mesaj.attach(body_text)
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            mail.close()
    except Exception as e:
        print(f"An error occurred: {e}")

while(True):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")
    #chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options = chrome_options)
    driver.delete_all_cookies()

    wait = WebDriverWait(driver, 5)
    print("Driver Başlatıldı")
    driver.get("https://giris.turkiye.gov.tr/Giris/gir")
    print("Siteye Gidildi")
    driver.implicitly_wait(5)

    for x in ["tridField", "egpField", "submitButton"]:
        print("Bekleniyor: 1")
        wait.until(EC.visibility_of_element_located((By.NAME, x)))
        print("Bekleniyor: 2")
        wait.until(EC.presence_of_element_located((By.NAME, x)))
        print("Bekleniyor: 3")
        wait.until(EC.element_to_be_clickable((By.NAME, x)))
        print("Bekleniyor: 4")
    for x, infos in zip(["tridField", "egpField"], [kimlik, sifre]):
        print("Bekleniyor: 5")
        driver.find_element(By.NAME, x).send_keys(infos)
        print("Bekleniyor: 6")
    driver.find_element(By.NAME, "submitButton").click()

    print("buraya geçti 38")

    try:
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "mfp_close")))
        driver.find_element(By.CLASS_NAME, "mfp_close").click()
    except:
        pass
    #https://www.turkiye.gov.tr/nvi-pasaport-basvuru-randevusu
    #https://www.turkiye.gov.tr/nvi-pasaport-basvuru-randevusu?yeni=randevu
    print("Siteye Gidildi basvuru-randevusu")

    driver.get("https://www.turkiye.gov.tr/nvi-pasaport-basvuru-randevusu")
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "new")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "new")))
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "new")))
    newButton = driver.find_element(By.CLASS_NAME, "new")
    driver.execute_script("arguments[0].click();", newButton)
    #driver.find_element(By.CLASS_NAME, "new").click()


    wait.until(EC.element_to_be_clickable((By.ID, "onay")))
    onay = driver.find_element(By.ID, "onay")
    driver.execute_script("arguments[0].click();", onay)
    #submitButton

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submitButton")))
    closeButton = driver.find_element(By.CLASS_NAME, "submitButton")

    driver.execute_script("arguments[0].click();", closeButton)


    wait.until(EC.element_to_be_clickable((By.ID, "pasaportTur")))
    radioButton = driver.find_element(By.ID, "pasaportTur")
    driver.execute_script("arguments[0].click();", radioButton)

    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "submitButton")))
    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "submitButton")))
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "submitButton")))
    closeButton = driver.find_element(By.CLASS_NAME, "submitButton")
    print("Siteye Gidildi submitButton geçildi > il ilce secim yerine")
    status = list()
    driver.execute_script("arguments[0].click();", closeButton)
    print("Siteye Gidildi submitButton geçildi > il ilce secim yerine 2")
    try:
        wait.until(EC.visibility_of_element_located((By.ID, 'il')))
        print("İl Seçimi Bekleniyor")
        wait.until(EC.element_to_be_clickable((By.ID, "il")))
        print("İl Seçimi Bekleniyor 2")
        wait.until(EC.presence_of_element_located((By.ID, "il")))
        print("İl Seçimi Bekleniyor 3")
        driver.find_element(By.ID, "il").click()
        print("İl Seçimi tıklandı")
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[value='34']")))
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[value='34']")))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[value='34']")))
        driver.find_element(By.CSS_SELECTOR, "[value='31']").click()
        print("Hatay Seçildi")

        # there will be  a modal that id "modalContent"
        # we will check if there is modal or not
        # if there is modal we will close it
        # if there is not modal we will pass 
        # wait.until(EC.visibility_of_element_located((By.ID, 'ilce')))
        # wait.until(EC.element_to_be_clickable((By.ID, "ilce")))
        # wait.until(EC.presence_of_element_located((By.ID, "ilce")))
        # select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ilce')))
        driver.implicitly_wait(10)
        wait.until(EC.visibility_of_element_located((By.ID, 'ilce')))
        wait.until(EC.element_to_be_clickable((By.ID, "ilce")))
        wait.until(EC.presence_of_element_located((By.ID, "ilce")))
        select_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'ilce')))
        print("İlçe Seçimi Bekleniyor")
        # Use Select class for dropdown
        ilce_dropdown = Select(select_element)
        


        # Check if ilce dropdown has options
        if ilce_dropdown.options:
            # Loop through options and append to status
            for option in ilce_dropdown.options:
                if(option.text != "Seçiniz" and option.text != "Yükleniyor..."):
                    status.append(option.text)
                    if "Karaağaç" in option.text:
                        print(option.text)
                        print("Seçenekler bulundu")
                        send_email(status, mailUser, mailPass)
                        driver.implicitly_wait(200)
                else:
                    print("Karaağaç bulunamadı")
                    pass
        else:
            print("No options found in ilce dropdown")
            #send_email("No options found in ilce dropdown", mailUser, mailPass)
        # driver.implicitly_wait(50)
        print(status)
        # if there is ilce option  send e mail to me continue to code
        #send_email(status, mailUser, mailPass)
        # driver.find_element(By.ID, "ilce").click()
        # i = 2
        # for x in range(30):
        #     bilgi = '//*[@id="ilce"]/option[' + str(i) + ']'
        #     status.append(driver.find_element(By.XPATH, bilgi).text)
        #     i += 1    

    except:
        print("İl Seçimi Hatası")
        wait.until(EC.visibility_of_element_located((By.ID, 'modalContent')))
        wait.until(EC.element_to_be_clickable((By.ID, "modalContent")))
        wait.until(EC.presence_of_element_located((By.ID, "modalContent")))
        modal_element = wait.until(EC.presence_of_element_located((By.ID, 'modalContent')))
        print("StaleElementReferenceException occurred. Re-locating element...")
       
        closeButton = driver.find_element(By.ID, "modalContent")
        driver.execute_script("arguments[0].click();", closeButton)
        print("Modal Kapatıldı")
        #send_email(status, mailUser, mailPass)
        pass
    #send_email(status, mailUser, mailPass)

    driver.close()
    sleep(250)



