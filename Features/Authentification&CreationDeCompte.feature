
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


  Scenario Outline: Connexion valide
    Given je clique sur "Log in"
    When je saisis un email et mot de passe valides <email> <password>
    And je clique sur "Log in"
    Then je suis connecté et je vois le lien "Log out"

    Examples:
    |email               | password   |
    |mdenis@example.com  | ^5W5L9z2q3 |

