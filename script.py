from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

user = "ElizabethAlarconITSQMET7"
key = "123456"

#ABRE PAGINA WEB
driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/index.html")
sleep(1)

# 1. Registro
sign_up = driver.find_element(By.XPATH, "//*[@id='signin2']")
sign_up.click()
sleep(1)
user_name = driver.find_element(By.XPATH, "//*[@id='sign-username']")
user_name.send_keys(user)
password = driver.find_element(By.XPATH, "//*[@id='sign-password']")
password.send_keys(key)
register = driver.find_element(By.XPATH, "//*[@id='signInModal']/div/div/div[3]/button[2]")
register.click()
sleep(1)
alert = driver.switch_to.alert
alert.accept()
sleep(1)

# 2. Loguearse
login = driver.find_element(By.XPATH, "//*[@id='login2']")
login.click()
sleep(2)
user_name_login = driver.find_element(By.XPATH, "//*[@id='loginusername']")
user_name_login.send_keys(user)
password_login = driver.find_element(By.XPATH, "//*[@id='loginpassword']")
password_login.send_keys(key)
button_login = driver.find_element(By.XPATH, "//*[@id='logInModal']/div/div/div[3]/button[2]")
button_login.click()
sleep(2)

# 3. Seleccionar productos
selec_product = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/div/h4/a")
selec_product.click()
sleep(2)
add_to_card = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")
add_to_card.click()
sleep(1)
alert.accept()
sleep(1)
home = driver.find_element(By.XPATH, "//*[@id='navbarExample']/ul/li[1]")
home.click()
sleep(1)
selec_product = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[1]/div/div/h4/a")
selec_product.click()
sleep(2)
add_to_card2 = driver.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/a")
add_to_card2.click()
sleep(1)
alert.accept()
sleep(1)

# 4. Realizar el pedido
cart = driver.find_element(By.XPATH, "//*[@id='cartur']")
cart.click()
sleep(3)
place_order = driver.find_element(By.XPATH, "//*[@id='page-wrapper']/div/div[2]/button")
place_order.click()
sleep(1)
name = driver.find_element(By.XPATH, "//*[@id='name']")
name.send_keys("Elizabeth Alarcón")
country = driver.find_element(By.XPATH, "//*[@id='country']")
country.send_keys("Ecuador")
city = driver.find_element(By.XPATH, "//*[@id='city']")
city.send_keys("Quito")
card = driver.find_element(By.XPATH, "//*[@id='card']")
card.send_keys("4401-1734-6095-2288")
month = driver.find_element(By.XPATH, "//*[@id='month']")
month.send_keys("8")
year = driver.find_element(By.XPATH, "//*[@id='year']")
year.send_keys("2024")
purchase = driver.find_element(By.XPATH, "//*[@id='orderModal']/div/div/div[3]/button[2]")
purchase.click()
sleep(1)
ok = driver.find_element(By.XPATH, "/html/body/div[10]/div[7]/div/button")
ok.click()
sleep(1)

# 5 Desloguearse
logout = driver.find_element(By.XPATH, "//*[@id='logout2']")
logout.click()
sleep(1)

driver.close()

