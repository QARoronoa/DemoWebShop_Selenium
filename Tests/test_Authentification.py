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


@step('je renseigne un genre, un prénom, un nom, un email non utilisé et un mot de passe valide')
def formulaire_register(login_page: LoginPage, formulaire_enregistrement):
    login_page.remplir_le_formulaire_register(**formulaire_enregistrement)


@step('je soumets le formulaire')
def soumettre_formulaire(login_page):
    login_page.cliquer_sur_le_bouton_register()

@then('je suis connecté et mon nom s’affiche dans l’en-tête')
def lutilisateur_est_connecte(login_page):
    login_page.verifier_que_lutilisateur_est_connecte()

