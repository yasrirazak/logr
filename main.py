import pickle
import pandas as pd
import streamlit as st
logr = pickle.load(open('model.pkl','rb'))
x_test_data = [[1.0,14]]
X_test = pd.DataFrame(x_test_data, columns=['Sex', 'Hb'])
predicted = logr.predict(X_test)
print(predicted)

age = st.text_input("Sex","0") 
age = st.text_input("Hb","0"
if st.button("Predict"):
  x_test_data = [[1.0,14]]
  X_test = pd.DataFrame(x_test_data, columns=['Sex', 'Hb'])
  predicted = logr.predict(X_test)
  st.success('Predicted {}'.format(predicted))