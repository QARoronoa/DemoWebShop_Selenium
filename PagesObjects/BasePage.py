import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Basepage():
    def __init__(self, driver):
        self.driver = driver

    @allure.step("Le titre est '{titreAttendu}'")
    def verifier_le_titre_de_la_page(self, titreAttendu):
        titre = self.driver.title
        assert titre == titreAttendu, f"Titre obtenu '{titre}', titre attendu '{titreAttendu}'"

    @allure.step("Cliquer sur {locator}")
    def cliquer_sur_un_element(self, locator):
        element = WebDriverWait(self.driver,20).until(EC.visibility_of_element_located(locator))
        element.click()

    @allure.step("Le texte '{text}' est saisie")
    def saisir_du_text_dans_le_champ(self, locator, text):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Capturer le texte de l'élément")
    def capturer_text_element(self, locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return element.text