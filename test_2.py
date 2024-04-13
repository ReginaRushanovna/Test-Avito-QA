from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Chrome()
browser.get('https://www.avito.ru/avito-care/eco-impact')
#sleep(15)


def test_second_case():
    log_in = browser.find_element(By.CLASS_NAME, 'desktop-button-wrapper-K8ki0') # нопка авторизоваться
    log_in.click()  # нажали на кнопку авторизоваться
    sleep(5)

    browser.switch_to.window(browser.window_handles[1])  # переход на вкладку с формой авторизации

    sleep(20)
    login_input = browser.find_element(By.XPATH,
                                       "/html/body/div[3]/div/div/div/div/div/div/div/div[1]/form/div/div[1]/label/div/div/input")
    sleep(2)
    login_input.send_keys('test5_for_content@avito.ru')  # ввод тестового логина в поле "Телефон или почта"
    sleep(2)

    password_input = browser.find_element(By.XPATH,
                                          "/html/body/div[3]/div/div/div/div/div/div/div/div[1]/form/div/label/div/div/input")
    sleep(2)
    password_input.send_keys('i~yrg2G$0z') # ввод тестового пароля в поле "Пароль"
    sleep(2)

    browser.find_element(By.CLASS_NAME, 'css-kj8sh1').click()  # нажатие на кнопку "Войти"

    sleep(30)
    water = browser.find_element(By.XPATH,
                                 "//div[@class='desktop-impact-item-eeQO3' and contains(., 'было сохранено')]")
    water.screenshot("C:\\py.projects\\autotestsAvito\\output\\2_water.png")  # сохранения счётчика воды в папку output

    carbon_dioxide = browser.find_element(By.XPATH,
                                          "//div[@class='desktop-impact-item-eeQO3' and contains(., 'не попало в атмосферу')]")
    carbon_dioxide.screenshot("C:\\py.projects\\autotestsAvito\\output\\2_co2.png")  # сохранения счётчика c02 в папку output

    electricity = browser.find_element(By.XPATH,
                                       "//div[@class='desktop-impact-item-eeQO3' and contains(., 'было сэкономлено')]")
    electricity.screenshot("C:\\py.projects\\autotestsAvito\\output\\2_electricity.png")  # сохранения счётчика электричества в папку output

    sleep(20)