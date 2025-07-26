import streamlit as st
import pickle
import string
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
def clean_msg(msg):
    no_punc = [c for c in msg if c not in string.punctuation]
    no_punc = ''.join(no_punc)
    return [word for word in no_punc.split() if word.lower() not in stop_words]

with open('spam_classifier_model.pkl' , 'rb') as f:
    loaded_pipeline = pickle.load(f)

st.title('Spam V/S Ham Classifier')
st.image('https://cdn.prod.website-files.com/659fa592476e081fbd5a3335/669f84768899d32f200f7556_spamz.png',
         width= 200 , caption= 'Spot the scam!')
email = st.text_area('Please enter your email content here : ' , height= 250)

if st.button('Check if its spam'):
    prediction = loaded_pipeline.predict([email])[0]
    if prediction==1:
        st.error('The mail you entered is predcited to be spam!')
    else:
        st.success('Congratulations! The mail you entered is not spam!')
st.info('This model predicts spam mails with 97% precesion and ham mails with 96% precision!')