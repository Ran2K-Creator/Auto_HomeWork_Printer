from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyChatGPT import ChatGPT
session_token = 'YOUR_SESSION_TOKEN'
api = ChatGPT(session_token)

options = Options()
options.add_argument('-headless')

# create webdriver object
driver = webdriver.Firefox()


driver.get("https://3dwriter.io/")

question = input("input your homework question: ")
tall = int(input("how high your notebook is? write in mm: "))
resp = api.send_message(question + " enter to the next line after every 8 words!")
print("preapering the printable file...")

api.reset_conversation()  
api.clear_conversations()  
api.refresh_chat_page() 


font = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div/div[1]/div[2]/div/div[1]').click()
font2 = driver.find_element(By.XPATH, '//*[@id="canvas_timesr"]').click()

text = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div/div[1]/div[2]/div/div[12]/textarea').send_keys(Keys.CONTROL, 'a')
text2 = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div/div[1]/div[2]/div/div[12]/textarea').send_keys(resp['message'])

size = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div/div[1]/div[2]/div/div[2]').click()
size2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/div[1]').click()

spacing = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div/div[1]/div[2]/div/div[6]').click()
spacing2 = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/input[1]').send_keys("0.2")
spacing3 = driver.find_element(By.XPATH, '/html/body/div[1]/div[4]/input[2]').click()

center = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div/div[1]/div[2]/div/div[3]').click()


setting = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div/div[1]/div[1]/div/div[1]/h4/a').click()
setting2 = driver.find_element(By.XPATH, '//*[@id="set_pen_up"]').send_keys(Keys.CONTROL, 'a')
setting3 = driver.find_element(By.XPATH, '//*[@id="set_pen_up"]').send_keys(tall + 2)
setting4 = driver.find_element(By.XPATH, '//*[@id="set_pen_down"]').send_keys(Keys.CONTROL, 'a')
setting5 = driver.find_element(By.XPATH, '//*[@id="set_pen_down"]').send_keys(tall + 0.5)


printfile = driver.find_element(By.XPATH, '/html/body/div[1]/section[1]/div/div/div[2]/div[1]/div[4]/input').click()

print("Good! now check your downloads folder for the file!")

