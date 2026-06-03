import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Bank Marketing - Scoring", layout="wide")

st.title("Prédiction du Comportement Client - Scoring Bancaire")
st.markdown("Modèle IA pour prédire la probabilité de souscription à un dépôt à terme")

# ============================================================================
# 1. CHARGEMENT DES DONNEES
# ============================================================================
@st.cache_data
def load_data():
    df = pd.read_csv('bank_marketing_uci.csv')

    colonnes_francais = {
        'age': 'âge', 'job': 'emploi', 'marital': 'état_civil',
        'education': 'éducation', 'default': 'crédit_défaut', 'balance': 'solde',
        'housing': 'prêt_immobilier', 'loan': 'prêt_personnel',
        'contact': 'type_contact', 'day': 'jour', 'month': 'mois',
        'duration': 'durée', 'campaign': 'campagne',
        'pdays': 'jours_depuis_contact', 'previous': 'contacts_précédents',
        'poutcome': 'résultat_précédent', 'y': 'souscription'
    }
    df = df.rename(columns=colonnes_francais)
    return df

@st.cache_data
def prepare_data(df):
    df_enc = df.copy()

    cat_cols = ['emploi', 'éducation', 'état_civil', 'résultat_précédent',
                'prêt_immobilier', 'prêt_personnel', 'crédit_défaut']
    for col in cat_cols:
        df_enc[col] = LabelEncoder().fit_transform(df_enc[col])

    df_enc['souscription'] = (df_enc['souscription'] == 'yes').astype(int)

    mapping_contact = {'unknown': 1, 'telephone': 2, 'cellular': 3}
    mapping_mois = {
        'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6,
        'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10, 'nov': 11, 'dec': 12
    }

    df_enc['mois'] = df_enc['mois'].map(mapping_mois)
    df_enc['type_contact'] = df_enc['type_contact'].map(mapping_contact)

    X = df_enc.drop('souscription', axis=1)
    y = df_enc['souscription']

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    scaler = StandardScaler()
    X_train_sc = scaler.fit_transform(X_train)
    X_test_sc = scaler.transform(X_test)

    return X, X_train, X_test, y_train, y_test, X_train_sc, X_test_sc, scaler

df = load_data()
X, X_train, X_test, y_train, y_test, X_train_sc, X_test_sc, scaler = prepare_data(df)

# ============================================================================
# 2. ENTRAINEMENT DU MODELE (cache)
# ============================================================================
@st.cache_resource
def train_model():
    rf = RandomForestClassifier(n_estimators=100, class_weight='balanced',
                                 n_jobs=-1, random_state=42)
    rf.fit(X_train, y_train)

    gb = GradientBoostingClassifier(n_estimators=100, random_state=42)
    gb.fit(X_train, y_train)

    voting = VotingClassifier(
        estimators=[
            ('rf', rf),
            ('gb', gb),
            ('lr', LogisticRegression(max_iter=500, class_weight='balanced', random_state=42))
        ],
        voting='soft'
    )
    voting.fit(X_train, y_train)

    return rf, gb, voting

rf_model, gb_model, voting_model = train_model()

# ============================================================================
# 3. NAVIGATION
# ============================================================================
st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Selectionnez une page",
    ["Scoring Client", "Statistiques", "Performance du Modele"]
)

