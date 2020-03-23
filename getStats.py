from selenium import webdriver as wd

driver = wd.Firefox()
driver.get('https://covid19.isciii.es/')

def fechaActualizacion(driver):
    """
    Almacena la fecha de última actualización de los datos recogidos
    :return:
    """
    fecha = driver.find_element_by_id('fecha').text
    hora = driver.find_element_by_id('hora').text

    return [fecha, hora]

def datosGlobales(driver):
    """
    Recoge los datos nacionales de casos por Covid-19
    :return: array con los datos
    """
    casos = driver.find_element_by_id('casos').text
    casos24 = driver.find_element_by_id('casos24h').text
    recuperados = driver.find_element_by_id('recuperados').text
    hospitalizados = driver.find_element_by_id('hospitalizados').text
    fallecidos = driver.find_element_by_id('defunciones').text

    return [casos, casos24, recuperados, hospitalizados, fallecidos]

def datosCCAA(driver):
    """
    Recoge los datos por Comunidad Autónoma
    :return: 
    """