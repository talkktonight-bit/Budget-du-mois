import streamlit as st
import datetime

# Configuration de la page pour un look "Appli"
st.set_page_config(page_title="Mon Assistant Budget", page_icon="💰", layout="centered")

st.title("💰 Mon Assistant Budget")

# --- ENTRÉES ---
# On regroupe les entrées dans un bloc propre
with st.expander("📝 Saisie des données", expanded=True):
    salaire = st.number_input("1. Votre salaire net (€)", min_value=0.0, step=10.0, value=0.0)
    solde_compte = st.number_input("2. Votre solde actuel (€)", step=10.0, value=0.0)
    date_paie = st.date_input("3. Date de la prochaine paie")

# --- CALCULS ET AFFICHAGE STYLE "APP" ---
if salaire > 0:
    # Logique de calcul
    budget_vie = salaire * 0.5
    budget_epargne = salaire * 0.2
    reste_a_vivre_salaire = salaire * 0.3
    nouveau_solde_disponible = reste_a_vivre_salaire + solde_compte
    
    jours_restants = (date_paie - datetime.date.today()).days
    nb_jours = jours_restants if jours_restants > 0 else 1
    budget_quotidien = nouveau_solde_disponible / nb_jours

    st.divider()

    # Affichage en colonnes (le plus beau sur mobile)
    col1, col2, col3 = st.columns(3)
    col1.metric("Coût Vie", f"{budget_vie:.0f}€")
    col2.metric("Épargne", f"{budget_epargne:.0f}€")
    col3.metric("Reste", f"{reste_a_vivre_salaire:.0f}€")

    st.write("---")

    # Résultats principaux mis en avant
    st.subheader("Résultats de gestion")
    
    # Ligne 4 et 5 avec un style visuel fort
    st.info(f"*Total disponible (Ligne 4) :* {nouveau_solde_disponible:.2f} €")
    
    label_jours = f"Budget quotidien ({nb_jours} jours restants)" if jours_restants > 0 else "Budget quotidien (Paie aujourd'hui)"
    st.success(f"*{label_jours} :* {budget_quotidien:.2f} € / jour")

    # --- AMORTISSEMENT ---
    st.write("---")
    st.subheader("🛒 Simulateur d'achat")
    somme_amortir = st.number_input("Combien veux-tu amortir ? (€)", min_value=0
