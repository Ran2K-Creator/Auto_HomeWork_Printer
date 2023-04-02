from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pyChatGPT import ChatGPT
session_token = 'eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..YE0CsRpgkLjNsWzc.ah_cmUJCiJF7WHBeRYMGTducZALZ7NC5rzwKTi7fAK7kLeSu-OtcyonhyA5_d5_pVrwE1s6Kz9jsn37DcPo-njZ4vtTYYKQTSocQhHUcMrxPOfXZL_LVX4_zx_PCNKW2ypwKRe-WJpQOrYGSJS5EyOQPULoUzVo8mMNPjqJQbfPJxFmLJXTYnUpt9r5z30k2-RCDQC23e6-6qyR9CemYh3tdo0FNx-0vuQei1PtX_PfhcGUlqkBbICSb_DrzOzkNJQhwj97JrKlYFAxFcT-cbgSBkYSrMUAPrjLTUxqugSNfM3RMJJw8Lyhz6Z9lUa9JnX7lCFopuruNVK-gQGSMLC0_WiQz9f2dZmwXs-X-kQx8T3FWX-3jyL9TX5-Glzxy7iVGaQhAQKuxSehWnyuihKi4INZhwYDMRHKl5qixdYvO77NOflxHNfIqanzFNAD31hNKbeITVHkFXmlEh9FtG_yg3eTcYA46g-C6c_W9Mlz_Q1mchB0MIwMeiHNiuulzzaYd_3gA4WRFULVc-JOB3xG4aGmZKcCSpKQ5JvZdFCAqUM5POJTrU9wpvlO90H13sLgWVo9hdZ_22WNOcc5W_KXhE0PAXBOBfPIUrBJe9S9YNahK7xLtqcm9s9uAWWHtu5R6Tyhk5KNQr6YqGo0sZI5T0jcpukyXrUbgcQHSgVBd-c2eYw_CTb3sIi8QvonN1Wzd468MdasQbj9gIT5XF_mv4yMe0rtXkpO9_xVCyO5nMDFFPaE-v09AAoumml1sJcp2p3NbTNAcKcVLwPq24pTJnZeXNiCFkqy3kC8lUXLbSDkCs_Y4huX7c_wu7jlN2k5Fmh_PlWTt0_eY-K6fUenR-azFNZxsL0k00NgKeovHwdbVfExNRevWVt2iQwqw33Vfygxnf0RjVBoFlUGyHMT9UYA7NgiIxay7F6i6lVZPgFLvA8L0Z7MnPYDrNgfnnVOBjNgG1NenFowmtSwjTPpqqH3ip2Q27vt7Fd79TA9QleW0fi_ezxz7KeiyYeKRsAwXyVN0nfthRewUNWfTA2m0WTfuvrsAI141RJGDFXQB5fHt4Nmf_09syUmCrouiX3DyphHU3_DLgCHgFgn12HiIb2Rst_nkwdBpNuZsTmej5QjobZMa6-e7D2besZuoW45adsuOlWf3cHL3MNqpgWHt3l8VV92LnnGQv6tQDHl4CTMc8mAy76s6TxzL4UxC5f_c4__VoEW7_NE5MiKMcwl8xCvV2FmBFn81b1FopgdwJn7kM-W1_UArs0pKjj8mqn2ZPSv9ZT_CY9_0OzBhRL9LNOVdewel8500oX5PIsTXk4CddXl_6it_hWq4U5JOwTLqGktxo9cuelO1OLlJ0BWI09AJ8vj5Uh0VKSjuW_PS6LxJPHUnxtW0C0Hp2BSfzV8K1abDCq3NpYrA8XyJj8kUA826Be4NpRGCXVD0SmsJZhT8QQ8n4qEqVSVU1Z2DYc9BevEGu_zZQ_ToPAI6Inbhgzj6JKzgXg0vkocShar20EfzTzCRnNDL7ibm37BbbBfOWw4ZlFAn9UKBEYYg7o_mxhR9gJpdzWdsm6U2_xl1iF6wV8Ov0wdqK4B6xNUdvARBay4iXzw2W7gU5l7Ku2vKSiGOv-WAj6BvXzc-QtNnw55OTT7ISHoEr_wG2lT6BCZxQxoA0ZKbQ1pI15rR7I8K5NrP93f7eUfvrbgbcsKCa_2SMhnqOsaX84OqIaMa2ZBS3HrlISy1INh0wb93Evu170TPtdEw0oj9SRr6igFj84WruQlv8Dtb5gzKqChsKd1XgVgnKJ4uD8g8227ctSd1NDOucMH3fQxEsx-H0KE_IGJn-wSBjBgrA-xiAU1mIjqEDJEQom7BpZYboc8wOl22-cDrQ1S0Rb5bbmfCQz_KyhRPu0RnHjTjmXLHMCMbZ3umwGRKMw6VvlUiFiKRYXbjApFT376bvuBiE8WtQGt95mFxemQMqjCUEyFUj_0_2hXNh2kZZHGUCIX7F7cPIFBm4LIUfOlBgFfjcUFYZZdMbd5c7pF7pW0gN9O7Eaq_oR0XmbCzKjietE4gCM61S9QOhAkAmOH12ItWDxBHpN2B_y8nSyivg3n5WM2OF198tQo0yX0mTPl6oOJ_Vri6xVJI8ty_qWjiWTJjqs1hCC_5WkV0FhUXzvm6BEvtoP9Kq4QJmMNR8P9HHaR0DOQYosf-LzmrseUd6dSdhWdOfM0KmLyqZ5itQ_5dZjbi1H0fJ65Yd41XrFqRYRpJtBTPBISH4msN5kbClpWmBO5LaduXSxWLdlQ3flPYVw0JnpfmgQTW2Y-VQvb10eEVs26MPqWt8lTZmKK3lqkDPGUrb7clo2n5PrQi09N1lH-0oeD5ArTCXe-9l8ZuVbfH2CoQRGzsIuazadR1QD9AjPoCIsp8ARJJGacAmNqF-W0VjY-vd5ecDQyPB9OaukzopKVQtzIONguJc9RwL445NZO6Mjux76EENmZkVjY1VjTIuIXCkPUInit19bk4oeCS2zg0ajuKvCXduir6vMkpsXkEfD2Xoy2oAAntGbZrYO011PVep6AUnA.zdUd6ISC4w8d1Pg1AeSdVA'
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

