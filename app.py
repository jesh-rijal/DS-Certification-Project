import streamlit as st
import pandas as pd
import joblib

model = joblib.load('online_fraud_model.pkl')

st.title('online Fraud Detection Web App')

st.markdown('Please enter the transaction details to predict fraud.')

st.divider()

transaction_type = st.selectbox('Transaction Type', ['PAYMENT', 'TRANSFER', 'CASH_OUT', 'DEPOSIT'])
amount = st.number_input('Amount', min_value = 0.0, value= 0.0)
oldbalanceOrg = st.number_input('Old Balance (Sender)', min_value = 0.0, value= 0.0)
newbalanceOrig = st.number_input('New Balance (Sender)', min_value= 0.0, value= 0.0)
oldbalanceDest = st.number_input('Old Balance (Receiver)', min_value= 0.0, value= 0.0)
newbalanceDest = st.number_input('New Balance (Receiver)', min_value= 0.0, value= 0.0)
OrgbalanceDiff = st.number_input('OrgbalanceDiff(Sender Old-New)', min_value= 0.0, value= 0.0)
DestbalanceDiff = st.number_input('DestbalanceDiff(Receiver New-Old)', min_value= 0.0, value= 0.0)

type_mapping = {
    'PAYMENT': 1,
    'TRANSFER': 2,
    'CASH_OUT': 3,
    'DEBIT': 4
}

type_encoded = type_mapping[transaction_type]

if st.button('Predict'):
    input_data = pd.DataFrame([{
        'type': type_encoded,
        'amount': amount,
        'oldbalanceOrg': oldbalanceOrg,
        'newbalanceOrig': newbalanceOrig,
        'oldbalanceDest': oldbalanceDest,
        'newbalanceDest': newbalanceDest,
        'OrgbalanceDiff': OrgbalanceDiff,
        'DestbalanceDiff': DestbalanceDiff

    }])


    prediction = model.predict(input_data)[0]

    st.subheader(f"Prediction : '{int(prediction)}'")

    if prediction == 1:
        st.error('This transaction is fraud')
    else:
        st.success('This transaction is not fraud')