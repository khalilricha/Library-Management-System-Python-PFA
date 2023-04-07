# PFAPython
Library Management System - PFA PROJECT

Implémentation d'une application de gestion de bibliothèque à l'aide de Python Tkinter
+ Connexion avec une base de données MYSQL via XAMPP

3 Python Files : 

1) Login.py --> Page de connexion : Une classe Login contenant
Un Champ pour saisir l'username,
Un Champ pour saisir le mot de passe,
Un bouton de connexion qui redirige l'utilisateur vers la page principale du système de gestion main.py,
Un bouton de création de compte qui redirige l'utilisateur vers la page formulairecreation.py afin de créer un compte,
Une connexion avec une base de données MYSQL via XAMPP.

2) FormulaireCreation.py --> Page de création de compte :
Similaire à Login.py avec une classe Formulaire contenant un bouton de validation de création et un bouton de redirection vers la page de connexion,
Une connexion avec une base de données MYSQL via XAMPP pour mémoriser les entrées de l'utilisateur.

3) Main.py --> Page principale du système de gestion :Une classe Bibiliothèque contenant
Une première zone(Frame) avec des champs pour saisir les informations du livre : ID, Titre, Auteur, Année,
4 Boutons : Ajouter, Modifier, Supprimer et Réinitialiser assimilés à 4 Fonctions,
Une deuxième zone(Frame) avec un tableau liée à une base de données MYSQL via XAMPP pour stocker les informations du livre saisies par l'utilisateur,
Une checkbox de recherche, une entrée de l'élément à rechercher, un bouton Rechercher et un bouton Afficher Tout.

Tous les éléments implémentés sont commentés au niveau du code source.

