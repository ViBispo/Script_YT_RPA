# 🚀 Automação com Selenium para Assistir Vídeos no YouTube

Este projeto usa **Selenium** para abrir o YouTube, pesquisar um vídeo de **Júlio Cocielo**, clicar no primeiro resultado e, caso haja anúncios, pular automaticamente.

## 📌 Funcionalidades
- Abre o **Google Chrome** com o perfil do usuário logado.
- Pesquisa **"Júlio Cocielo"** no YouTube.
- Clica no primeiro vídeo da pesquisa.
- **Verifica e pula anúncios automaticamente**, caso apareçam.
- Mantém o navegador aberto por um tempo para assistir ao vídeo.

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
     options.add_argument(r'--profile-directory=Profile 1')
     ```
   - Se necessário, altere "Profile 1" para **Default, Profile 2, etc.**

3. **Execute o script**:
   ```bash
   python nome_do_arquivo.py
   ```

---

## ⚙️ Explicação Técnica
### 🖥️ Tecnologias Usadas
- **Python**: Linguagem de programação usada para escrever o script.
- **Selenium**: Biblioteca para automação de navegadores.
- **WebDriver Manager**: Gerenciador automático do ChromeDriver.

### 📜 Como Funciona o Código?
1. **Abre o Chrome com o perfil do usuário logado**.
2. **Navega até o YouTube**.
3. **Pesquisa "Júlio Cocielo" e clica no primeiro vídeo**.
4. **Verifica se há um botão "Pular anúncio" e clica nele**.
5. **Mantém o vídeo rodando e depois fecha o navegador**.

### 🔄 Como a Automação Pula Anúncios?
- O script usa **Selenium** para procurar o botão de **"Pular anúncio"** (`ytp-skip-ad-button__text`).
- Se o botão aparecer, o Selenium **clica automaticamente** para pular o anúncio.

---

## ❗ Possíveis Erros e Soluções
| Erro | Solução |
|------|---------|
| `ModuleNotFoundError: No module named 'selenium'` | Instale a biblioteca com `pip install selenium` |
| `chrome.exe não encontrado` | Verifique se o Chrome está instalado corretamente |
| O Chrome abre sem estar logado | Confirme que `--user-data-dir` e `--profile-directory` estão corretos |

---

## 📌 Melhorias Futuras
- [ ] Criar um menu interativo para buscar qualquer canal/vídeo.
- [ ] Adicionar suporte a outros navegadores além do Chrome.
- [ ] Melhorar a detecção e o fechamento automático de anúncios.

---

## 🤝 Contribuição
Se quiser melhorar esse projeto, sinta-se à vontade para abrir um **Pull Request** ou relatar **issues**!

---

## 📝 Licença
Este projeto é de código aberto e pode ser usado livremente para aprendizado e experimentação.

🚀 **Divirta-se automatizando o YouTube!**