import numpy as np
import streamlit as st

from columize import columize_range, columize_options, columize_range_and_grid

def generate_random_floats(max_value, round_val):
    return round(np.random.uniform(0, max_value, 1)[0], round_val)

def generate_random_floats_range(start, end, num_floats, round_val):
    return [round(x, round_val) for x in np.random.uniform(start, end, num_floats).tolist()]

def generate_random_floats_2d_range(start, end, num_rows, num_cols, round_val):
    return [[round(x, round_val) for x in row] for row in np.random.uniform(start, end, size=(num_rows, num_cols)).tolist()]

def generate_floats(round_val):
    option, n = columize_options('floats')

    if option == 'Random floats':
        num_floats = st.number_input('Max Value:(Minimum value is always 0)', min_value=0.0, value=10.0, step=0.1)
        if st.button('Generate'):
            for _ in range(n):
                st.code(generate_random_floats(num_floats, round_val))

    elif option == 'Random floats within a range':
        start_range, end_range = columize_range(0.1)
        num_floats = st.number_input('Number of floats to generate:', min_value=1, step=1)
        if st.button('Generate'):
            for _ in range(n):
                st.code(generate_random_floats_range(start_range, end_range, num_floats, round_val))

    elif option == '2D Random floats within a range':
        start_range, end_range, num_rows, num_cols = columize_range_and_grid(0.1, 1)
        if st.button('Generate'):
            for _ in range(n):
                st.code(generate_random_floats_2d_range(start_range, end_range, num_rows, num_cols, round_val))