from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.binary_location = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"

driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.saucedemo.com")
    usuario = driver.find_element(By.ID, "user-name")
    usuario.send_keys("standard_user")
    contrasena = driver.find_element(By.ID, "password")
    contrasena.send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    #actividad 1
    assert "/inventory.html" in driver.current_url
    print("Test OK")

    #actividad 2
    titulo = driver.find_element(By.CSS_SELECTOR, "div.header_secondary_container .title").text
    assert titulo == "Products"
    print("Título de sección OK:", titulo)

    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0
    print("Cantidad de productos:", len(productos))

    nombre = productos[0].find_element(By.CLASS_NAME, "inventory_item_name").text
    print("Primer producto:", nombre)
    precio = productos[0].find_element(By.CLASS_NAME, "inventory_item_price").text
    print("Precio del primer producto:", precio)

    #actividad 3
    productos[0].find_element(By.TAG_NAME, "button").click()
    print("Clic en Add to cart realizado")
    contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert contador == "1"
    print("Carrito OK:", contador)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    producto_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert producto_carrito == nombre
    print("Producto verificado en el carrito:", producto_carrito)


    time.sleep(1)
    print("Campo Username encontrado")

finally:
    driver.quit()