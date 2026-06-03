import pandas as pd

# Charger le dataset
df = pd.read_csv('bank_marketing_uci.csv')

# Dictionnaire de renommage (anglais → français)
colonnes_francais = {
    'age': 'âge',
    'job': 'emploi',
    'marital': 'état_civil',
    'education': 'éducation',
    'default': 'crédit_défaut',
    'balance': 'solde',
    'housing': 'prêt_immobilier',
    'loan': 'prêt_personnel',
    'contact': 'type_contact',
    'day': 'jour',
    'month': 'mois',
    'duration': 'durée',
    'campaign': 'campagne',
    'pdays': 'jours_depuis_contact',
    'previous': 'contacts_précédents',
    'poutcome': 'résultat_précédent',
    'y': 'souscription'
}

# Renommer les colonnes
df = df.rename(columns=colonnes_francais)

# Sauvegarder le fichier modifié
df.to_csv('bank_marketing_francais.csv', index=False)

print("✅ Fichier renommé avec succès!")
print("\nNouvelles colonnes:")
print(df.columns.tolist())
print("\nAperçu des premières lignes:")
print(df.head())
