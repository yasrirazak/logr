import pickle
import pandas as pd
import streamlit as st
import sklearn
logr = pickle.load(open('model.pkl','rb'))
def main(): 
  age = st.text_input("Sex","0") 
  hb = st.text_input("Hb","0")
  if st.button("Predict"):
    x_test_data = [[age,hb]]
    X_test = pd.DataFrame(x_test_data, columns=['Sex', 'Hb'])
    predicted = logr.predict(X_test)
    st.success('Predicted {}'.format(predicted))
if __name__=='__main__': 
    main() 
    
