from selenium import webdriver
from time import sleep

class bombowobot():
    def __init__(self):
        self.driver = webdriver.Chrome()
    def open_bombowo(self):
        self.driver.get('https://literalnie.fun/bombowo')
        
        sleep(1)

        cookies = self.driver.find_element('xpath', '/html/body/div[2]/div[1]/div[2]/div/div[2]/button[2]')
        cookies.click()

        sleep(1)

        nickname = self.driver.find_element('xpath', '/html/body/div[1]/div[4]/div[1]/div/div/form/input[1]')
        nickname.send_keys("pnrtrot3000")

        sleep(1)

        zapisz = self.driver.find_element('xpath','/html/body/div[1]/div[4]/div[1]/div/div/form/input[2]')
        zapisz.click()

        sleep(1)

        cancelpop = self.driver.find_element('xpath','/html/body/div[1]/div[1]/div/div/button[1]')
        cancelpop.click()

        sleep(1)

        joingame = self.driver.find_element('xpath','/html/body/div[1]/div[2]/div[3]/div[1]/div[1]/div/button')
        joingame.click()

        sleep(30)


        # Poczekaj na wyniki, aby zobaczyć efekt
        input("Naciśnij dowolny klawisz, aby zakończyć...")
        self.driver.quit()
        


bot = bombowobot()
bot.open_bombowo()
