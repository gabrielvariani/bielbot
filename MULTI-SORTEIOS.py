from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
from datetime import datetime

class instagrambot:
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:/Users/COAL/Desktop/documentos/get/geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(5)
        campo_usuario = driver.find_element_by_xpath("//input[@name='username']")
        campo_usuario.click()
        campo_usuario.clear()
        campo_usuario.send_keys(self.username)
        campo_senha = driver.find_element_by_xpath("//input[@name='password']")
        campo_senha.click()
        campo_senha.clear()
        campo_senha.send_keys(self.password)
        botao_entrar = driver.find_element_by_xpath("//button[@type='submit']")
        botao_entrar.click()
        time.sleep(5)
        contador = 1 
        while (contador <4000): 
            driver = self.driver
            file = open("C:/Users/COAL/Desktop/documentos/get/fws.txt", "r")
            datas = file.read()
            words = datas.split()
            driver.get("https://www.instagram.com/p/CQyYy3VMHnm/")
            time.sleep(5)
            driver.find_element_by_class_name('Ypffh').click()
            comentario = driver.find_element_by_class_name('Ypffh')
            word_pos = random.randint(0, len(words)-1)
            comentario.send_keys(words[word_pos]+" ")
            time.sleep(2)
            word_pos2 = random.randint(0, len(words)-1)
            comentario.send_keys(words[word_pos2]+" ")
            driver.find_element_by_xpath("//button[@type='submit']").click()
            now = datetime.now()
            hora = now.hour
            minutos = now.minute
            segundos = now.second
            dia = now.day
            mes = now.month
            ano = now.year
            print("PRIMO GAMES - PS5: "+str(contador)+"º "+str(dia)+"/"+str(mes)+"/"+str(ano)+" - "+str(hora)+":"+str(minutos)+":"+str(segundos),"\n",words[word_pos],"POSIÇÃO:"+str(word_pos),"\n",words[word_pos2],"POSIÇÃO:"+str(word_pos2))
            time.sleep(random.randint(300,600))
            

            contador = contador + 1

bielbot = instagrambot('gabrielvariani','Camilo31')
bielbot.login()