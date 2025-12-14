from selenium.webdriver.common.by import By

from PagesObjects.BasePage import Basepage

class HomePage(Basepage):


    #locators

    bouton_register = (By.LINK_TEXT, "Register")
    bouton_login = (By.LINK_TEXT, "Log in")
    bouton_logout = (By.LINK_TEXT, "Log out")
    barre_de_recherche = (By.ID, "small-searchterms")
    bouton_search = (By.CSS_SELECTOR, ".search-box-button")

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

    def cliquer_sur_le_bouton_logout(self):
        self.cliquer_sur_un_element(self.bouton_logout)

    def visualiser_le_bouton_login(self):
        bouton_login = self.capturer_text_element(self.bouton_login)
        assert bouton_login == "Log in"

    def rechercher_un_article(self, text):
        self.saisir_du_text_dans_le_champ(self.barre_de_recherche, text)

    def cliquer_sur_le_bouton_search(self):
        self.cliquer_sur_un_element(self.bouton_search)

    def cliquer_sur_une_categorie(self, categorie):
        self.driver.find_element(By.LINK_TEXT, categorie).click()
