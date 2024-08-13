#!/usr/bin/env python

import numpy as np
import streamlit as st

from utils import get_result
from columize import columize_range, columize_range_and_grid, columize_options

def generate_random_integers(max_value):
    return np.random.randint(0, max_value, 1)[0]

def generate_random_integers_range(start, end, num_integers, replace):
    return np.random.choice(range(start, end+1), size=num_integers, replace=replace).tolist()

def generate_random_integers_2d_range(start, end, num_rows, num_cols, replace):
    return np.random.choice(range(start, end+1), size=(num_rows, num_cols), replace=replace).tolist()

def generate_integers():
    option, n = columize_options('integers')

    if option == 'Random integers':
        num_integers = st.number_input('Max Value:(Minimum value is always 0)', min_value=0, value=10, step=1)
        if st.button('Generate'):
            for _ in range(n):
                st.code(generate_random_integers(num_integers))

    elif option == 'Random integers within a range':
        start_range, end_range = columize_range(1)
        num_integers = st.number_input('Number of integers to generate:', min_value=1, step=1)
        distinct = st.sidebar.checkbox('Generate distinct integers', value=True)
        sort = st.sidebar.checkbox('Sort the generated integers', value=False)
        if st.button('Generate'):
            for _ in range(n):
                result = generate_random_integers_range(start_range, end_range, num_integers, not(distinct))
                st.code(get_result(result, sort))

    elif option == '2D Random integers within a range':
        start_range, end_range, num_rows, num_cols = columize_range_and_grid(1, 1)
        distinct = st.sidebar.checkbox('Generate distinct integers', value=True)
        sort = st.sidebar.checkbox('Sort the generated integers', value=False)
        if st.button('Generate'):
            for _ in range(n):
                result = generate_random_integers_2d_range(start_range, end_range, num_rows, num_cols, not(distinct))
                st.code(get_result(result, sort))