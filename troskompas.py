import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
import linecache
import random
import json
from textwrap import wrap
import pygame
import pygame.freetype
from threading import Thread
from selenium.webdriver.support.select import Select
import os

PATH = r"C:\Program Files (x86)\chromedriver.exe"
delay = 19
chrome_options = ChromeOptions()
#chrome_options.add_argument('headless')
chrome_options.add_argument('window-size=800x880')
driver = webdriver.Chrome(PATH, options=chrome_options)


###doen
#https://www.seniorenvoordeelpas.nl/aanmelden/bolcom3995?utm_medium=Email%20&utm_source=oa&utm_campaign=Webwinkels&c_id=TIP2-38076933

def Adres():
    while True:
        addressInfo = linecache.getline("PostalCodes.csv", random.choice(range(1, 471994))).replace("\n", "").split(", ")[:-1]
        if addressInfo[3] == "mixed":
            step = 1
        else:
            step = 2
        try:
            num = random.choice(range(int(addressInfo[1]), int(addressInfo[2]), step))
            break
        except:
            pass
    for index in [1, 2, 3][::-1]:
        addressInfo.pop(index)
    addressInfo.insert(1, num)
    Adres.temppostcode = (addressInfo[0])
    Adres.osso = (addressInfo[1])
    Adres.postcode = wrap(Adres.temppostcode, 4)[0]
    Adres.postcodeletter = wrap(Adres.temppostcode, 4)[1]
    Adres.straat = (addressInfo[2])
    Adres.stad = (addressInfo[3])
    return addressInfo

def ibagen():
    time.sleep(3)
    round = 1
    os.remove("iban.txt")
    driver.get("http://randomiban.com/?country=Netherlands")
    while round < 500:
        driver.find_element_by_xpath("/html/body/div[2]/button").click()
        f = open("iban.txt", "a")
        f.write(driver.find_element_by_xpath("/html/body/p").get_attribute("innerHTML")+"\n")
        f.close()
        round += 1
        ibagen.current = True
    ibagen.current = False

