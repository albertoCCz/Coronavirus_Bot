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
    Recoge los datos por Comunidad Autónoma en una tabla
    :return: array 20x4 con los datos
    """
    numeroCCAA = 19
    num_col = 4
    table = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    for j in range(0, num_col):
        table[0].append(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[7]/table/thead/tr/th[' +
                                                 str(j + 1) + ']').text)
    for i in range(0,numeroCCAA):
        for j in range(0,num_col):
            table[i+1].append(driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[7]/table/tbody/tr[' +
                                                        str(i+1) + ']/td[' + str(j+1) + ']').text)


    return table

def graficas(driver):
    """
    Recoge la gráfica de datos acumulados
    :return: imagen
    """
    img = driver.find_elements_by_tag_name('img')
    src = []
    for image in img:
        if "CURVAACUMULADA" in str(image.get_attribute('src')):
            src.append(image.get_attribute('src'))
        if "CURVASTATUS" in image.get_attribute('src'):
            src.append(image.get_attribute('src'))
    return src
