from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PagesObjects.BasePage import Basepage

class LoginPage(Basepage):

    #locators
        #register
    champ_gender = (By.ID, "gender-male")
    champ_first_name = (By.ID, "FirstName")
    champ_last_name = (By.ID, "LastName")
    champ_email = (By.ID, "Email")
    champ_password = (By.ID, "Password")
    champ_confirm_password = (By.ID, "ConfirmPassword")
    bouton_register = (By.ID, "register-button")
    message_erreur_emailExistant = (By.CSS_SELECTOR, 'div.validation-summary-errors li')
    champ_email_login = (By.ID,"Email")
    champ_password_login = (By.ID, "Password")
    bouton_login = (By.CSS_SELECTOR, ".login-button")
    message_erreur_connexion_ko = (By.CSS_SELECTOR, ".validation-summary-errors")


    #methodes
    def __init__(self, driver):
        super().__init__(driver)


    def remplir_le_formulaire_register(self, firstName, lastName, email, password, confirmPassword):
        self.cliquer_sur_un_element(self.champ_gender)
        self.saisir_du_text_dans_le_champ(self.champ_first_name, firstName)
        self.saisir_du_text_dans_le_champ(self.champ_last_name, lastName)
        self.saisir_du_text_dans_le_champ(self.champ_email, email)
        self.saisir_du_text_dans_le_champ(self.champ_password, password)
        self.saisir_du_text_dans_le_champ(self.champ_confirm_password, confirmPassword)

    def cliquer_sur_le_bouton_register(self):
        self.cliquer_sur_un_element(self.bouton_register)

    def verifier_que_lutilisateur_est_connecte(self):
        WebDriverWait(self.driver, 20).until(EC.invisibility_of_element_located(self.bouton_register))

    def verifier_message_derreur_email_deja_existant(self):
        # self.driver.find_element(By.CSS_SELECTOR, ".validation-summary-errors li")
        element = self.capturer_text_element(self.message_erreur_emailExistant)
        assert "The specified email already exists" in element

    def saisir_mdp_et_password(self, email, password):
        self.saisir_du_text_dans_le_champ(self.champ_email_login, email)
        self.saisir_du_text_dans_le_champ(self.champ_password_login, password)

    def cliquer_sur_le_bouton_login(self):
        self.cliquer_sur_un_element(self.bouton_login)

    def verifier_message_connexion_ko_est_visible(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.message_erreur_connexion_ko))
        return True


