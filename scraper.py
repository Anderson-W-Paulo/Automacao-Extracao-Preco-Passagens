from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


'''# captura data, transforma para adqui 4 semanas
data_hoje = datetime.now()
print(data_hoje)
data_daqui_um_mes = data_hoje + timedelta(weeks=4)
data_formatada = data_daqui_um_mes.strftime(f'%d/%m/%Y')
print(data_formatada)'''

'''resposta = requests.get(link)
if resposta.status_code == 200:
    print('SUCESSO GETTER')
else:
    print(f'Falha: {resposta.status_code}')

soup = BeautifulSoup(resposta.text, 'html.parser')
'''


def extrair_valores_passagem():
    link1 = 'https://www.decolar.com/shop/flights/results/oneway/FOR/OPO/2025-05-27/1/0/0?from=SB&di=1&reSearch=true'
    driver = webdriver.Chrome()
    driver.get(link1)

    # Fechar Pop-Up
    '''<span class="login-aggressive--button login-aggressive--button-close shifu-3-btn-ghost">
                <em class="btn-text">Não quero benefícios</em>
            </span>'''
    campo_fechar = driver.find_element(By.XPATH, "//em[text()='Não quero benefícios']") # caminha pelos elementos HTML de forma flexível e específica, indo direto pelo texto, assim encontrando o elemento desejado da página
    campo_fechar.click()
    time.sleep(1)

    html = driver.page_source # capturar HTML da página após renderizar na página
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
'''
    # Resgatar dados das passagens
    div_principal = soup.find('div', id='clusters')
    itens = div_principal.find_all('div', class_='cluster-container COMMON')

    lista_passagens = []
    # Loop e resgate dos dados pro passagem
    for item in itens:
        data_viagem = item.find_next('span', class_='route-info-item-date lowercase').text.strip()
        companhia_area = item.find_next('span', class_='name').text.strip()
        horario_saida = item.find_next('span', class_='hour').text.strip()
        duracao_viagem = item.find_next('span', class_='duration-text').text.strip()
        horarior_chegada = item.find_next('span', class_='hour-wrapper hover-cursor').text.strip()
        preco_passagem = item.find_next('span', class_='amount price-amount').text.strip().replace('.', '')
        imposto_sobre_passagem = item.find_next('span', class_='amount price-amount').text.strip().replace('.', '')

        # Guardar informarções no dicionário e adicinoar na lista
        passagem = {'data-viagem': data_viagem,
                    'companhia-aerea': companhia_area,
                    'saida': horario_saida,
                    'chegada': horarior_chegada,
                    'duracao': duracao_viagem,
                    'preco-passagem': int(preco_passagem),
                    'imposto-passagem': int(imposto_sobre_passagem)}
        lista_passagens.append(passagem)
    driver.quit() # fecha navegador inteiro

    for i in lista_passagens:
        print(i)'''


'''        
 # Resgatar valores das passagens
    <span _ngcontent-ttj-c82="" class="amount price-amount">
                                         3.700
                                        </span>
    valores = soup.find_all('span', class_='amount price-amount')
    lista_valores = []
    for v in valores:
        texto = v.text.strip().replace('.', '')
        numero = float(texto)
        if numero > 1200: # valor médio encontra-se sempre acima
            lista_valores.append(numero)
    print('\n\n', lista_valores)
    # Salva valor mais barata das passagens
    valor_min = min(lista_valores)
    print(valor_min)
'''

extrair_valores_passagem()