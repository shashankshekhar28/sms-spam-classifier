# 📩 SMS Spam Classifier

A **Machine Learning–based SMS Spam Classification system** that predicts whether a message is **Spam** or **Not Spam (Ham)** using **Natural Language Processing (NLP)**.  
The project also includes a **web application (`app.py`)** for real-time predictions.

---

## 🚀 Project Overview

This project applies NLP techniques and machine learning algorithms to classify SMS messages.  
Users can enter an SMS message through a web interface and instantly receive a prediction.

---

## 🧠 Key Concepts Used

- Natural Language Processing (NLP)
- Text Cleaning & Preprocessing
- Tokenization & Stopword Removal
- Bag of Words / TF-IDF
- Machine Learning Classification
- Model Serialization using Pickle
- Web Application Development

---

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- NLTK
- Streamlit / Flask
- Pickle

---

## 📂 Project Structure

├── app.py
├── sms spam classifier.ipynb
├── model.pkl
├── vectorizer.pkl
├── dataset.csv
├── requirements.txt
└── README.md

---

## ⚙️ Project Workflow

1. Load SMS dataset  
2. Clean and preprocess text  
3. Convert text into numerical features  
4. Train machine learning model  
5. Save trained model and vectorizer  
6. Predict spam or ham using the web app  

---

## 📊 Machine Learning Models Used

- Naive Bayes  
- Logistic Regression  

---

## ▶️ How to Run the Project Locally

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name


---

### 2️⃣ Install Dependencies

pip install -r requirements.txt


---

### 3️⃣ Run the Web Application

#### If using Streamlit
streamlit run app.py


## 🧪 Example Prediction

**Input SMS**
You have won ₹10,00,000! Click the link to claim now.



**Output**
Spam



---

## 📌 Applications

- SMS spam filtering
- Email spam detection
- Fraud and scam message detection
- Chat moderation systems

---

## 📈 Future Enhancements

- Deploy on Streamlit Cloud or Render
- Improve accuracy using deep learning models
- Multi-language spam detection
- Store prediction history

---

## 🧑‍💻 Author

**Shashank Shekhar**  
Machine Learning & Data Science Enthusiast

---

⭐ If you like this project, please **star the repository**!
