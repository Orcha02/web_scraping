import random
from time import sleep
from selenium import webdriver

# Instancio el driver de selenium que va a controlar el navegador
# A partir de este objeto voy a realizar el web scraping e interacciones
driver = webdriver.Chrome('./chromedriver.exe')

# Voy a la pagina que requiero
driver.get('https://www.olx.com.ec/autos_c378')


# Busco el boton para cargar mas informacion
boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
for i in range(3): # Voy a darle click en cargar 3 veces
    try:
        # le doy click
        boton.click()
        # espero que cargue la informacion dinamica
        sleep(random.uniform(8.0, 10.0))
        # busco el boton nuevamente para darle click en la siguiente iteracion
        boton = driver.find_element_by_xpath('//button[@data-aut-id="btnLoadMore"]')
    except:
        # si hay algun error, rompo el lazo. No me complico.
        break

# Encuentro cual es el XPATH de cada elemento donde esta la informacion que quiero extraer
# Esto es una LISTA. Por eso el metodo esta en plural
# (//)-> Para que haga la busqueda dentro del DOM todos los elementos con el tag <li> con atributo data-aut-id="itemBox"
autos = driver.find_elements_by_xpath('//li[@data-aut-id="itemBox"]')


# Recorro cada uno de los anuncios que he encontrado
for auto in autos:
    """
    No busco dentro del driver porque se me va a buscar de nuevo dentro de toda la pagina
    -> En vez de buscar elementos dentro de la variable "driver" los busco dentro de la variable "autos"
    "autos"= No tiene toda la pagina sino cada uno de los anuncios de manera individual
    """
    # Por cada anuncio hallo el precio [(.//)-> Asegurarnos que la busqueda sea dentro del elemento "auto"]
    precio = auto.find_element_by_xpath('.//span[@data-aut-id="itemPrice"]').text
    print (precio)
    # Por cada anuncio hallo la descripcion
    descripcion = auto.find_element_by_xpath('.//span[@data-aut-id="itemTitle"]').text
    print (descripcion)
