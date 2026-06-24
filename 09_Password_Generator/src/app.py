import streamlit as st
from Password_Generators import random_Password, Memorable_Password, Pincode_Password
from nltk.corpus import words

st.title("Password Generator")

option = st.radio("Password Type", ('Random Password', 'Memorable Password', 'Pin Code'))

if option == 'Random Password':
    length = st.slider("Length", min_value=4, max_value=44, value=8)
    include_numbers = st.toggle("Include Numbers")
    include_symbols = st.toggle("Include Symbols")

    generator = random_Password(length, include_numbers, include_symbols)
elif option == 'Memorable Password':
    no_of_words = st.slider("Number of Words", min_value=4, max_value=44, value=8)
    separator = st.text_input("Separator", value='-')
    capitalization = st.toggle("Capitalization")

    generator = Memorable_Password(no_of_words, separator, capitalization, words.words())
else:
    length = st.slider("Length", min_value=4, max_value=44, value=8)

    generator = Pincode_Password(length)

password = generator.generate()
st.write("Your password is:")
st.header(fr"``` {password} ```")


