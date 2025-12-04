from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

menager = ChromeDriverManager().install()
service = ChromeService(menager)
options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "credentials_enable_service": False,    
    "profile.password_manager_enabled": False, 
    "profile.password_manager_leak_detection": False, 
    "safebrowsing.enabled": True 
})

print(">>> Odpalam bota...")
driver = webdriver.Chrome(service=service, options=options)

url = "https://www.saucedemo.com/"

driver.get(url)
print(f">>> Wszedłem na strone: {url}")

def drive_find(path, by=By.XPATH, timeout=10):
    return WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((by, f'{path}'))
    )
time.sleep(1)
drive_find('//*[@id="user-name"]').send_keys("standard_user")
time.sleep(1)

drive_find('//*[@id="password"]').send_keys("secret_sauce")
time.sleep(1)

drive_find('//*[@id="login-button"]').click()
print(f">>>Pomyślnie wpisałem dane i przeszedłem na strone: {driver.title}")
time.sleep(2)

drive_find('//*[@id="add-to-cart-sauce-labs-backpack"]').click()
print(f">>>Dodałem do koszyka plecak.")
time.sleep(2)

drive_find('//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
print(f">>>Dodano do koszyka koszulke")
time.sleep(2)

print(">>>Przechodzę do koszyka.")
drive_find('//*[@id="shopping_cart_container"]/a').click()
time.sleep(2)

drive_find('//*[@id="checkout"]').click()
print(f">>>Pomyślnie przeszedłem na kolejną stronę, wpisuje informacje o płatności.")
time.sleep(2)

drive_find('//*[@id="first-name"]').send_keys("x")
time.sleep(1)

drive_find('//*[@id="last-name"]').send_keys("y")
time.sleep(1)

drive_find('//*[@id="postal-code"]').send_keys("z")         
print(">>>Pomyslnie uzupełniono dane o płatności.")
time.sleep(2)

drive_find('//*[@id="continue"]').click()
print(f">>> przechodzę na kolejną stronę.")
time.sleep(2)

drive_find('//*[@id="finish"]').click()
print(">>>Zakańczam transakcję.")
time.sleep(1)

print(f">>>Pomyślnie zfinalizowaliśmy transakcję, wiadomość z strony: {drive_find('//*[@id="checkout_complete_container"]/h2').text}")
time.sleep(2)
print("Zamykam bota.")
driver.quit()