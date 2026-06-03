# Scoring Bancaire — Projet

Petit projet de prédiction (bank marketing) pour scorer la propension
des clients à souscrire à un dépôt à terme.

## Contenu du dépôt

- `app.py` : script principal (si présent, point d'entrée). 
- `bank_marketing_uci.csv`, `bank_marketing_francais.csv` : jeux de données.
- `rename_columns.py` : utilitaire de renommage de colonnes.
- `requirements.txt` : dépendances Python.
- `Scoring_Bancaire_ANI-IA4.ipynb` et `Scoring_Bancaire_ANI-IA4_V2.ipynb` : notebooks d'analyse et modèle.
- `DOCUMENTATION_DATASET.md` : documentation détaillée du dataset.

## Installation (Windows)

1. Créer un environnement virtuel :

```powershell
python -m venv venv
```

2. Activer l'environnement (PowerShell) :

```powershell
& .\venv\Scripts\Activate.ps1
```

3. Installer les dépendances :

```powershell
pip install -r requirements.txt
```

## Exécution

- Pour lancer le script principal (si applicable) :

```powershell
python app.py
```

- Pour ouvrir les notebooks :

```powershell
jupyter notebook
```

## Données

Le dataset principal est documenté dans `DOCUMENTATION_DATASET.md`.
Utilisez les fichiers CSV fournis pour l'entraînement et l'exploration.

## Git / .gitignore

Le dossier de l'environnement virtuel `venv/` est ignoré via `.gitignore`.
Si `venv` est déjà suivi par Git, exécutez :

```bash
git rm -r --cached venv
git commit -m "Stop tracking venv"
```

## Notes
- Le projet est en français.
- Pour toute question ou ajout (tests, CI, docker), dites-moi ce que vous voulez que j'ajoute.
