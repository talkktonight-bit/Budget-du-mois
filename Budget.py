import streamlit as st
import datetime

st.title("💰 Mon Assistant Budget")

# --- ENTRÉES ---
salaire = st.number_input("1. Salaire net (€)", min_value=0.0, step=100.0)
solde_compte = st.number_input("2. Solde actuel du compte (€)", step=10.0)
date_paie = st.date_input("3. Date de la prochaine paie")

if st.button("Calculer mon budget"):
    # --- CALCULS ---
    budget_vie = salaire * 0.5
    budget_epargne = salaire * 0.2
    reste_a_vivre_salaire = salaire * 0.3
    nouveau_solde_disponible = reste_a_vivre_salaire + solde_compte
    
    jours_restants = (date_paie - datetime.date.today()).days
    diviseur = jours_restants if jours_restants > 0 else 1
    budget_quotidien = nouveau_solde_disponible / diviseur

    # --- AFFICHAGE ---
    st.divider()
    st.subheader("Résultats")
    col1, col2 = st.columns(2)
    
    with col1:
        st.write(f"*Coût de vie (50%) :* {budget_vie:.2f} €")
        st.write(f"*Épargne (20%) :* {budget_epargne:.2f} €")
        st.write(f"*Reste à vivre (30%) :* {reste_a_vivre_salaire:.2f} €")
    
    with col2:
        st.metric("Total Disponible", f"{nouveau_solde_disponible:.2f} €")
        st.metric("Budget Quotidien", f"{budget_quotidien:.2f} €/j")

    # --- AMORTISSEMENT ---
    st.divider()
    st.subheader("Simulateur d'achat")
    somme = st.number_input("Montant de l'achat à amortir (€)", min_value=0.0)
    if somme > 0 and budget_quotidien > 0:
        jours = somme / budget_quotidien
        st.info(f"Il vous faudra *{jours:.1f} jours* de budget quotidien pour amortir cet achat.")
