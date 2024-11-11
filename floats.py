import numpy as np
import streamlit as st

from utils import float_sidebar_options
from columize import (
    columize_range,
    columize_options,
    columize_range_and_grid,
    columize_min_max,
)


class GenerateFloats:
    def __init__(self, sort=None, round_val=6) -> None:
        self.sort = sort
        self.round_val = round_val

    def set_config(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def generate_random_floats(self, start, end, num_floats):
        # Generates random floats within a range and rounds them with the map and converts it to list

        return list(
                    map(
                        lambda x: round(x, self.round_val), np.random.uniform(start, end, num_floats)
                    )
                )

    def generate_single_floats(self, min_value, max_value):
        # Generates a single float within a range

        return self.generate_random_floats(min_value, max_value, 1)[0]

    def generate_1d_test_case(self, start, end, num_floats):
        # Sort the floats if the user wants

        if self.sort:
            return sorted(
                self.generate_random_floats(start, end, num_floats)
            )

        return self.generate_random_floats(start, end, num_floats)

    def generate_2d_test_case(
        self, start, end, num_rows, num_cols
    ):
        # Sort the floats if the user wants

        if self.sort:
            return [
                sorted([round(x, self.round_val) for x in row])
                for row in np.random.uniform(
                    start, end, size=(num_rows, num_cols)
                ).tolist()
            ]
        return [
            [round(x, self.round_val) for x in row]
            for row in np.random.uniform(start, end, size=(num_rows, num_cols)).tolist()
        ]


def generate_floats():
    option, n = columize_options("floats")
    round_val = float_sidebar_options()
    gen_float = GenerateFloats(round_val=round_val)

    if option == "Random floats":
        min_value, max_value = columize_min_max(0.0, 10.0, 0.1)
        if st.button("Generate"):
            for _ in range(n):
                st.code(
                    gen_float.generate_single_floats(min_value, max_value)
                )

    elif option == "Random floats within a range":
        start_range, end_range = columize_range(0.1)
        num_floats = st.number_input(
            "Number of floats to generate:", min_value=1, step=1
        )
        sort = st.sidebar.checkbox("Sort the generated floats", value=False)
        gen_float.set_config({"sort": sort})

        if st.button("Generate"):
            for _ in range(n):
                st.code(
                    gen_float.generate_1d_test_case(
                        start_range, end_range, num_floats
                    )
                )

    elif option == "2D Random floats within a range":
        start_range, end_range, num_rows, num_cols = columize_range_and_grid(0.1, 1)
        sort = st.sidebar.checkbox("Sort the generated floats", value=False)
        gen_float.set_config({"sort": sort})

        if st.button("Generate"):
            for _ in range(n):
                st.code(
                    gen_float.generate_2d_test_case(
                        start_range, end_range, num_rows, num_cols
                    )
                )
