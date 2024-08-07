import numpy as np
import streamlit as st

def generate_characters(lower, upper, digits, special):
    character_set = ''
    if lower:
        character_set += 'abcdefghijklmnopqrstuvwxyz'
    if upper:
        character_set += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if digits:
        character_set += '0123456789'
    if special:
        character_set += '!@#$%^&*()'

    if character_set == '':
        st.warning('Please select atleast one character set')
        return

    option = st.selectbox(
        'Choose the type of testcase to generate:',
        ('Random characters in 1D Array', 'Random characters in 2D Array')
    )

    if option == 'Random characters in 1D Array':
        num_chars = st.number_input('Number of characters to generate:', min_value=1, step=1)
        if st.button('Generate'):
            st.code(''.join(np.random.choice(list(character_set), num_chars)))

    elif option == 'Random characters in 2D Array':
        num_rows = st.number_input('Number of rows:', min_value=1, step=1)
        num_cols = st.number_input('Number of columns:', min_value=1, step=1)
        if st.button('Generate'):
            st.code([np.random.choice(list(character_set), num_cols).tolist() for _ in range(num_rows)])