from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

from Graph import comb_city, cities
'''Сайты для реализации поиска'''
# driver = webdriver.Chrome()
# driver.implicitly_wait(10)
#
# url_dist = 'https://www.avtodispetcher.ru/'
# url_coord = 'https://u-karty.ru/opredelenie-koordinat-na-karte-google'

'''Дистанция между городами'''
# driver.get(url_dist)
# distance_between_cities = []
# for coupe_cities_1, coupe_cities_2 in comb_city:
#     from_city = driver.find_element(By.NAME, 'from')
#     from_city.send_keys(coupe_cities_1 + Keys.RETURN)
#     to_city = driver.find_element(By.NAME, 'to')
#     to_city.send_keys(coupe_cities_2 + Keys.RETURN)
#     distance = driver.find_element(By.ID, 'totalDistance')
#     distance_between_cities.append(distance.text)
#     distance_between_cities = list(map(int, distance_between_cities))
#     main_page = driver.find_element(By.CLASS_NAME, 'logo_container')
#     main_page.click()

'''Координаты городов'''
# driver.get(url_coord)
# coord_cities = driver.find_element(By.XPATH, '//*[@id="address"]')
# coord = []
# for city in cities:
#     coord_cities.send_keys(city)
#     button_coord = driver.find_element(By.XPATH, '//*[@id="map"]/input[2]')
#     button_coord.click()
#     coord.append(driver.find_element(By.ID, 'latitude').text)
#     coord.append(driver.find_element(By.ID, 'longitude').text)
#     coord_cities = driver.find_element(By.CLASS_NAME, 'page_item page-item-1863 current_page_item')
#
# print(coord)

# coord = ["Наро-Фоминск, 55.39, 36.73, Сергиев Посад, 56.3, 38.13, Воскресенск, 55.32, 38.65, Лобня, 56.01, 37.48, "
#          "Клин, 56.33, 36.73, Дубна, 56.73, 37.17, Чехов, 55.15, 37.48, Дмитров, 56.34, 37.52, Ступино, 54.9, 38.07, "
#          "Павловский Посад, 55.78, 38.65,Фрязино, 55.96, 38.05, Дзержинский, 55.63, 37.85, Балашиха, 55.81, 37.96, "
#          "Солнечногорск, 56.18, 36.98, Кашира, 54.50, 38.11, Протвино, 54.52, 37.12, Шатура,55.34, 39.32, "
#          "Ликино-Дулёво, 55.42, 38.57, Красноармейск, 56.06, 38.08, Химки, 55.9, 37.43"]
#
#
#
# driver.quit()
