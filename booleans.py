import numpy as np
import streamlit as st

def generate_booleans(binarise):
    option = st.selectbox(
        'Choose the type of testcase to generate:',
        ('Random booleans in 1D Array', 'Random booleans in 2D Array')
    )
    n = st.number_input('Number of Test Cases of generate', min_value=1, step=1)

    if option == 'Random booleans in 1D Array':
        num_bools = st.number_input('Number of booleans to generate:', min_value=1, step=1)
        if st.button('Generate'):
            for _ in range(n):
                if binarise:
                    st.code(np.random.choice([True, False], num_bools).astype(int).tolist())
                else:
                    st.code(np.random.choice([True, False], num_bools).tolist())
    elif option == 'Random booleans in 2D Array':
        num_rows = st.number_input('Number of rows:', min_value=1, step=1)
        num_cols = st.number_input('Number of columns:', min_value=1, step=1)
        if st.button('Generate'):
            for _ in range(n):
                if binarise:
                    st.code([np.random.choice([True, False], num_cols).astype(int).tolist() for _ in range (num_rows)])
                else:
                    st.code([np.random.choice([True, False], num_cols).tolist() for _ in range (num_rows)])