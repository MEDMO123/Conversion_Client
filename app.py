import streamlit as st
import pandas as pd
import pickle
import os



BASE_DIR = os.path.dirname(__file__)
MODEL_PATH = os.path.join(BASE_DIR, ".\modele_conversion.pkl")

st.write("📁 Chemin absolu du modèle :", MODEL_PATH)
st.write("📦 Fichier existe :", os.path.exists(MODEL_PATH))

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"❌ Erreur de chargement du modèle : {e}")
    st.stop()

# 📂 Interface Streamlit
st.title("🔮 Modele de Prédiction des conversions e-commerce")
st.write("Ce modèle prédit la probabilité qu'un utilisateur achète un produit sur un site e-commerce.")
st.write("📊 Veuillez téléchargez un fichier CSV contenant les données des utilisateurs pour effectuer des prédictions.")

if st.button("Details sur le modèle et les données"):
    with open("Readme.txt", "r", encoding="utf-8") as f:
        details = f.read()
    st.text_area("Détails du modèle", details, height=300)

    if st.button("❌ Fermer"):
        st.close()
  

uploaded_file = st.file_uploader("📂 Importer un fichier CSV", type=["csv"])
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Aperçu des données :", df.head())

    # Lancer la Prédiction
    if st.button("🚀 Lancer la prédiction"):
        X = df.drop("Revenue", axis=1)
        X=pd.DataFrame(X)
        predictions = model.predict(X)
        df["Prediction"] = predictions

        st.success("✅ Prédiction terminée ! Voici les résultats :")
        st.write(df)

   

    # 📥 Télécharger les résultats
    if st.button("📥 Télécharger les résultats"):
        df.to_csv("resultats_predictions.csv", index=False)
        st.success("✅ Fichier téléchargé : resultats_predictions.csv")

    #Réinitialiser l'application
    if st.button("❌ Réinitialiser"):
        st.rerun()