# ============================================================================
# PAGE 1 : SCORING CLIENT
# ============================================================================
if page == "Scoring Client":
    st.header("Scoring d'un Client")
    st.write("Remplissez les informations du client pour obtenir sa probabilite de souscription")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 18, 95, 42)
        emploi = st.selectbox("Emploi",
            ["admin", "technician", "management", "entrepreneur", "blue-collar",
             "services", "retired", "housemaid", "student", "unemployed",
             "self-employed", "unknown"])
        etat_civil = st.selectbox("Etat civil", ["married", "single", "divorced"])
        education = st.selectbox("Education", ["primary", "secondary", "tertiary", "unknown"])
        credit_defaut = st.selectbox("Credit en defaut", ["no", "yes"])

    with col2:
        solde = st.number_input("Solde moyen annuel (EUR)", -10000, 100000, 2500)
        pret_immobilier = st.selectbox("Pret immobilier", ["yes", "no"])
        pret_personnel = st.selectbox("Pret personnel", ["yes", "no"])
        type_contact = st.selectbox("Type de contact", ["cellular", "telephone", "unknown"])
        mois = st.selectbox("Mois du contact",
            ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])

    col3, col4 = st.columns(2)

    with col3:
        jour = st.slider("Jour du mois", 1, 31, 15)
        duree = st.slider("Duree du contact (secondes)", 0, 4918, 450)
        campagne = st.slider("Nombre de contacts (campagne actuelle)", 1, 63, 1)

    with col4:
        jours_depuis_contact = st.slider("Jours depuis dernier contact", -1, 871, -1)
        contacts_precedents = st.slider("Contacts precedents", 0, 275, 0)
        resultat_precedent = st.selectbox("Resultat precedent", ["unknown", "other", "failure", "success"])

    # Encodage des donnees
    mapping_emploi = {k: v for v, k in enumerate(
        ["admin", "technician", "management", "entrepreneur", "blue-collar",
         "services", "retired", "housemaid", "student", "unemployed", "self-employed", "unknown"]
    )}
    mapping_contact = {"unknown": 1, "telephone": 2, "cellular": 3}
    mapping_mois_dict = {
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
        "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12
    }

    # Encodage manuels pour les categoriques
    le_etat_civil = LabelEncoder().fit(["married", "single", "divorced"])
    le_education = LabelEncoder().fit(["primary", "secondary", "tertiary", "unknown"])
    le_credit = LabelEncoder().fit(["no", "yes"])
    le_pret_immo = LabelEncoder().fit(["no", "yes"])
    le_pret_perso = LabelEncoder().fit(["no", "yes"])
    le_resultat = LabelEncoder().fit(["unknown", "other", "failure", "success"])

    client_data = {
        'âge': age,
        'emploi': mapping_emploi[emploi],
        'état_civil': le_etat_civil.transform([etat_civil])[0],
        'éducation': le_education.transform([education])[0],
        'crédit_défaut': le_credit.transform([credit_defaut])[0],
        'solde': solde,
        'prêt_immobilier': le_pret_immo.transform([pret_immobilier])[0],
        'prêt_personnel': le_pret_perso.transform([pret_personnel])[0],
        'type_contact': mapping_contact[type_contact],
        'jour': jour,
        'mois': mapping_mois_dict[mois],
        'durée': duree,
        'campagne': campagne,
        'jours_depuis_contact': jours_depuis_contact,
        'contacts_précédents': contacts_precedents,
        'résultat_précédent': le_resultat.transform([resultat_precedent])[0],
        'type_contact_enc': mapping_contact[type_contact],
    }

    client_encoded = pd.DataFrame([client_data])
    client_encoded = client_encoded[X.columns]

    # Prediction
    if st.button("Calculer la Probabilite de Souscription"):
        proba_rf = rf_model.predict_proba(client_encoded)[0, 1]
        proba_gb = gb_model.predict_proba(client_encoded)[0, 1]
        proba_voting = voting_model.predict_proba(client_encoded)[0, 1]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("Random Forest", f"{proba_rf*100:.1f}%")
        with col2:
            st.metric("Gradient Boosting", f"{proba_gb*100:.1f}%")
        with col3:
            st.metric("Ensemble (Voting)", f"{proba_voting*100:.1f}%")

        avg_proba = (proba_rf + proba_gb + proba_voting) / 3

        st.success(f"Probabilite moyenne de souscription : {avg_proba*100:.1f}%")

        if avg_proba > 0.5:
            st.info("DECISION : Le client est un BON PROSPECT pour une campagne de marketing")
        else:
            st.warning("DECISION : Le client est un MAUVAIS PROSPECT - A moins de cibler")

# ============================================================================
# PAGE 2 : STATISTIQUES
# ============================================================================
elif page == "Statistiques":
    st.header("Analyse Exploratoire des Donnees")

    tab1, tab2, tab3 = st.tabs(["Distribution Cible", "Variables Numeriques", "Variables Categorielles"])

    with tab1:
        st.subheader("Distribution de la Variable Cible")

        counts = df['souscription'].value_counts()
        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots()
            colors = ['#2E75B6', '#C55A11']
            ax.pie(counts, labels=['Non souscrit', 'Souscrit'], autopct='%1.1f%%',
                   colors=colors, startangle=90)
            ax.set_title("Distribution de la Cible")
            st.pyplot(fig)

        with col2:
            st.metric("Total de clients", len(df))
            st.metric("Taux de souscription", f"{(df['souscription']=='yes').mean()*100:.1f}%")
            st.metric("Clients ayant souscrit", (df['souscription']=='yes').sum())

    with tab2:
        st.subheader("Distribution des Variables Numeriques")

        num_cols = ['âge', 'solde', 'durée', 'campagne', 'contacts_précédents']
        selected_col = st.selectbox("Selectionnez une variable", num_cols)

        fig, ax = plt.subplots()
        ax.hist(df[selected_col], bins=30, color='#2E75B6', edgecolor='white')
        ax.set_title(f"Distribution de {selected_col}")
        ax.set_xlabel(selected_col)
        ax.set_ylabel("Frequence")
        st.pyplot(fig)

    with tab3:
        st.subheader("Taux de Souscription par Variable Categorielle")

        cat_cols = ['emploi', 'éducation', 'état_civil', 'prêt_immobilier', 'prêt_personnel']
        selected_cat = st.selectbox("Selectionnez une variable", cat_cols)

        rate = df.groupby(selected_cat)['souscription'].apply(
            lambda x: (x=='yes').mean() * 100
        ).sort_values(ascending=False)

        fig, ax = plt.subplots(figsize=(10, 5))
        ax.bar(range(len(rate)), rate.values, color='#2E75B6', edgecolor='white')
        ax.set_xticks(range(len(rate)))
        ax.set_xticklabels(rate.index, rotation=45, ha='right')
        ax.set_ylabel("Taux de souscription (%)")
        ax.set_title(f"Taux par {selected_cat}")
        st.pyplot(fig)

