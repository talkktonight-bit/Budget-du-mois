import streamlit as st
import datetime

st.title("💰 Mon Assistant Budget")

# --- ENTRÉES ---
# Valeurs remises à 0 pour un lancement propre
salaire = st.number_input("1. Salaire net (€)", min_value=0.0, step=10.0, value=0.0)
solde_compte = st.number_input("2. Solde actuel du compte (€)", step=10.0, value=0.0)

# Date réglée sur aujourd'hui par défaut
date_paie = st.date_input("3. Date de la prochaine paie", value=datetime.date.today())

# --- CALCULS ---
# On calcule tout en temps réel dès que le salaire est > 0
budget_vie = salaire * 0.5
budget_epargne = salaire * 0.2
reste_a_vivre_salaire = salaire * 0.3
total_disponible = reste_a_vivre_salaire + solde_compte

jours_restants = (date_paie - datetime.date.today()).days
nb_jours = jours_restants if jours_restants > 0 else 1
budget_quotidien = total_disponible / nb_jours

# --- AFFICHAGE (Ton interface validée) ---
st.divider()
st.subheader("Résultats")

col1, col2 = st.columns(2)

if salaire > 0:
    with col1:
        st.write(f"Coût de vie (50%) : {budget_vie:.2f} €")
        st.write(f"Épargne (20%) : {budget_epargne:.2f} €")
        st.write(f"Reste à vivre (30%) : {reste_a_vivre_salaire:.2f} €")

    with col2:
        st.metric("Total Disponible", f"{total_disponible:.2f} €")
        st.metric("Budget Quotidien", f"{budget_quotidien:.2f} €/j")
else:
    st.info("Entrez un montant de salaire pour afficher les résultats.")

# --- SIMULATEUR D'ACHAT ---
st.divider()
st.subheader("Simulateur d'achat")
montant_amortir = st.number_input("Montant de l'achat à amortir (€)", min_value=0.0, value=0.0, step=10.0)

if montant_amortir > 0:
    if budget_quotidien > 0:
        jours = montant_amortir / budget_quotidien
        st.info(f"Il vous faudra *{jours:.1f} jours* de budget quotidien pour amortir cet achat.")
    else:
        st.error("Le budget quotidien doit être supérieur à 0 pour calculer l'amortissement.")
