#!/usr/bin/python3

import numpy as np
import streamlit as st

def generate_random_integers(max_value):
    return np.random.randint(0, max_value, 1)[0]

def generate_random_floats(max_value, round_val):
    return round(np.random.uniform(0, max_value, 1)[0], round_val)

def generate_random_integers_range(start, end, num_integers):
    return np.random.randint(start, end, num_integers).tolist()

def generate_random_floats_range(start, end, num_floats, round_val):
    return [round(x, round_val) for x in np.random.uniform(start, end, num_floats).tolist()]

def generate_random_integers_2d_range(start, end, num_rows, num_cols):
    return np.random.randint(start, end, size=(num_rows, num_cols)).tolist()

def generate_random_floats_2d_range(start, end, num_rows, num_cols, round_val):
    return [[round(x, round_val) for x in row] for row in np.random.uniform(start, end, size=(num_rows, num_cols)).tolist()]

st.title('Random Testcase Generator')

def main():
    st.sidebar.title('Select the DataType')
    option = st.sidebar.selectbox(
        'Choose the type of testcase to generate:',
        ("Integers", "Floats", "Characters", "Booleans")
    )

    if option == 'Integers':
        generate_integers()
    elif option == 'Floats':
        round_val = st.sidebar.number_input("Round Value", min_value=1, max_value=6, step=1)
        generate_floats(round_val)

def generate_integers():
    option = st.selectbox(
        'Choose the type of testcase to generate:',
        ('Random integers', 'Random integers within a range', '2D Random integers within a range')
    )

    if option == 'Random integers':
        num_integers = st.number_input('Max Value:(Minimum value is always 0)', min_value=0, value=10, step=1)
        if st.button('Generate'):
            st.code(generate_random_integers(num_integers))

    elif option == 'Random integers within a range':
        start_range = st.number_input('Start of range:', step=1)
        end_range = st.number_input('End of range:', step=1)
        num_integers = st.number_input('Number of integers to generate:', min_value=1, step=1)
        if st.button('Generate'):
            st.code(generate_random_integers_range(start_range, end_range, num_integers))

    elif option == '2D Random integers within a range':
        start_range = st.number_input('Start of range:', step=1)
        end_range = st.number_input('End of range:', step=1)
        num_rows = st.number_input('Number of rows:', min_value=1, step=1)
        num_cols = st.number_input('Number of columns:', min_value=1, step=1)
        if st.button('Generate'):
            st.code(generate_random_integers_2d_range(start_range, end_range, num_rows, num_cols))

def generate_floats(round_val):
    option = st.selectbox(
        'Choose the type of testcase to generate:',
        ('Random floats', 'Random floats within a range', '2D Random floats within a range')
    )

    if option == 'Random floats':
        num_floats = st.number_input('Max Value:(Minimum value is always 0)', min_value=0.0, value=10.0, step=0.1)
        if st.button('Generate'):
            st.code(generate_random_floats(num_floats, round_val))

    elif option == 'Random floats within a range':
        start_range = st.number_input('Start of range:', step=0.1)
        end_range = st.number_input('End of range:', step=0.1)
        num_floats = st.number_input('Number of floats to generate:', min_value=1, step=1)
        if st.button('Generate'):
            st.code(generate_random_floats_range(start_range, end_range, num_floats, round_val))

    elif option == '2D Random floats within a range':
        start_range = st.number_input('Start of range:', step=0.1)
        end_range = st.number_input('End of range:', step=0.1)
        num_rows = st.number_input('Number of rows:', min_value=1, step=1)
        num_cols = st.number_input('Number of columns:', min_value=1, step=1)
        if st.button('Generate'):
            st.code(generate_random_floats_2d_range(start_range, end_range, num_rows, num_cols, round_val))

if __name__ == '__main__':
    main()