import streamlit as st
import datetime

st.set_page_config(page_title="Mon Assistant Budget", page_icon="💰")

st.title("💰 Mon Assistant Budget")

# --- ENTRÉES ---
with st.container():
    salaire = st.number_input("1. Salaire net (€)", min_value=0.0, step=100.0, value=0.0)
    solde_compte = st.number_input("2. Solde actuel du compte (€)", step=10.0, value=0.0)
    date_paie = st.date_input("3. Date de la prochaine paie")

# --- CALCULS AUTOMATIQUES ---
# On calcule dès que les valeurs changent, sans bouton "Calculer", pour éviter le bug du reset
if salaire > 0:
    budget_vie = salaire * 0.5
    budget_epargne = salaire * 0.2
    reste_a_vivre_salaire = salaire * 0.3
    nouveau_solde_disponible = reste_a_vivre_salaire + solde_compte
    
    jours_restants = (date_paie - datetime.date.today()).days
    diviseur = jours_restants if jours_restants > 0 else 1
    budget_quotidien = nouveau_solde_disponible / diviseur

    # --- AFFICHAGE DES RÉSULTATS ---
    st.divider()
    st.subheader("📊 Tes Budgets")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Coût Vie (50%)", f"{budget_vie:.2f} €")
    c2.metric("Épargne (20%)", f"{budget_epargne:.2f} €")
    c3.metric("Reste à vivre", f"{reste_a_vivre_salaire:.2f} €")
    
    st.info(f"*Total disponible (Ligne 4) :* {nouveau_solde_disponible:.2f} €")
    st.success(f"*Budget quotidien (Ligne 5) :* {budget_quotidien:.2f} € / jour")

    # --- AMORTISSEMENT ---
    st.divider()
    st.subheader("🛒 Simulateur d'achat")
    somme_achat = st.number_input("Montant de l'achat à amortir (€)", min_value=0.0, value=0.0)
    
    if somme_achat > 0:
        if budget_quotidien > 0:
            jours = somme_achat / budget_quotidien
            st.warning(f"🕒 Il te faudra *{jours:.1f} jours* de ton budget quotidien pour amortir cet achat.")
        else:
            st.error("Budget quotidien trop faible pour calculer l'amortissement.")
else:
    st.info("Entre ton salaire pour voir apparaître tes budgets.")
