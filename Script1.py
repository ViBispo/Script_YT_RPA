from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

def iniciar_driver():
    options = webdriver.ChromeOptions()
    
    # Ajuste aqui para o caminho do seu perfil
    options.add_argument(r'--user-data-dir=C:\\Users\\Victor\\AppData\\Local\\Google\\Chrome\\User Data')
    options.add_argument(r'--profile-directory=Default')

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    return driver

def buscar_video_youtube(driver, termo_busca):
    driver.get("https://www.youtube.com")
    time.sleep(2)

    search_box = driver.find_element(By.NAME, "search_query")
    search_box.send_keys(termo_busca)
    search_box.send_keys(Keys.RETURN)
    time.sleep(3)

    first_video = driver.find_element(By.XPATH, "//ytd-video-renderer[1]//a[@id='thumbnail']")
    first_video.click()
    time.sleep(5)

    pular_anuncio(driver)
    
    aguardar_fim_video(driver)

def pular_anuncio(driver):
    while True:
        try:
            botao_pular = driver.find_element(By.CLASS_NAME, "ytp-skip-ad-button__text")
            botao_pular.click()
            print("Anúncio pulado!")
            break
        except:
            pass
        
        time.sleep(1)

def aguardar_fim_video(driver):
    while True:
        try:
            # Obtém a duração total e o tempo atual do vídeo
            tempo_total = driver.execute_script("return document.querySelector('video').duration")
            tempo_atual = driver.execute_script("return document.querySelector('video').currentTime")
            
            print(f"Tempo atual: {tempo_atual:.2f} / {tempo_total:.2f}")

            # Se o vídeo estiver perto do fim (1 segundo de diferença), retorna ao menu
            if tempo_total - tempo_atual < 1:
                print("O vídeo terminou! Voltando ao menu...")
                break
        except:
            pass

        time.sleep(5)

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

menu_interativo()
