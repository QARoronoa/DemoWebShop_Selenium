
Feature: Authentification & Création de compte

  Background:
    Given je suis sur la page d’accueil

  Scenario: Inscription réussie
    Given je clique sur "Register"
    And je renseigne un genre, un prénom, un nom, un email non utilisé et un mot de passe valide
    And je soumets le formulaire
    Then je suis connecté et mon nom s’affiche dans l’en-tête

  Scenario: Inscription avec email déjà utilisé
    Given je clique sur "Register"
    When je saisis le même email et je soumets
    And je soumets le formulaire
    Then un message d’erreur m’indique que l’email existe déjà
