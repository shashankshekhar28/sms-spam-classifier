import streamlit as st
import string
import pickle
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer

# Download NLTK resources (only first time)
nltk.download('punkt')
nltk.download('stopwords')

ps = PorterStemmer()

# Load vectorizer and model
tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('📩 SMS Spam Classifier')
input_msg = st.text_input('Enter your message:')

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = [i for i in text if i.isalnum()]
    y = [i for i in y if i not in stopwords.words('english') and i not in string.punctuation]
    y = [ps.stem(i) for i in y]

    return " ".join(y)

if st.button("Predict"):
    # Preprocess
    transformed_sms = transform_text(input_msg)
    # Vectorize
    vector_input = tfidf.transform([transformed_sms])
    # Predict
    result = model.predict(vector_input)[0]
    # Display
    if result == 1:
        st.header('🚨 Spam!')
    else:
        st.header('✅ Not Spam')


