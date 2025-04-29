'''
Mini Projeto: Atualizador Automático de Preços de Produtos:
Criar um script que verifica automaticamente o preço das passagens de um site (escolhi decolar) e salva os principais dados em um banco de dados (escolhi arquivo csv).
'''

from scraper_poo import ExtrairDadosPassagens
import funcoes

print('============ATUALIZADOR DE PREÇOS AUTOMÁTICO - PASSAGENS ÁREAS DO SITE DECOLAR============\n')
print('Informe a data que gostaria de verificar os preços')

# Solicitar as data com verificação correta para minimar o máximo possível de erros do usuário
dia = funcoes.solicitar_dia()
mes = funcoes.solicitar_mes()
ano = funcoes.solicitar_ano()

# Transformando data
data_formatada = f'{ano}-{mes:02d}-{dia:02d}'


link_url = f'https://www.decolar.com/shop/flights/results/oneway/FOR/OPO/{data_formatada}/1/0/0?from=SB&di=1&reSearch=true'

passagem = ExtrairDadosPassagens(link_url)
passagem.scraping_valores_passagem()




