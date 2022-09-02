from selenium import webdriver
import time

#Inserir em nome e sobrenome cadeia de caracteres
#repetida com comprimento especificado em 20

from selenium.webdriver.common.by import By

drive = webdriver.Chrome(executable_path=r'./chromedriver.exe')
drive.get('https://mateusmais.com.br/cadastro')
drive.maximize_window()

nome = 'aaaaaaaaaaaaaaaaaaaa'
sobrenome = 'aaaaaaaaaaaaaaaaaaaa'

campoNome = drive.find_element(By.CSS_SELECTOR,"#mat-tab-content-0-0 > div > div > gmf-input.ng-untouched.ng-pristine.ng-valid > div > div > input")
time.sleep(1)
campoNome.send_keys(nome)

campoSobrenome = drive.find_element(By.CSS_SELECTOR,"#mat-tab-content-0-0 > div > div > gmf-input.ng-untouched.ng-pristine.ng-valid > div > div > input")
time.sleep(1)
campoSobrenome.send_keys(sobrenome)

botao_entrar = drive.find_element(By.CSS_SELECTOR,"body > app-root > app-master-page > app-register > div > div > div > gmf-button > div > button > div.content.--gmf-text > div")
time.sleep(1)
botao_entrar.click()