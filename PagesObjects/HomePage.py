from selenium.webdriver.common.by import By

from PagesObjects.BasePage import Basepage

class HomePage(Basepage):


    #locators

    bouton_register = (By.LINK_TEXT, "Register")

    def __init__(self, driver):
        super().__init__(driver)

    #methodes
    def verifier_le_titre_home_page(self, titre):
        self.verifier_le_titre_de_la_page(titre)

    def cliquer_sur_register(self):
        self.cliquer_sur_un_element(self.bouton_register)
