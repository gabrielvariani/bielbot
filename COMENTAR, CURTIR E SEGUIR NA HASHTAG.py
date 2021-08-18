from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class instagrambot:
    def __init__ (self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path="C:/Users/COAL/Desktop/get/geckodriver.exe")

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
        self.comentarios('concursopublico')
   
    @staticmethod
    def digitar_como_uma_pessoa(frase,onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comentarios(self,hashtag):
        driver = self.driver   
        driver.get("https://www.instagram.com/explore/tags/"+ hashtag +"/")
        time.sleep(3)

        for i in range(1,500):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(5)
        
        hrefs = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href') for elem in hrefs]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos ' + str(len(pic_hrefs)))

        for pic_href in pic_hrefs:
            driver.get(pic_href)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            try:
                comentario = ["Muito bem!","Boa!","Pra cima!","Com fé e luta conseguiremos!","Nunca será somente a vitória, mas sim a caminhada!","Sucesso!","Vamos conseguir!","Com fé em Deus!","Muito bom!","Isso mesmo!","Deus abençoe!","Amém!","Toda vitória é de Deus!","Se Deus quiser!","Trabalhe duro, viva intensamente!","Luta diária, vida mansa!","Seja feita a Tua vontade!","Isso aí!","Que venha mais e mais conquistas!","Vitória!"]
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(random.randint(2,5))
                self.digitar_como_uma_pessoa(random.choice(comentario),campo_comentario)
                driver.find_element_by_xpath("//button[contains(text(),'Publicar')]").click()
                time.sleep(3)
                driver.find_element_by_class_name('fr66n').click()
                time.sleep(3)
                driver.find_element_by_class_name('bY2yH').click()
                time.sleep(random.randint(60,150))
                
            except Exception as e:
                print(e)
                time.sleep(5)

bielbot = instagrambot('concursado21','leirbaG3031')
bielbot.login()
bielbot.comentarios()