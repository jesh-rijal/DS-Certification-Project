# 💳 Online Fraud Detection Web App

## 📌 Project Overview

This project focuses on detecting fraudulent online transactions using machine learning techniques. A **Random Forest Classifier** was selected as the final model due to its superior performance in identifying fraudulent transactions while maintaining a strong balance between precision and F1-score.

The system is deployed as an **interactive Streamlit web application**, allowing users to input transaction details and receive real-time fraud predictions along with probability scores.

---

## 🎯 Objective

* Detect fraudulent transactions with high accuracy
* Maximize **recall** to minimize missed fraud cases
* Maintain a balance between **precision and F1-score**
* Provide a user-friendly web interface for predictions

---

## 📊 Dataset

* **Name:** Online Fraud Detection Dataset (`onlinefraud.csv`)
* **Source:** Kaggle
* **Type:** Transactional financial dataset

### Key Features:

* `amount` – Transaction amount
* `oldbalanceOrg` – Sender’s initial balance
* `newbalanceOrig` – Sender’s balance after transaction
* `oldbalanceDest` – Receiver’s initial balance
* `newbalanceDest` – Receiver’s balance after transaction
* `type` – Transaction type (PAYMENT, TRANSFER, CASH_OUT, DEBIT)
* `isFraud` – Target variable (0 = Not Fraud, 1 = Fraud)

---

## 🧠 Feature Engineering

Additional features were created to capture transaction inconsistencies:

* **OrgbalanceDiff** = oldbalanceOrg - newbalanceOrig
* **DestbalanceDiff** = newbalanceDest - oldbalanceDest

These features are critical for identifying abnormal money flow patterns.

---

## ⚙️ Model Selection

### ✅ Final Model: Random Forest Classifier

**Why Random Forest?**

* Achieved **higher recall** compared to XGBoost
* Maintained strong **precision and F1-score**
* Performed consistently on imbalanced data

### 🔍 Key Insight:

* After hyperparameter tuning:

  * **Random Forest** → Recall improved while maintaining balance
  * **XGBoost** → Recall decreased

👉 Since **recall is most important in fraud detection**, Random Forest was selected.

---

## 📈 Evaluation Metrics

* **Precision** – Accuracy of fraud predictions
* **Recall** – Ability to detect fraud (most important)
* **F1-score** – Balance between precision and recall

---

## 🔥 Fraud Detection Patterns

The model identifies fraud based on patterns such as:

* Transactions with type **TRANSFER** or **CASH_OUT**
* Full balance withdrawal (`oldbalanceOrg → 0`)
* Mismatch between deducted and received amounts
* Large **OrgbalanceDiff** with low **DestbalanceDiff**

---

## 🌐 Web Application (Streamlit)

An interactive web app allows users to:

* Input transaction details
* Select transaction type
* Get fraud prediction instantly
* View probability of fraud

---

## 🚀 How to Run the Project

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/fraud-detection.git
cd fraud-detection
```

---

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install streamlit scikit-learn pandas numpy joblib
```

---

### 3️⃣ Run the Application

```bash
streamlit run app.py
```

---

### 4️⃣ Open in Browser

```
http://localhost:8501
```

---

## 🧪 Sample Test Inputs

### 🚨 Fraud Case

```
Type: TRANSFER
Amount: 150000
Old Balance (Sender): 150000
New Balance (Sender): 0
Old Balance (Receiver): 0
New Balance (Receiver): 0
OrgbalanceDiff(Sender Old-New): 150000
DestbalanceDiff(Receiver New-Old): 0
```

### ✅ Non-Fraud Case

```
Type: PAYMENT
Amount: 5000
Old Balance (Sender): 20000
New Balance (Sender): 15000
Old Balance (Receiver): 10000
New Balance (Receiver): 15000
OrgbalanceDiff(Sender Old-New): 100C
DestbalanceDiff(Receiver New-Old): 150C
```

---

## 📁 Project Structure

```
fraud-detection/
│
├── app.py                 # Streamlit application
├── model.pkl              # Trained Random Forest model
├── notebook.ipynb         # EDA + Model training
├── requirements.txt       # Dependencies
└── README.md              # Project documentation
```

---

## ⚠️ Important Notes

* Ensure feature order matches training data
* Use same encoding for `type`
* Use engineered features (balance differences)
* Threshold tuning improves recall

---

## 🔮 Future Improvements

* Deploy application online (Streamlit Cloud / AWS)
* Add real-time transaction monitoring
* Implement model comparison dashboard
* Use deep learning models for improved detection

---

## 🏁 Conclusion

This project demonstrates an effective fraud detection system using machine learning. By prioritizing recall and leveraging transaction patterns, the model successfully identifies fraudulent activities while maintaining reliability.

---

## 👨‍💻 Author

Rajesh Rijal

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
