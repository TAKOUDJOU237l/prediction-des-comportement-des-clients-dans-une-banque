# Documentation du Dataset Bank Marketing 🏦
**Source**: https://archive.ics.uci.edu/dataset/222/bank+marketing

---

## 📊 Description Générale
Ce dataset contient des données relatives à des campagnes de marketing direct d'une institution bancaire portugaise. L'objectif est de prédire si un client va souscrire à un dépôt à terme (term deposit).

**Nombre de lignes**: 45,211 enregistrements  
**Nombre de colonnes**: 17 variables

---

## 📋 Détail de Chaque Colonne

### **1. âge (age)** - TYPE: Numérique
**Description**: L'âge du client en années.  
**Valeurs**: Nombres entiers positifs (ex: 25, 46, 58, 65...)  
**Importance**: Permet d'analyser le comportement des clients selon leur tranche d'âge.  
**Exemple**: Un client de 46 ans

---

### **2. emploi (job)** - TYPE: Catégorique
**Description**: Le type d'emploi/profession du client.  
**Catégories possibles**:
- "admin." → Administration
- "technician" → Technicien
- "management" → Gestion/Cadre
- "entrepreneur" → Entrepreneur
- "blue-collar" → Ouvrier
- "services" → Services
- "retired" → Retraité
- "housemaid" → Femme de ménage
- "student" → Étudiant
- "unemployed" → Sans emploi
- "self-employed" → Travailleur indépendant
- "unknown" → Inconnu

**Importance**: La profession influence souvent les décisions financières.  
**Exemple**: "management", "admin.", "services"

---

### **3. état_civil (marital)** - TYPE: Catégorique
**Description**: L'état matrimonial du client.  
**Catégories possibles**:
- "married" → Marié(e)
- "single" → Célibataire
- "divorced" → Divorcé(e) ou veuf/veuve

**Note**: La catégorie "divorced" inclut aussi les personnes veuves.  
**Importance**: L'état civil peut affecter la capacité d'épargne et les besoins financiers.  
**Exemple**: "married", "single", "divorced"

---

### **4. éducation (education)** - TYPE: Catégorique
**Description**: Le niveau d'éducation/formation du client.  
**Catégories possibles**:
- "primary" → Éducation primaire
- "secondary" → Éducation secondaire
- "tertiary" → Éducation tertiaire (université/études supérieures)
- "unknown" → Inconnu

**Importance**: Le niveau d'éducation peut influencer la compréhension des produits financiers et la propension à investir.  
**Exemple**: "tertiary", "secondary", "primary"

---

### **5. crédit_défaut (default)** - TYPE: Binaire (Oui/Non)
**Description**: Le client a-t-il un crédit en défaut (impayé) ?  
**Valeurs**:
- "yes" → Oui, le client a un crédit en défaut
- "no" → Non, le client n'a pas de crédit en défaut

**Importance**: C'est un indicateur majeur de risque de crédit et de fiabilité financière.  
**Exemple**: "no", "yes"

---

### **6. solde (balance)** - TYPE: Numérique
**Description**: Le solde moyen annuel du client, en euros (€).  
**Valeurs**: Nombres entiers (positifs ou négatifs)  
**Plage observée**: Peut être négatif (découvert) ou positif (économies)  
**Importance**: Reflète la santé financière et la capacité d'épargne du client.  
**Exemple**: 2143 €, 825 €, -2496 € (découvert)

---

### **7. prêt_immobilier (housing)** - TYPE: Binaire (Oui/Non)
**Description**: Le client a-t-il un prêt immobilier (hypothèque) ?  
**Valeurs**:
- "yes" → Oui, le client a un prêt immobilier
- "no" → Non, le client n'a pas de prêt immobilier

**Importance**: Indique un engagement financier important et la capacité d'endettement.  
**Exemple**: "yes", "no"

---

### **8. prêt_personnel (loan)** - TYPE: Binaire (Oui/Non)
**Description**: Le client a-t-il un prêt personnel ?  
**Valeurs**:
- "yes" → Oui, le client a un prêt personnel
- "no" → Non, le client n'a pas de prêt personnel

**Importance**: Reflète le niveau d'endettement global du client.  
**Exemple**: "no", "yes"

---

### **9. type_contact (contact)** - TYPE: Catégorique
**Description**: Le type de communication utilisé pour contacter le client.  
**Catégories possibles**:
- "cellular" → Par téléphone mobile
- "telephone" → Par téléphone fixe
- "unknown" → Inconnu

**Importance**: Peut influencer la réceptivité du client et le taux de réponse.  
**Exemple**: "cellular", "unknown"

---

### **10. jour (day)** - TYPE: Numérique
**Description**: Le jour du mois du dernier contact avec le client (dans la campagne actuelle).  
**Valeurs**: Nombres entre 1 et 31  
**Importance**: Peut révéler des tendances saisonnières ou des patterns de contact.  
**Exemple**: 5 (5e jour du mois), 15, 28

---

