import streamlit as st
import pickle
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


def load_model():
    try:
        with open("spam_classifier.pkl", "rb") as model_file:
            return pickle.load(model_file)
    except FileNotFoundError:
        st.error("Error: No se encontró el modelo. Ejecuta 'train_model.py' primero.")
        return None


def preprocess_email(from_field, to_field, subject, body):
    email_text = f"From: {from_field} To: {to_field} Subject: {subject} Body: {body}"

    stop_words = stopwords.words("english")
    tfidf = TfidfVectorizer(
        stop_words=stop_words, token_pattern=r"(?u)\b([a-zA-Z]{4,12})\b"
    )

    model, tfidf = load_model()
    if model is not None:
        email_vectorized = tfidf.transform([email_text])
        return email_vectorized
    return None


def classify_email(from_field, to_field, subject, body):
    email_vectorized = preprocess_email(from_field, to_field, subject, body)
    if email_vectorized is not None:
        model, tfidf = load_model()
        if model:
            prediction = model.predict(email_vectorized)
            if prediction[0] == 1:
                return "SPAM ❌"
            else:
                return "NO SPAM ✅"
    return "❌ Error en el procesamiento del correo."


def main():
    st.title("Clasificador de Correos Spam")

    from_field = st.text_input("From", "example@example.com")
    to_field = st.text_input("To", "recipient@example.com")
    subject = st.text_input("Subject", "Subject of the email")
    body = st.text_area("Body", "Body of the email.")

    if st.button("Clasificar"):
        if from_field and to_field and subject and body:
            result = classify_email(from_field, to_field, subject, body)
            st.write(f"🔍 El correo es: {result}")
        else:
            st.error("❌ Por favor, completa todos los campos del correo.")


if __name__ == "__main__":
    main()
