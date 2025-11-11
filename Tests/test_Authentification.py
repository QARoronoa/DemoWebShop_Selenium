import time

import allure
from pytest_bdd import *
from PagesObjects.HomePage import HomePage
from PagesObjects.LoginPage import LoginPage

scenarios('../Features/Authentification&CreationDeCompte.feature')


@allure.feature('Authentification & Création de compte')
@given('je suis sur la page d’accueil')
def open_home_page(home_page: HomePage):
    home_page.verifier_le_titre_de_la_page("Demo Web Shop")


# -----------Inscription-----------#
@given('je clique sur "Register"')
def cliquer_sur_register(home_page: HomePage):
    home_page.cliquer_sur_register()
    allure.step("Ouverture de la page de connexion")


@step('je renseigne un genre, un prénom, un nom, un email non utilisé et un mot de passe valide')
def formulaire_register(login_page: LoginPage, formulaire_enregistrement):
    login_page.remplir_le_formulaire_register(**formulaire_enregistrement)
    allure.step("Le formulaire est remplie")


@step('je soumets le formulaire')
def soumettre_formulaire(login_page):
    login_page.cliquer_sur_le_bouton_register()
    allure.step("Soumission du formulaire")

@then('je suis connecté et mon nom s’affiche dans l’en-tête')
def lutilisateur_est_connecte(login_page):
    login_page.verifier_que_lutilisateur_est_connecte()
    allure.step("L'utilisateur est connecté'")


#________Inscription avec email déjà utilisé____________#

@when('je saisis le même email et je soumets')
def Lutilisateur_remplie_le_formulaire_avec_credentials_existant(login_page, formulaire_enregistrement_echoue):
    login_page.remplir_le_formulaire_register(**formulaire_enregistrement_echoue)
    login_page.cliquer_sur_le_bouton_register()

@then('un message d’erreur m’indique que l’email existe déjà')
def visualiser_message_derreur_mail_existant(login_page):
    login_page.verifier_message_derreur_email_deja_existant()

