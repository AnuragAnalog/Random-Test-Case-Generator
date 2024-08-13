import numpy as np
import streamlit as st

from columize import columize_grid, columize_options

def generate_booleans(binarise):
    option, n = columize_options('booleans')

    if option == 'Random booleans in 1D Array':
        num_bools = st.number_input('Number of booleans to generate:', min_value=1, step=1)
        if st.button('Generate'):
            for _ in range(n):
                if binarise:
                    st.code(np.random.choice([True, False], num_bools).astype(int).tolist())
                else:
                    st.code(np.random.choice([True, False], num_bools).tolist())
    elif option == 'Random booleans in 2D Array':
        num_rows, num_cols = columize_grid(1)
        if st.button('Generate'):
            for _ in range(n):
                if binarise:
                    st.code([np.random.choice([True, False], num_cols).astype(int).tolist() for _ in range (num_rows)])
                else:
                    st.code([np.random.choice([True, False], num_cols).tolist() for _ in range (num_rows)])