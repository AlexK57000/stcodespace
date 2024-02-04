import streamlit as st
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_absolute_error

# Création de deux vecteurs de dimension 6
vecteur_true = [1.5, 2.0, 3.2, 4.8, 5.5, 6.2]
vecteur_pred = [1.2, 2.5, 3.0, 4.5, 5.8, 6.0]

# Calcul de l'erreur absolue moyenne
mae = mean_absolute_error(vecteur_true, vecteur_pred)

# Affichage du résultat
st.write(f"Vecteur True: {vecteur_true}")
st.write(f"Vecteur Prédit: {vecteur_pred}")
st.write(f"Mean Absolute Error: {mae}")


#st.title("Hello World, je m'appelle A")

st.code("def : class image", language='javascript')

with st.sidebar:
    st.button("test")
    st.write("test d'écriture ici")
