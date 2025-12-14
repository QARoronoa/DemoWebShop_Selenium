from selenium.webdriver.common.by import By

from PagesObjects.BasePage import Basepage


class CategoriePage(Basepage):

    #locators
    fil_d_Ariane = (By.CSS_SELECTOR, ".current-item")
    #methodes
    def __init__(self, driver):
        super().__init__(driver)

    def verifier_le_titre_de_la_page_de_la_categorie(self):
        self.verifier_le_titre_de_la_page()

    def verifier_que_book_est_visible_dans_le_fil_dariane(self):
        self.capturer_text_element(self.fil_d_Ariane)