### **11. mois (month)** - TYPE: Catégorique
**Description**: Le mois du dernier contact avec le client.  
**Catégories possibles**:
- "jan" → Janvier
- "feb" → Février
- "mar" → Mars
- "apr" → Avril
- "may" → Mai
- "jun" → Juin
- "jul" → Juillet
- "aug" → Août
- "sep" → Septembre
- "oct" → Octobre
- "nov" → Novembre
- "dec" → Décembre

**Importance**: Permet d'identifier les périodes où les clients sont plus réceptifs.  
**Exemple**: "may" (mai), "jan" (janvier)

---

### **12. durée (duration)** - TYPE: Numérique
**Description**: La durée du dernier contact avec le client, **en secondes**.  
**Valeurs**: Nombres entiers (ex: 261 secondes ≈ 4 minutes)  
**Note**: Cette variable ne peut être connue que APRÈS l'appel. Elle n'est pas utile pour prédire, mais elle fortement corrélée au résultat.  
**Importance**: Un appel plus long suggère un intérêt plus grand du client.  
**Exemple**: 261 secondes, 150 secondes

---

### **13. campagne (campaign)** - TYPE: Numérique
**Description**: Le nombre de contacts effectués **pendant cette campagne** pour ce client (incluant le dernier contact).  
**Valeurs**: Nombres entiers positifs (1, 2, 3...)  
**Importance**: Indique l'intensité de la campagne marketing pour ce client.  
**Exemple**: 1 (premier contact), 3 (3 contacts pendant la campagne)

---

### **14. jours_depuis_contact (pdays)** - TYPE: Numérique
**Description**: Le nombre de jours qui se sont écoulés **depuis le dernier contact d'une campagne précédente**.  
**Valeurs spéciales**:
- **-1** → Le client n'avait JAMAIS été contacté dans une campagne précédente
- **Nombre positif** → Nombre de jours depuis le dernier contact (ex: 45 jours)

**Importance**: Montre si le client a déjà été approché et quand.  
**Exemple**: -1 (jamais contacté), 30 (30 jours depuis le dernier contact)

---

### **15. contacts_précédents (previous)** - TYPE: Numérique
**Description**: Le nombre de contacts effectués **avant cette campagne** pour ce client.  
**Valeurs**: Nombres entiers (0, 1, 2, 3...)  
**Note**: Si = 0, alors le client n'avait jamais été contacté avant.  
**Importance**: Indique la familiarité du client avec la banque et ses campagnes.  
**Exemple**: 0 (nouveau client), 5 (5 contacts précédents)

---

### **16. résultat_précédent (poutcome)** - TYPE: Catégorique
**Description**: Le résultat de la **dernière campagne précédente** pour ce client.  
**Catégories possibles**:
- "unknown" → Le résultat est inconnu (ou client jamais contacté)
- "other" → Autre résultat
- "failure" → Échec (client n'a pas souscrit)
- "success" → Succès (client a souscrit)

**Importance**: Si le client a déjà souscrit par le passé, il est plus susceptible de le refaire.  
**Exemple**: "unknown", "failure", "success"

---

### **17. souscription (y)** - TYPE: Binaire (Oui/Non) ⭐ VARIABLE CIBLE
**Description**: **Le client a-t-il souscrit à un dépôt à terme ?** ← **C'est ce qu'on veut prédire !**  
**Valeurs**:
- "yes" → Oui, le client a souscrit à un dépôt à terme
- "no" → Non, le client n'a pas souscrit

**Importance**: **C'est la variable à prédire (TARGET)** dans notre modèle de machine learning.  
**Répartition typique**: Environ 88-90% de "no" et 10-12% de "yes" (classe fortement déséquilibrée).  
**Exemple**: "no" (n'a pas souscrit), "yes" (a souscrit)

---

## 🎯 Résumé des Types de Variables

| Type | Colonnes | Nombre |
|------|----------|--------|
| **Numériques** | âge, solde, jour, durée, campagne, jours_depuis_contact, contacts_précédents | 7 |
| **Catégoriques** | emploi, état_civil, éducation, type_contact, mois, résultat_précédent | 6 |
| **Binaires** | crédit_défaut, prêt_immobilier, prêt_personnel, souscription | 4 |

---

## 💡 Utilisation pour le Scoring Bancaire

Ce dataset est **idéal pour créer un modèle de prédiction** qui aide la banque à :
1. **Identifier** quels clients sont les plus susceptibles de souscrire
2. **Optimiser** les campagnes marketing (cibler les bons clients)
3. **Réduire** les coûts en évitant de contacter les clients peu intéressés
4. **Augmenter** le ROI (retour sur investissement) des campagnes

---

## 📌 Notes Importantes

- **Données réelles et validées** : Proviennent de l'UCI Machine Learning Repository
- **Pas de données sensibles** : Aucune information personnelle identifiable (pas de noms, adresses, numéros de compte)
- **Prête pour l'analyse** : Toutes les données sont correctement structurées et nettoyées
- **Classe déséquilibrée** : La majorité des clients ne souscrivent pas (important pour la modélisation)

---

**Créé pour le projet Scoring Bancaire AIR-IA4**
