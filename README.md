# Age and Gender Prediction Application

## Description
Cette application console permet de prédire le **genre** et l'**âge** d'une personne en fonction de son prénom. Elle utilise les API publiques [Genderize.io](https://genderize.io/) et [Agify.io](https://agify.io/) pour fournir des prédictions avec un certain degré de probabilité.

---

## Fonctionnalités
- **Prédiction du genre** : Entrez un prénom, et l'application prédit le genre (homme ou femme) avec une probabilité associée.
- **Prédiction de l'âge** : Entrez un prénom, et l'application estime l'âge moyen des personnes portant ce prénom.
- **Menu interactif** : Naviguez facilement entre les options ou quittez l'application.

---

## Prérequis
- Python 3.x
- Les modules Python suivants :
  - `os`
  - `requests`

Installez le module requests si nécessaire:
```bash
pip install requests
```

---

## Installation
1. Clonez ou téléchargez ce dépôt.
2. Assurez-vous que **Python** est correctement installé sur votre machine.
3. Exécutez le script **Python** dans un terminal compatible:

```bash
python age_gender_prediction.py
```

---

## Utilisation
1. Lancez l'application.
2. Le menu principal propose les options suivantes:
   - 1: Prédiction du genre en fonction d'un prénom.
   - 2: Prédiction de l'âge en fonction d'un prénom.
   - 9: Quitter l'application.
3. Suivez les instructions affichées sur l'écran.

---

## Exemple de sortie
### Prédiction du genre:
```
-------------------------
Age and gender prediction
-------------------------
1) Predict Gender
2) Predict Age
.
9) Quit

Choice: 1
Predict the gender of a name: Alice
ALICE is FEMALE with 97% certainty.
```

### Prédiction de l'âge:
```
-------------------------
Age and gender prediction
-------------------------
1) Predict Gender
2) Predict Age
.
9) Quit

Choice: 2
Predict the age of a name: Alice
ALICE is 25 years old.
```

---

## Notes importantes
- L'application nettoie l'écran après chaque action pour une meilleure lisibilité.
- Les prédictions sont basées sur des données statistiques et peuvent ne pas être précises.
- Nécessite une connexion internet pourt fonctionner.
