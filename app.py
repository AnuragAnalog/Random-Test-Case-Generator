#!/usr/bin/python3

import streamlit as st

from integer import generate_integers
from floats import generate_floats
from chars import generate_characters
from booleans import generate_booleans

st.set_page_config(page_title='Random Testcase Generator', layout='wide')
st.title('Random Testcase Generator')

def main():
    st.sidebar.title('Select the DataType')
    option = st.sidebar.selectbox(
        'Select the data type of testcase:',
        ("Integers", "Floats", "Characters", "Booleans")
    )

    if option == 'Integers':
        generate_integers()
    elif option == 'Floats':
        round_val = st.sidebar.number_input("Round Value", min_value=1, max_value=6, step=1)
        generate_floats(round_val)
    elif option == 'Characters':
        lower = st.sidebar.checkbox('Include lowercase characters', value=True)
        upper = st.sidebar.checkbox('Include uppercase characters', value=False)
        digits = st.sidebar.checkbox('Include digits', value=False)
        special = st.sidebar.checkbox('Include special characters', value=False)
        is_string = st.sidebar.checkbox('Generate as string', value=False)

        generate_characters(lower=lower, upper=upper, digits=digits, special=special, is_string=is_string)
    elif option == 'Booleans':
        binarise = st.sidebar.checkbox('Binarise the output', value=False)

        generate_booleans(binarise=binarise)

if __name__ == '__main__':
    main()