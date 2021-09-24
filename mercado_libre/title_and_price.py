from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


driver = webdriver.Chrome('./chromedriver.exe') 
driver.get('https://listado.mercadolibre.com.ec/repuestos-autos-camionetas-bujias')

# Para obtener info de desde pafina actual hasta la 10
PAGINACION_MAX = 10
PAGINACION_ACTUAL = 1

# click al boton de coockies para que no interrumpa nuestras acciones
try: # Encerramos todo en un try catch para que si no aparece el discilamer, no se caiga el codigo
  coockies = driver.find_element_by_xpath('//button[@id="cookieDisclaimerButton"]')
  coockies.click() # lo obtenemos y le damos click
except Exception as e:
  print (e) 
  None

# Ejecuto hasta que llegue a la pagina maxima que es la 10
while PAGINACION_MAX > PAGINACION_ACTUAL:

  links_productos = driver.find_elements_by_xpath('//a[@class="ui-search-item__group__element ui-search-link"]')
  links_de_la_pagina = []
  for a_link in links_productos:
    links_de_la_pagina.append(a_link.get_attribute("href"))
  # Q: Porque no hiciste for link in link_productos, y simplemente ibas y volvias haciendo click en el contenedor que me lleva a la otra pagina?
  # A: Porque al yo irme y volver, pierdo la referencia de links_productos que tuve inicialmente. Y selenium me daria error porque le intentaria dar click a algo que no existe en el DOM actual.
  # Es por esto que, la mejor estrategia es obtener todos los links como cadenas de texto y luego iterarlos.

  for link in links_de_la_pagina:

    try:
      # Voy a cada uno de los links de los detalles de los productos
      driver.get(link)
      titulo = driver.find_element_by_xpath('//h1').text
      precio = driver.find_element_by_xpath('//span[contains(@class,"price-tag ui-pdp-price__part")]').text
      print (titulo)
      print (precio.replace('\n', '').replace('\t', ''))

      # Click en boton para devolverme a pagina principal
      driver.back()
    except Exception as e:
      print (e)
      # Si sucede algun error dentro del detalle, no me complico. Regreso a la lista y sigo con otro producto.
      driver.back()

  # Logica de deteccion de fin de paginacion
  try:
    # Intento obtener el boton de SIGUIENTE y le intento dar click
    puedo_seguir_horizontal = driver.find_element_by_xpath('//span[text()="Siguiente"]')
    puedo_seguir_horizontal.click()
  except: 
    # Si hay error al darle click al boton, quiere decir que no existe
    # No puedo seguir bajando e la misma pagina
    break

PAGINACION_ACTUAL += 1
