import numpy as np
import streamlit as st

from utils import boolean_sidebar_options
from columize import columize_grid, columize_options


class GenerateBooleans:
    def __init__(self, binarise=None) -> None:
        self.binarise = binarise

    def set_config(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def generate_random_booleans(self, num_bools):
        if self.binarise:
            return np.random.choice([True, False], num_bools).astype(int).tolist()
        return np.random.choice([True, False], num_bools).tolist()

    def generate_random_booleans_2d(self, num_rows, num_cols):
        if self.binarise:
            return [
                np.random.choice([True, False], num_cols).astype(int).tolist()
                for _ in range(num_rows)
            ]
        return [
            np.random.choice([True, False], num_cols).tolist() for _ in range(num_rows)
        ]


def generate_booleans():
    binarise = boolean_sidebar_options()
    option, n = columize_options("booleans")
    gen_bool = GenerateBooleans(binarise)

    if option == "Random booleans in 1D Array":
        num_bools = st.number_input(
            "Number of booleans to generate:", min_value=1, step=1
        )
        if st.button("Generate"):
            for _ in range(n):
                st.code(gen_bool.generate_random_booleans(num_bools))
    elif option == "Random booleans in 2D Array":
        num_rows, num_cols = columize_grid(1)
        if st.button("Generate"):
            for _ in range(n):
                st.code(gen_bool.generate_random_booleans_2d(num_rows, num_cols))
