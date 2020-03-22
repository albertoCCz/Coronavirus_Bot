from selenium import webdriver as wd

driver = wd.Firefox()
driver.get('https://covid19.isciii.es/')

def datos(driver):
    casos = driver.find_element_by_id('casos').text
    fallecidos = driver.find_element_by_id('defunciones').text
    recuperados = driver.find_element_by_id('recuperados').text
    return [casos, fallecidos, recuperados]


