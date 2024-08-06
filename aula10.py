#importando webdriver e By da biblioteca selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
#importando biblioteca time para adicionar uma pausa no nosso codigo
from time import sleep 

#abrindo o navegador para comecar a automacao, utilizando o webdriver
driver = webdriver.Chrome()
#abrindo uma URL
driver.get('https://www.saucedemo.com/')
#adicionando uma pausa no codigo
sleep (2)


try:
    #buscando um elemento usuario utilizando o XPATH
    login = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[1]/input')
    #inserindo o valor no campo de username
    login.send_keys('standard_user')
    sleep (2)

    #buscando um elemento senha utilizando o XPATH
    senha = driver.find_element(By.XPATH, '/html/body/div/div/div[2]/div[1]/div/div/form/div[2]/input')
    #inserindo o valor no campo de senha
    senha.send_keys('secret_sauce')
    sleep (2)
    #Clicando no 'enter'
    senha.send_keys(Keys.ENTER)
except NoSuchElementException:
    print ('Nada foi encontrado!')
except Exception as e:
    print ('Tente novamente mais tarde!')

try:
    compra1 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-backpack"]')
    sleep (1)
    compra1.click()
    compra2 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-bike-light"]')
    sleep (1)
    compra2.click()
    compra3 = driver.find_element(By.XPATH, '//button[@id="add-to-cart-sauce-labs-onesie"]')
    sleep (1)
    compra3.click()
except NoSuchElementException:
    print ('Nada foi encontrado!')
except Exception as e:
    print ('Tente novamente mais tarde!', e)

try:
    carrinho = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    sleep (1)
    carrinho.click()

    remover = driver.find_element(By.XPATH, '//button[@id="remove-sauce-labs-bike-light"]')
    sleep (2)
    remover.click()
    sleep (2)

    checkout = driver.find_element(By.XPATH, '//button[@id="checkout"]')
    sleep (2)
    checkout.click()
    sleep (2)

    name = driver.find_element(By.XPATH, '//input[@id="first-name"]')
    sleep (2)
    name.click()
    name.send_keys('Lia Maria')
    sleep (2)
    lastname = driver.find_element(By.XPATH, '//input[@id="last-name"]')
    sleep (2)
    lastname.click()
    lastname.send_keys('Santos')
    sleep (2)
    postcode = driver.find_element(By.XPATH, '//input[@id="postal-code"]')
    sleep (2)
    postcode.click()
    postcode.send_keys('13471-200')
    sleep (2)
    continua = driver.find_element(By.XPATH, '//input[@id="continue"]')
    sleep (2)
    continua.click()
    final = driver.find_element(By.XPATH, '//button[@id="finish"]')
    sleep (2)
    final.click()    
except NoSuchElementException:
    print ('Nada foi encontrado!')
except Exception as e:
    print ('Tente novamente mais tarde!', e)

sleep (10)
input()
