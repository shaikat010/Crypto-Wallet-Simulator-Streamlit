import streamlit as st
from PIL import Image
from trilio import *

# Creating the blockchain object
blockchain = Trilio()

col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write("")

with col2:
    img = Image.open("MetaMask_Fox.png")
    # display image using streamlit
    # width is used to set the width of an image
    st.image(img, width=200)

with col3:
    st.write("")

import streamlit as st
st.markdown("<h1 style='text-align: center; color: white;'>Blockchain Wallet Simulator</h1>", unsafe_allow_html=True)



col1, col2, col3 = st.columns([1,1,1])

with col1:
    st.write("")

with col2:
    x = st.button("Request for Wallet Account!")

with col3:
    st.write("")

with st.sidebar:
    st.title('Blockchain Wallet Simulator: About ')
    st.write("This is a simple blockchain wallet simulator make in streamlit! The simulator has the ability to store account details and be able to able to generate public and private keys!")
    img = Image.open("key.png")
    # display image using streamlit
    # width is used to set the width of an image
    st.image(img, width=200)
    if(x):
        st.write("The account has been created")





