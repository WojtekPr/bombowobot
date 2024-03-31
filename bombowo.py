from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

class bombowobot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open_bombowo(self):
        self.driver.get('https://literalnie.fun/bombowo')   
        
        sleep(1)

        cookies = self.driver.find_element('xpath', '/html/body/div[2]/div[1]/div[2]/div/div[2]/button[2]')
        cookies.click()

        sleep(1)

        nickname_input = self.driver.find_element('xpath', '/html/body/div[1]/div[4]/div[1]/div/div/form/input[1]')
        nickname = self.nickname_generator()  # Wywołanie funkcji generującej pseudonim
        nickname_input.send_keys(nickname)
        
        sleep(1)

        zapisz = self.driver.find_element('xpath','/html/body/div[1]/div[4]/div[1]/div/div/form/input[2]')
        zapisz.click()

        sleep(1)

        cancelpop = self.driver.find_element('xpath','/html/body/div[1]/div[1]/div/div/button[1]')
        cancelpop.click()

        sleep(1)

        joingame = self.driver.find_element('xpath','/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/button')
        joingame.click()

        self.driver.implicitly_wait(10)
        self.szukanie_lobby()

    
    def szukanie_lobby(self):
            wait = WebDriverWait(self.driver, 10, poll_frequency=0.5)
            previous_text = None
            
            while True:
                # Znajdź element z tekstem na stronie
                element = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/div[3]/div[1]/div[2]/p')))
                current_text = element.text
                
                # Sprawdź czy tekst się zmienił
                if current_text != previous_text:
                    print('Tekst się zmienił:', current_text)
                    previous_text = current_text
                else:
                    print('Tekst nie zmienił się:', current_text)
                
                # Tutaj możesz umieścić dodatkowe warunki przerwania pętli
                # np. jeśli warunek został spełniony
                if current_text == 'Jakiś inny tekst':
                    break
        
                time.sleep(0.5) 

    def nickname_generator(self):
        nicknames = ["Anna", "Maria", "Katarzyna", "Małgorzata", "Agnieszka",
                     "Joanna", "Marta", "Dorota", "Ewa", "Magdalena",
                     "Aleksandra", "Monika", "Barbara", "Justyna", "Kinga",
                     "Natalia", "Beata", "Karolina", "Weronika", "Izabela"]
        
        
        selected = random.choice(nicknames)
        return selected
        

    def exit(self):
        input("Naciśnij dowolny klawisz, aby zakończyć...")
        self.driver.quit()

# Utworzenie instancji klasy i uruchomienie metody open_bombowo()
bot = bombowobot()
bot.open_bombowo()
bot.exit()