import time

import allure
from pytest_bdd import *

from PagesObjects.HomePage import HomePage
from PagesObjects.SearchPage import SearchPage

scenarios("../Features/Recherche&Navigation.feature")

@allure.feature("Recherche&Navigation.feature")

@given("je suis sur la page d’accueil")
@allure.step("user est sur la page d accueil")
def user_est_sur_home_page(setup):
    pass


@when('je saisis "book" dans la barre de recherche')
@allure.step("user saisit un mot dans la barre de recherche")
def user_effectue_une_recherche(home_page: HomePage):
    home_page.rechercher_un_article('book')

@step('je clique sur search')
@allure.step('user valide ca recherche')
def user_clique_sur_search(home_page: HomePage):
    home_page.cliquer_sur_le_bouton_search()

@step('Je suis redirigé vers la page recherche')
@allure.step('redirection vers la page recherche')
def user_redirige_vers_la_page_search(search_page: SearchPage):
    search_page.verifier_le_titre_de_la_page("Demo Web Shop. Search")

@step('le terme "book" apparaît dans le résultat de la recherche')
@allure.step('resultat de la recherche OK')
def user_visualise_ca_recherche(search_page: SearchPage):
    search_page.verifier_que_larticle_apparait_dans_la_recherche("book")

@when('je clique sur la catégorie "Books"')
@allure.step('clique sur la categorie books')
def user_clique_sur_books(home_page):
    home_page.cliquer_sur_une_categorie("Books")

@then("je suis redirigé vers la page Books")
@allure.step('Redirection vers la page books')
def user_redirige_vers_la_page_books(categorie_page):
    categorie_page.verifier_le_titre_de_la_page("Demo Web Shop. Books")

@step('le fil d\'Ariane affiche "HOME/BOOKS"')
@allure.step("fil d'Ariane affiche BOOKS")
def user_visualise_book_dans_le_fil_dariane(categorie_page):
    categorie_page.verifier_que_book_est_visible_dans_le_fil_dariane()
