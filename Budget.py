import streamlit as st
import datetime

st.title("💰 Mon Assistant Budget")

# --- ENTRÉES ---
# On garde tes champs exactement comme sur la photo
salaire = st.number_input("1. Salaire net (€)", min_value=0.0, step=10.0, value=2000.0)
solde_compte = st.number_input("2. Solde actuel du compte (€)", step=10.0, value=200.0)
date_paie = st.date_input("3. Date de la prochaine paie", value=datetime.date(2026, 5, 28))

# On utilise un petit bouton comme sur ta photo
# Note : Sur Streamlit, pour éviter le reset du simulateur, on calcule automatiquement
# mais on garde la mise en page aérée que tu aimes.

st.write("") # Espace
if st.button("Calculer mon budget"):
    st.session_state.calcule = True

# --- CALCULS ET RÉSULTATS ---
# Cette partie permet de garder l'affichage même si on touche au simulateur après
budget_vie = salaire * 0.5
budget_epargne = salaire * 0.2
reste_a_vivre_salaire = salaire * 0.3
total_disponible = reste_a_vivre_salaire + solde_compte

jours_restants = (date_paie - datetime.date.today()).days
nb_jours = jours_restants if jours_restants > 0 else 1
budget_quotidien = total_disponible / nb_jours

st.divider()
st.subheader("Résultats")

# Organisation en deux colonnes comme sur ta photo
col1, col2 = st.columns(2)

with col1:
    st.write(f"Coût de vie (50%) : {budget_vie:.2f} €")
    st.write(f"Épargne (20%) : {budget_epargne:.2f} €")
    st.write(f"Reste à vivre (30%) : {reste_a_vivre_salaire:.2f} €")

with col2:
    st.metric("Total Disponible", f"{total_disponible:.2f} €")
    st.metric("Budget Quotidien", f"{budget_quotidien:.2f} €/j")

# --- SIMULATEUR D'ACHAT ---
st.divider()
st.subheader("Simulateur d'achat")
montant_amortir = st.number_input("Montant de l'achat à amortir (€)", min_value=0.0, value=0.0, step=10.0)

if montant_amortir > 0:
    if budget_quotidien > 0:
        jours = montant_amortir / budget_quotidien
        st.info(f"Il vous faudra *{jours:.1f} jours* de budget quotidien pour amortir cet achat.")
    else:
        st.error("Budget quotidien nul ou négatif.")
