Feature: Recherche & Navigation Catalogue

  Background:
    Given je suis sur la page d’accueil

  Scenario: Recherche par mot-clé
    When je saisis "book" dans la barre de recherche
    And je clique sur search
    Then Je suis redirigé vers la page recherche
    And le terme "book" apparaît dans le résultat de la recherche

  Scenario: Navigation par categorie
    When je clique sur la catégorie "Books"
    Then je suis redirigé vers la page Books
    And le fil d'Ariane affiche "HOME/BOOKS"

#  Scenario: Tri des produits
#    Given je suis sur la catégorie "Books"
#    When je sélectionne "Price: Low to High" dans le tri
#    Then les produits sont affichés dans l’ordre de prix croissant
#
#  Scenario: Pagination (suivant)
#    Given je suis sur une catégorie avec plusieurs pages de produits
#    When je clique sur la page suivante
#    Then la page suivante de produits est affichée
