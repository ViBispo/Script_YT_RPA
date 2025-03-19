from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def acessar_video_julio_cocielo():
    # Configurações do Chrome
    options = webdriver.ChromeOptions()

    options.add_argument(r'--user-data-dir=C:\Users\Victor\AppData\Local\Google\Chrome\User Data')
    options.add_argument(r'--profile-directory=Default')

    # Inicia o Chrome com o perfil do usuário
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        # Acessa o YouTube
        driver.get("https://www.youtube.com")
        time.sleep(2)

        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("Júlio Cocielo")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)

        # Clica no primeiro vídeo
        first_video = driver.find_element(By.XPATH, "//ytd-video-renderer[1]//a[@id='thumbnail']")
        first_video.click()
        time.sleep(5)

    except Exception as e:
        print(f"Erro: {e}")
    finally:
        time.sleep(100)
        driver.quit()

acessar_video_julio_cocielo()