# ============================================================================
# PAGE 3 : PERFORMANCE DU MODELE
# ============================================================================
elif page == "Performance du Modele":
    st.header("Evaluation des Modeles")

    from sklearn.metrics import roc_auc_score, accuracy_score, f1_score, roc_curve, confusion_matrix

    # Predictions
    y_pred_rf = rf_model.predict(X_test)
    y_prob_rf = rf_model.predict_proba(X_test)[:, 1]

    y_pred_gb = gb_model.predict(X_test)
    y_prob_gb = gb_model.predict_proba(X_test)[:, 1]

    y_pred_voting = voting_model.predict(X_test)
    y_prob_voting = voting_model.predict_proba(X_test)[:, 1]

    tab1, tab2, tab3 = st.tabs(["Metriques", "Courbes ROC", "Matrices de Confusion"])

    with tab1:
        col1, col2, col3 = st.columns(3)

        metrics_rf = {
            "AUC-ROC": roc_auc_score(y_test, y_prob_rf),
            "Accuracy": accuracy_score(y_test, y_pred_rf),
            "F1-Score": f1_score(y_test, y_pred_rf)
        }

        metrics_gb = {
            "AUC-ROC": roc_auc_score(y_test, y_prob_gb),
            "Accuracy": accuracy_score(y_test, y_pred_gb),
            "F1-Score": f1_score(y_test, y_pred_gb)
        }

        metrics_voting = {
            "AUC-ROC": roc_auc_score(y_test, y_prob_voting),
            "Accuracy": accuracy_score(y_test, y_pred_voting),
            "F1-Score": f1_score(y_test, y_pred_voting)
        }

        with col1:
            st.subheader("Random Forest")
            for metric, value in metrics_rf.items():
                st.metric(metric, f"{value:.4f}")

        with col2:
            st.subheader("Gradient Boosting")
            for metric, value in metrics_gb.items():
                st.metric(metric, f"{value:.4f}")

        with col3:
            st.subheader("Voting Ensemble")
            for metric, value in metrics_voting.items():
                st.metric(metric, f"{value:.4f}")

    with tab2:
        st.subheader("Courbes ROC")

        fig, ax = plt.subplots()

        fpr_rf, tpr_rf, _ = roc_curve(y_test, y_prob_rf)
        ax.plot(fpr_rf, tpr_rf, linewidth=2, label=f"RF (AUC={metrics_rf['AUC-ROC']:.4f})")

        fpr_gb, tpr_gb, _ = roc_curve(y_test, y_prob_gb)
        ax.plot(fpr_gb, tpr_gb, linewidth=2, label=f"GB (AUC={metrics_gb['AUC-ROC']:.4f})")

        fpr_voting, tpr_voting, _ = roc_curve(y_test, y_prob_voting)
        ax.plot(fpr_voting, tpr_voting, linewidth=2, label=f"Voting (AUC={metrics_voting['AUC-ROC']:.4f})")

        ax.plot([0, 1], [0, 1], 'k--', linewidth=1, alpha=0.5, label='Aleatoire')

        ax.set_xlabel("Taux de Faux Positifs")
        ax.set_ylabel("Taux de Vrais Positifs")
        ax.set_title("Courbes ROC")
        ax.legend()
        ax.grid(True, alpha=0.3)
        st.pyplot(fig)

    with tab3:
        st.subheader("Matrices de Confusion")

        col1, col2, col3 = st.columns(3)

        with col1:
            cm_rf = confusion_matrix(y_test, y_pred_rf)
            fig, ax = plt.subplots()
            sns.heatmap(cm_rf, annot=True, fmt='d', cmap='Blues', ax=ax,
                       xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
            ax.set_title("Random Forest")
            st.pyplot(fig)

        with col2:
            cm_gb = confusion_matrix(y_test, y_pred_gb)
            fig, ax = plt.subplots()
            sns.heatmap(cm_gb, annot=True, fmt='d', cmap='Blues', ax=ax,
                       xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
            ax.set_title("Gradient Boosting")
            st.pyplot(fig)

        with col3:
            cm_voting = confusion_matrix(y_test, y_pred_voting)
            fig, ax = plt.subplots()
            sns.heatmap(cm_voting, annot=True, fmt='d', cmap='Blues', ax=ax,
                       xticklabels=['No', 'Yes'], yticklabels=['No', 'Yes'])
            ax.set_title("Voting Ensemble")
            st.pyplot(fig)

st.sidebar.markdown("---")
st.sidebar.info("Prédiction du Comportement Client - Scoring Bancaire\nANI-IA 4")
