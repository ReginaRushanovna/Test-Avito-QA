from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

browser = webdriver.Chrome()
browser.get('https://www.avito.ru/avito-care/eco-impact')


def test_first_case():
    water = browser.find_element(By.XPATH, "//div[@class='desktop-impact-item-eeQO3' and contains(., 'было сохранено')]")
    water.screenshot("C:\\py.projects\\autotestsAvito\\output\\1_water.png")  # сохранения счётчика воды в папку output

    carbon_dioxide = browser.find_element(By.XPATH,
                                          "//div[@class='desktop-impact-item-eeQO3' and contains(., 'не попало в атмосферу')]")
    carbon_dioxide.screenshot("C:\\py.projects\\autotestsAvito\\output\\1_co2.png")  # сохранения счётчика c02 в папку output

    electricity = browser.find_element(By.XPATH,
                                       "//div[@class='desktop-impact-item-eeQO3' and contains(., 'было сэкономлено')]")
    electricity.screenshot("C:\\py.projects\\autotestsAvito\\output\\1_electricity.png")  # сохранения счётчика электричества в папку output

    sleep(5)