from selenium import webdriver
from selenium.webdriver.common.by import By
import random
from opciones import *

def  automatedSurvey(survey):
    driver = webdriver.Chrome()
    driver.get(survey)

    # edad
    pointer = driver.find_element(By.XPATH, opciones_1[random.randint(0,len(opciones_1)-1)])
    pointer.click()
    pointer = ''

    # genero
    pointer = driver.find_element(By.XPATH, opciones_2[random.randint(0,len(opciones_2)-1)])
    pointer.click()
    pointer = ''

    #distrito
    pointer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    pointer.send_keys(opciones_3[random.randint(0,len(opciones_3)-1)])
    pointer = ''

    # preferencias
    pointer = driver.find_element(By.XPATH, opciones_4[random.randint(0,len(opciones_4)-1)])
    pointer.click()
    pointer = ''

    # cartas
    pointer = driver.find_element(By.XPATH, opciones_5[random.randint(0,len(opciones_5)-1)])
    pointer.click()
    pointer = ''

    # estado de animo
    pointer = driver.find_element(By.XPATH, opciones_6[random.randint(0,len(opciones_6)-1)])
    pointer.click()
    pointer = ''

    # atencion
    pointer = driver.find_element(By.XPATH, opciones_7[random.randint(0,len(opciones_7)-1)])
    pointer.click()
    pointer = ''

    # has probado
    pointer = driver.find_element(By.XPATH, opciones_8[random.randint(0,len(opciones_8)-1)])
    pointer.click()
    pointer = ''

    # ofrece información
    pointer= driver.find_element(By.XPATH, opciones_9[random.randint(0,len(opciones_9)-1)])
    pointer.click()
    pointer = ''

    # sitios externos
    pointer = driver.find_element(By.XPATH, opciones_10[random.randint(0,len(opciones_10)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_11[random.randint(0,len(opciones_11)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_12[random.randint(0,len(opciones_12)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_13[random.randint(0,len(opciones_13)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_14[random.randint(0,len(opciones_14)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_15[random.randint(0,len(opciones_15)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_16[random.randint(0,len(opciones_16)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_17[random.randint(0,len(opciones_17)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_18[random.randint(0,len(opciones_18)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_19[random.randint(0,len(opciones_19)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_20[random.randint(0,len(opciones_20)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_21[random.randint(0,len(opciones_21)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_22[random.randint(0,len(opciones_22)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_23[random.randint(0,len(opciones_23)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_24[random.randint(0,len(opciones_24)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_25[random.randint(0,len(opciones_25)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_26[random.randint(0,len(opciones_26)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_27[random.randint(0,len(opciones_27)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_28[random.randint(0,len(opciones_28)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_29[random.randint(0,len(opciones_29)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_30[random.randint(0,len(opciones_30)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_31[random.randint(0,len(opciones_31)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_32[random.randint(0,len(opciones_32)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_33[random.randint(0,len(opciones_33)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_34[random.randint(0,len(opciones_34)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_35[random.randint(0,len(opciones_35)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_36[random.randint(0,len(opciones_36)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_37[random.randint(0,len(opciones_37)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_38[random.randint(0,len(opciones_38)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_39[random.randint(0,len(opciones_39)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, opciones_40[random.randint(0,len(opciones_40)-1)])
    pointer.click()
    pointer = ''

    pointer = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    pointer.click()
    pointer = ''

    driver.quit()

#haremos el main
survey = ''
numberOfTimes = 10
for i in range(0, int(numberOfTimes)):
    automatedSurvey(survey)