def tempmail():
    driver.get("https://mail.tm")
    tempmail.current = True
    with open("names.json", "r") as file:
        data = json.load(file)
        file.close()
    name = random.choice(data[0])[0]
    sName = random.choice(data[1])
    try:
        time.sleep(0.5)
        webdriver.ActionChains(driver).click(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div/button")))).perform()
    except:
        webdriver.ActionChains(driver).click(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div/button")))).perform()
        webdriver.ActionChains(driver).click(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div")))).perform()
    try:
        time.sleep(0.5)
        webdriver.ActionChains(driver).click(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div[3]/div/div[3]")))).perform()
    except:
        webdriver.ActionChains(driver).click(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div[3]/div/div[3]")))).perform()
        webdriver.ActionChains(driver).click(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[4]/div[3]/div/div[3]/a")))).perform()

    emailname= str(name+sName+str(random.randint(1967, 1999)))
    domain = "metalunits.com"

    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/span/form/div[1]/span/div/input"))).send_keys(emailname)
    WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div[2]/div[2]/span/form/div[2]/span/div/input"))).send_keys("Kanker112!")
    try:
        time.sleep(0.5)
        webdriver.ActionChains(driver).click(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/span[1]/button")))).perform()
    except:
        webdriver.ActionChains(driver).click(WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[3]/div/div[2]/div[2]/span[1]")))).perform()

    time.sleep(1)
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div/div/input")))).perform()

    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[5]/button")))).perform()
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[5]")))).perform()

    tempmail.mail = str(emailname+"@"+domain)
    f = open("mails.txt", "a")
    f.write(emailname+"@"+domain+"\n")
    f.close()
    tempmail.current = False

def bollie():
    driver.get("https://site-id.nettrack.nl/campaign/hmc/cid9833/index.html?")
    bollie.current = True
    iban = linecache.getline("iban.txt", all.currentiban)
    with open("names.json", "r") as file:
        data = json.load(file)
        file.close()
    name = random.choice(data[0])[0]
    gender = random.choice(data[0])[1]
    sName = random.choice(data[1])
    if gender == "M":
        webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/section[2]/div/div/form/div[2]/div[2]/div[1]/div[1]/label[1]")))).perform()
    elif gender == "F":
        webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/section[2]/div/div/form/div[2]/div[2]/div[1]/div[1]/label[2]")))).perform()
    driver.find_element_by_xpath("/html/body/section[2]/div/div/form/div[2]/div[2]/div[1]/div[2]/div/input").send_keys(name)
    driver.find_element_by_xpath("/html/body/section[2]/div/div/form/div[2]/div[2]/div[1]/div[4]/div/input").send_keys(sName)
    driver.find_element_by_xpath("/html/body/section[2]/div/div/form/div[2]/div[2]/div[2]/div[1]/div/input").send_keys(Adres.temppostcode)
    driver.find_element_by_xpath("/html/body/section[2]/div/div/form/div[2]/div[2]/div[2]/div[2]/div/input").send_keys(Adres.osso)
    driver.find_element_by_xpath("/html/body/section[2]/div/div/form/div[2]/div[2]/div[4]/div[1]/div/input[1]").send_keys("06"+str(random.randint(11111111,99999999)))
    driver.find_element_by_xpath("/html/body/section[2]/div/div/form/div[2]/div[2]/div[4]/div[2]/div/input").send_keys(tempmail.mail)
    driver.find_element_by_xpath("/html/body/section[2]/div/div/form/div[2]/div[2]/div[6]/div[1]/input").send_keys(iban)
    time.sleep(0.5)
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/section[2]/div/div/form/div[2]/div[2]/div[5]/div/div[1]/input")))).perform()
    time.sleep(0.5)

    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/section[2]/div/div/form/div[2]/div[2]/div[7]/div")))).perform()
    time.sleep(0.5)
    driver.save_screenshot('screenie.png')
    print("Done! info: " + tempmail.mail + ", " + iban)
    bollie.current = False

def bollie2():
    driver.get("https://www.leesmap.nl/order/?map=2")
    bollie2.current = True
    iban = linecache.getline("iban.txt", all.currentiban)
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[4]/div/div[2]")))).perform()
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[1]/div[2]/div/div[2]/ul/li[3]/div[2]")))).perform()
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[1]/div[2]/div/div[2]/ul/li[3]/div[2]")))).perform()
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[1]/p[3]/input")))).perform()
    with open("names.json", "r") as file:
        data = json.load(file)
        file.close()
    name = random.choice(data[0])[0]
    gender = random.choice(data[0])[1]
    sName = random.choice(data[1])
    time.sleep(1)
    if gender == "F":
        webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[2]/div[1]/div/div/label[2]")))).perform()
    driver.find_element_by_xpath("/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[2]/div[2]/div/div/div[1]/input").send_keys(name)
    driver.find_element_by_xpath("/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[2]/div[2]/div/div/div[3]/input").send_keys(sName)
    driver.find_element_by_xpath("/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[2]/div[3]/div[1]/div/div/div[1]/input").send_keys(Adres.temppostcode)
    driver.find_element_by_xpath("/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[2]/div[3]/div[1]/div/div/div[2]/input").send_keys(Adres.osso)
    driver.find_element_by_xpath("/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[2]/div[4]/div/div/div[1]/input").send_keys("06"+str(random.randint(11111111,99999999)))
    driver.find_element_by_xpath("/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[2]/div[4]/div/div/div[2]/input").send_keys(tempmail.mail)
    driver.find_element_by_xpath("/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[2]/div[5]/div/div/div/input").send_keys(str(random.randint(1,28))+"-"+str(random.randint(1,12))+"-"+str(random.randint(1960,2002)))
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[2]/div[8]/div/div[2]/input")))).perform()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[3]/div[3]/div/select")))
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[3]/div[4]/div/div/div/div[1]/div/input").send_keys(iban)
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[3]/div[5]/div/div[2]/input")))).perform()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[4]/div[1]/div/textarea")))
    time.sleep(2)
    Select(driver.find_element_by_xpath("/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[4]/div[2]/div/select")).select_by_index(random.randint(1,4))
    Select(driver.find_element_by_xpath("/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[4]/div[4]/div/select")).select_by_index(1)
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[4]/div[5]/div/label")))).perform()
    webdriver.ActionChains(driver).click(WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/section[3]/div/div/div[1]/form/fieldset[4]/div[6]/div/div[2]/input")))).perform()
    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/section[2]/div/div/div[1]/h2")))
    driver.save_screenshot('screenie2.png')
    print("Done! info: "+tempmail.mail +", "+ iban)
    bollie2.current = False
    f = open("mails2.txt", "a")
    f.write(tempmail.mail+iban+"\n")
    f.close()

def all():
    all.amount = 0
    all.currentiban = 1
    while True:
        try:
            tijd = int(input("hoe lang wachtin? (in seconden)"))
            break
        except:
            print("opkankeren")
    ibagen()
    try:
        while True:
            Adres()
            tempmail()
            bollie()
            time.sleep(tijd)
            bollie2()
            all.amount +=1
            all.currentiban += 1
            driver.delete_all_cookies()
            time.sleep(tijd)
    except:
        print("trying Agabrug")

def screen():
    pygame.init()
    bg = pygame.image.load("bg.png")
    screen = pygame.display.set_mode((800, 600))
    GAME_FONT = pygame.freetype.Font("font.otf", 24)
    pygame.display.set_caption('Bol GENERATOR VRIEND')
    programIcon = pygame.image.load('billie.jpg')

    pygame.display.set_icon(programIcon)

    all.amount = 0
    ibagen.current = False
    tempmail.current = False
    bollie.current = False
    bollie2.current = False

    running = True


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((255, 255, 255))
        text_surface, rect = GAME_FONT.render("Welcome", (0, 0, 0))
        screen.blit(bg, (0, 0))
        if ibagen.current == True:
            GAME_FONT.render_to(screen, (40, 445), "Generating IBAN", 	(255,255,255))
        elif tempmail.current == True:
            GAME_FONT.render_to(screen, (40, 445), "Generating Mail", 	(255,255,255))
        elif bollie.current == True:
            GAME_FONT.render_to(screen, (40, 445), "Generating 15 euro Gift Card", (255, 255, 255))
        elif bollie2.current == True:
            GAME_FONT.render_to(screen, (40, 445), "Generating 50 euro Gift Card", (255, 255, 255))
        else:
            GAME_FONT.render_to(screen, (40, 445), "...", 	(255,255,255))

        GAME_FONT.render_to(screen, (40, 350),"€"+str(int(sum(1 for line in open('mails.txt')))*15+int(sum(1 for line in open('mails2.txt')))*50), 	(255,255,255))
        GAME_FONT.render_to(screen, (40,165), str(all.amount), 	(255,255,255))
        GAME_FONT.render_to(screen, (40, 260), "€" + str(all.amount * 15),	(255,255,255))

        pygame.display.flip()


if __name__ == '__main__':
    Thread(target = screen).start()
    Thread(target = all).start()


