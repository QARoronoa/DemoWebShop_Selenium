from selenium.webdriver.common.by import By

from PagesObjects.BasePage import Basepage

class SearchPage(Basepage):

    #locators
    champ_resultat_recherche = (By.CSS_SELECTOR, "#Q" )

    def __init__(self, driver):
        super().__init__(driver)

    #methodes

    def verifier_que_larticle_apparait_dans_la_recherche(self, article):
        champ_search = self.capturer_text_element(self.champ_resultat_recherche)
        assert  article ==  article