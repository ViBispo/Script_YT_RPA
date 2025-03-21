# 🚀 Automação com Selenium para Assistir Vídeos no YouTube

Este projeto usa **Selenium** para abrir o YouTube, pesquisar um vídeo, clicar no primeiro resultado e, caso haja anúncios, pular automaticamente. Além disso, agora possui um **menu interativo** que permite buscar qualquer vídeo sem precisar reiniciar o script, e aguarda o fim do vídeo antes de retornar ao menu.

## 📌 Funcionalidades
- Abre o **Google Chrome** com o perfil do usuário logado.
- Exibe um **menu interativo** para escolher ações.
- Pesquisa **qualquer vídeo ou canal** no YouTube.
- Clica no primeiro vídeo da pesquisa.
- **Verifica e pula anúncios automaticamente**, caso apareçam.
- **Monitora o tempo do vídeo** e retorna ao menu quando o vídeo termina.
- Permite ao usuário fazer várias buscas sem reiniciar o script.

---

## 🛠️ Pré-requisitos
Antes de rodar o código, você precisa:

1. **Ter o Python instalado**
   - Baixe e instale o Python em: [https://www.python.org/downloads/](https://www.python.org/downloads/)
   - Verifique se está instalado corretamente:
     ```bash
     python --version
     ```

2. **Instalar as bibliotecas necessárias**
   Abra o terminal ou prompt de comando e execute:
   ```bash
   pip install selenium webdriver-manager
   ```

3. **Ter o Google Chrome instalado**
   - O Selenium precisa do Chrome para navegar na web.

---

## 🔥 Como Executar
1. **Verifique o caminho do seu perfil do Chrome**:
   - No Chrome, digite na barra de endereços:
     ```
     chrome://version/
     ```
   - Copie o caminho indicado em **"Perfil do caminho"**.

2. **Atualize o código com o caminho correto do perfil**
   - No código, substitua:
     ```python
     options.add_argument(r'--user-data-dir=C:\Users\SEU_USUARIO\AppData\Local\Google\Chrome\User Data')
     options.add_argument(r'--profile-directory=Default')
     ```
   - Se necessário, altere "Default" para **Profile 1, Profile 2, etc.**

3. **Execute o script**:
   ```bash
   python nome_do_arquivo.py
   ```

4. **Escolha uma opção no menu interativo**
   - `1` para buscar um vídeo.
   - `2` para sair do programa.

---

## ⚙️ Explicação Técnica
### 🖥️ Tecnologias Usadas
- **Python**: Linguagem de programação usada para escrever o script.
- **Selenium**: Biblioteca para automação de navegadores.
- **WebDriver Manager**: Gerenciador automático do ChromeDriver.

### 📜 Como Funciona o Código?
1. **Abre o Chrome com o perfil do usuário logado**.
2. **Exibe um menu interativo para o usuário escolher entre buscar um vídeo ou sair**.
3. **Pesquisa um vídeo no YouTube e clica no primeiro resultado**.
4. **Verifica se há um botão "Pular anúncio" e clica nele**.
5. **Monitora o tempo do vídeo usando JavaScript para detectar quando ele termina**.
6. **Retorna ao menu automaticamente após o vídeo finalizar.**
7. **Permite múltiplas buscas sem reiniciar o script.**
8. **Fecha o navegador ao sair do menu.**

### 🔄 Como a Automação Pula Anúncios?
- O script usa **Selenium** para procurar o botão de **"Pular anúncio"** (`ytp-skip-ad-button__text`).
- Se o botão aparecer, o Selenium **clica automaticamente** para pular o anúncio.
- Caso não haja anúncio, ele aguarda o vídeo até o final normalmente.

---

## ❗ Possíveis Erros e Soluções
| Erro | Solução |
|------|---------|
| `ModuleNotFoundError: No module named 'selenium'` | Instale a biblioteca com `pip install selenium` |
| `chrome.exe não encontrado` | Verifique se o Chrome está instalado corretamente |
| O Chrome abre sem estar logado | Confirme que `--user-data-dir` e `--profile-directory` estão corretos |

---

## 📌 Melhorias Futuras
- [ ] Criar uma interface gráfica com `Tkinter` para facilitar a interação.
- [ ] Adicionar suporte a outros navegadores além do Chrome.
- [ ] Melhorar a detecção e o fechamento automático de anúncios.
- [ ] Permitir que o usuário defina o tempo de exibição ou avance manualmente.

---

## 🤝 Contribuição
Se quiser melhorar esse projeto, sinta-se à vontade para abrir um **Pull Request** ou relatar **issues**!

---

## 📝 Licença
Este projeto é de código aberto e pode ser usado livremente para aprendizado e experimentação.

🚀 **Divirta-se automatizando o YouTube!**
