import numpy as np
import streamlit as st

from columize import columize_range, columize_options

def generate_characters(lower, upper, digits, special, is_string):
    character_set = ''
    if lower:
        character_set += 'abcdefghijklmnopqrstuvwxyz'
    if upper:
        character_set += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if digits:
        character_set += '0123456789'
    if special:
        character_set += '!@#$%^&*()'

    option, n = columize_options('characters')

    if character_set == '':
        st.warning('Please select atleast one character set from the sidebar')
        return

    if option == 'Random characters in 1D Array':
        num_chars = st.number_input('Number of characters to generate:', min_value=1, step=1)
        if st.button('Generate'):
            for _ in range(n):
                if is_string:
                    st.code(''.join(np.random.choice(list(character_set), num_chars).tolist()))
                else:
                    st.code(np.random.choice(list(character_set), num_chars).tolist())
        if digits and any((lower, upper, special)) is False:
            st.warning('Instead of this option, you can use Integer option to generate random integers')

    elif option == 'Random characters in 2D Array':
        num_rows, num_cols = columize_range(1)
        if st.button('Generate'):
            for _ in range(n):
                if is_string:
                    st.code([''.join(np.random.choice(list(character_set), num_cols).tolist()) for _ in range(num_rows)])
                else:
                    st.code([np.random.choice(list(character_set), num_cols).tolist() for _ in range(num_rows)])