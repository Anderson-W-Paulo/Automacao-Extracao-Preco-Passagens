import time
from urllib.parse import quote
import pandas as pd
import datetime
import os
import pywhatkit as kit
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium import webdriver


def transforma_df(dados):
    df = pd.DataFrame(dados)

    # Captura data atual
    data_hoje = datetime.datetime.today()
    # Formata data
    data_hoje_formatada = data_hoje.strftime('%d-%m-%y')

    # Garantir que pasta exista
    pasta = 'Banco de Dados Passagens da Decolar'
    os.makedirs(pasta, exist_ok=True)
    # Define nome do arquivo sendo a data atual da solicitação.csv
    nome_arquivo = f'{pasta}/{data_hoje_formatada}.csv'
    # Salva df em arquivo .csv sem index
    df.to_csv(nome_arquivo, index=False, sep=';')

    # Perguntar se o usuário quer enviar o arquivo para o WhatsApp
    numero = '+5585999324729'
    enviar_mensagem_wpp2(numero)


def solicitar_dia():
    while True:
        valor = input('Informe o dia (1 a 31):')
        if valor.isdigit() and 1 <= int(valor) <= 31:
            return int(valor)
        else:
            print('Dia inválido! Digite corretamente entre 1 a 31')


def solicitar_mes():
    while True:
        valor = input('Informe o mês (1 a 12):')
        if valor.isdigit() and 1 <= int(valor) <= 12:
            return int(valor)
        else:
            print('Mês inválido! Digite corretamente entre 1 a 12')


def solicitar_ano():
    while True:
        valor = input('Informe o ano:')
        if valor.isdigit() and len(valor) == 4:
            return int(valor)
        else:
            print('Ano inválido! Digite o ano completo corretamente')


def enviar_mensagem_wpp1(numero):
    try:
        # Usando pywhatkit para enviar o arquivo pelo WhatsApp
        kit.sendwhatmsg(numero, "Aqui está o arquivo CSV das passagens.", 9, 13)
        driver = webdriver.Edge()
        driver.quit()
        botao_enviar_wpp = driver.find_element(By.XPATH, "//span[@data-icon='wds-ic-send-filled']")  # "Localiza o botão de envio buscando o atributo data-icon no HTML, garantindo uma seleção precisa e segura."
        botao_enviar_wpp.click()
        time.sleep(5)
        print(f"Arquivo enviado com sucesso para {numero}")
    except Exception as e:
        print(f"Erro ao enviar o arquivo: {e}")


def iniciar_chrome_com_perfil():
    options = Options()

    # Caminho para os dados do Chrome
    options.add_argument(r"--user-data-dir=C:\Users\ander\AppData\Local\Google\Chrome\User Data")
    options.add_argument(r"--profile-directory=Default")  # Ou "Profile 1", depende do seu perfil no Chrome

    # NÃO criar novo perfil, usar o existente
    options.add_experimental_option("detach", True)  # Mantém o navegador aberto depois do script se quiser

    driver = webdriver.Chrome(options=options)
    return driver


def enviar_mensagem_wpp2(numero):
    # Instancia e abre navegador
    driver = iniciar_chrome_com_perfil()
    try:
        # Codifica mensagem para padrão url
        mensagem = 'O Arquivo Valor das Passagens foi baixado automáticamente e salvo CSV'
        mensagem_codificada = quote(mensagem)

        # Abre wpp web com número e mensangem
        url = f'https://web.whatsapp.com/send?phone={numero}&text={mensagem_codificada}'
        driver.get(url)

        time.sleep(6)

        # Clicar no botão
        botao_enviar = driver.find_element(By.XPATH, "//span[@data-icon='wds-ic-send-filled']")
        botao_enviar.click()
        print(f'Mensagem enviada para número {numero}')

    except Exception as e:
        print(f'Erro ao enviar mensagem: {e}')

    finally:
        time.sleep(5) # esperar e garantir envio
        driver.quit() # fechar navegador

