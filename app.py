import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Penguin Prediction App

This app predicts the **Palmer Penguin** species!
""")

st.sidebar.header('User Input Features')

#Hyperlink should be given inside () & name for hyperlink in [], inside markdown command
# The below markdown just displays the sample input csv file
st.sidebar.markdown("""
[Example CSV input file](https://raw.githubusercontent.com/dataprofessor/data/master/penguins_example.csv)
""")

# Collects user input features into dataframe in 2 ways:
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file",
                                         type=["csv"])

# 1st way: user input in the form of file uploaded
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file).drop(columns=[
        'species'
    ])  # this is used for prediction (contains multiple rows of data

# 2nd way: user input in the form of selectable features on the slider bar --ANY 1 WAY IS POSSIBLE
else:

    def user_input_features():
        st.subheader('Feature 1')
        island = st.sidebar.selectbox('Island',
                                      ('Biscoe', 'Dream', 'Torgersen'))
        st.subheader('Feature 2')
        sex = st.sidebar.selectbox('Sex', ('male', 'female'))
        st.subheader('Feature 3')
        bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1, 59.6,
                                           43.9)
        st.subheader('Feature 4')
        bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1, 21.5, 17.2)
        st.subheader('Feature 5')
        flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,
                                              231.0, 201.0)
        st.subheader('Feature 6')
        body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0, 6300.0,
                                        4207.0)
        data = {
            'island': island,
            'bill_length_mm': bill_length_mm,
            'bill_depth_mm': bill_depth_mm,
            'flipper_length_mm': flipper_length_mm,
            'body_mass_g': body_mass_g,
            'sex': sex
        }
        features = pd.DataFrame(data, index=[0])
        return features  # this is used for prediction (contains only 1 row of data)

    input_df = user_input_features()

# Combines user input features with entire penguins dataset
# This will be useful for the encoding phase
penguins_raw = pd.read_csv('penguins_cleaned.csv').drop(columns=['species'])
penguins = penguins_raw  #.drop(columns=['species'])
df = pd.concat([input_df, penguins], axis=0)

# Encoding of categorical features
encode = ['sex', 'island']
for col in encode:
    dummy = pd.get_dummies(df[col], prefix=col)
    df = pd.concat([df, dummy], axis=1)
    del df[col]
df = df[:1]  # Selects only the first row (the user input data)

# Displays the user input features
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(df)
else:
    st.write(
        'Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).'
    )
    st.write(df)

# Reads in saved classification model
load_clf = pickle.load(open('penguins_clf.pkl', 'rb'))

# Apply model to make predictions
st.markdown(""" Dataframe for prediction """)
st.write(df)
prediction = load_clf.predict(df)  #class prediction
prediction_proba = load_clf.predict_proba(df)  #class probability

#--------DISPLAY RESULTS-----------#
st.subheader('Prediction')
penguins_species = np.array(['Adelie', 'Chinstrap', 'Gentoo'])

#print(prediction)
st.write(penguins_species[prediction])

st.subheader('Prediction Probability')
st.write(prediction_proba)
