from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
import funcoes


class ExtrairDadosPassagens:
    def __init__(self, link):
        self.link = link

    def scraping_valores_passagem(self):
        driver = webdriver.Chrome()
        driver.get(self.link)

        # Fechar Pop-Up
        '''<span class="login-aggressive--button login-aggressive--button-close shifu-3-btn-ghost">
                    <em class="btn-text">Não quero benefícios</em>
                </span>'''
        campo_fechar = driver.find_element(By.XPATH, "//em[text()='Não quero benefícios']")  # caminha pelos elementos HTML de forma flexível e específica, indo direto pelo texto, assim encontrando o elemento desejado da página
        campo_fechar.click()
        time.sleep(1)

        html = driver.page_source  # capturar HTML da página após renderizar na página
        soup = BeautifulSoup(html, 'html.parser')
        # print(soup.prettify())

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

            # Guardar informarções no dicionário e adicinoar na lista
            passagem = {'data-viagem': data_viagem,
                        'companhia-aerea': companhia_area,
                        'saida': horario_saida,
                        'chegada': horarior_chegada,
                        'duracao': duracao_viagem,
                        'preco-passagem': int(preco_passagem)}
            lista_passagens.append(passagem)
        driver.quit()  # fecha navegador inteiro

        # chama função do funcoes.py para salver em csv e se tornar um arquivo manipulável
        funcoes.transforma_df(lista_passagens)

        for i in lista_passagens:
            print(i)

