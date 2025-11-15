from selenium.webdriver.common.by import By

from PagesObjects.BasePage import Basepage

class HomePage(Basepage):


    #locators

    bouton_register = (By.LINK_TEXT, "Register")
    bouton_login = (By.LINK_TEXT, "Log in")
    bouton_logout = (By.LINK_TEXT, "Log out")

    def __init__(self, driver):
        super().__init__(driver)

    #methodes
    def verifier_le_titre_home_page(self, titre):
        self.verifier_le_titre_de_la_page(titre)

    def cliquer_sur_register(self):
        self.cliquer_sur_un_element(self.bouton_register)

    def cliquer_sur_le_bouton_login(self):
        self.cliquer_sur_un_element(self.bouton_login)

    def visualiser_le_bouton_logout(self):
        texte = self.capturer_text_element(self.bouton_logout)
        assert texte == "Log out", f"attendu 'Logout', obtenu {texte}"
