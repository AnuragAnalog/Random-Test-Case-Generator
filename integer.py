#!/usr/bin/env python

import numpy as np
import streamlit as st

from columize import columize_range, columize_range_and_grid, columize_options

class GenerateIntegers():
    def __init__(self, distinct=None, sort=None) -> None:
        self.distinct = not(distinct)
        self.sort = sort

    def set_config(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def generate_random_integers(self, max_value):
        return np.random.randint(0, max_value, 1)[0]
    
    def generate_random_integers_range(self, start, end, num_integers):
        if self.sort:
            return sorted(np.random.choice(range(start, end+1), size=num_integers, replace=self.distinct).tolist())
        return np.random.choice(range(start, end+1), size=num_integers, replace=self.distinct).tolist()
    
    def generate_random_integers_2d_range(self, start, end, num_rows, num_cols):
        if self.sort:
            return np.sort(np.random.choice(range(start, end+1), size=(num_rows, num_cols), replace=self.distinct)).tolist()
        return np.random.choice(range(start, end+1), size=(num_rows, num_cols), replace=self.distinct).tolist()

def generate_integers():
    option, n = columize_options('integers')
    gen_int = GenerateIntegers()

    if option == 'Random integers':
        num_integers = st.number_input('Max Value:(Minimum value is always 0)', min_value=0, value=10, step=1)
        if st.button('Generate'):
            for _ in range(n):
                st.code(gen_int.generate_random_integers(num_integers))

    elif option == 'Random integers within a range':
        start_range, end_range = columize_range(1)
        num_integers = st.number_input('Number of integers to generate:', min_value=1, step=1)
        distinct = st.sidebar.checkbox('Generate distinct integers', value=True)
        sort = st.sidebar.checkbox('Sort the generated integers', value=False)
        gen_int.set_config({'distinct': not(distinct), 'sort': sort})

        if st.button('Generate'):
            for _ in range(n):
                st.code(gen_int.generate_random_integers_range(start_range, end_range, num_integers))

    elif option == '2D Random integers within a range':
        start_range, end_range, num_rows, num_cols = columize_range_and_grid(1, 1)
        distinct = st.sidebar.checkbox('Generate distinct integers', value=True)
        sort = st.sidebar.checkbox('Sort the generated integers', value=False)
        gen_int.set_config({'distinct': not(distinct), 'sort': sort})

        if st.button('Generate'):
            for _ in range(n):
                st.code(gen_int.generate_random_integers_2d_range(start_range, end_range, num_rows, num_cols))