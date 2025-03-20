from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do Selenium para abrir o Chrome com o perfil do usuário
def iniciar_driver():
    options = webdriver.ChromeOptions()
    
    options.add_argument(r'--user-data-dir=C:\Users\Victor\AppData\Local\Google\Chrome\User Data')
    options.add_argument(r'--profile-directory=Default')


    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

# Função para buscar um vídeo no YouTube
def buscar_video_youtube(driver, termo_busca):
    driver.get("https://www.youtube.com")
    time.sleep(2)

    # Encontra a barra de pesquisa e insere o termo
    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys(termo_busca)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    first_video = driver.find_element(By.XPATH, "//ytd-video-renderer[1]//a[@id='thumbnail']")
    first_video.click()
    time.sleep(5)

    pular_anuncio(driver)

# Função para pular anúncios automaticamente
def pular_anuncio(driver):
    while True:
        try:
            botao_pular = driver.find_element(By.CLASS_NAME, "ytp-skip-ad-button__text")
            botao_pular.click()
            print("🔥 Anúncio pulado!")
            break  
        except:
            pass  
        
        time.sleep(1)

# 📜 Menu interativo para o usuário escolher a ação
def menu_interativo():
    driver = iniciar_driver()
    while True:
        print("\n🎬 MENU DO BOT YOUTUBE 🎬")
        print("1️⃣ - Buscar um vídeo")
        print("2️⃣ - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            termo = input("Digite o nome do vídeo ou canal: ")
            buscar_video_youtube(driver, termo)
        elif opcao == "2":
            print("🚪 Fechando o navegador e encerrando...")
            driver.quit()
            break
        else:
            print("❌ Opção inválida! Tente novamente.")

# Inicia o menu interativo
menu_interativo()
