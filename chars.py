import numpy as np
import streamlit as st

from utils import char_sidebar_options
from columize import columize_grid, columize_options


class GenerateCharacters:
    def __init__(self, is_string=None, character_set="") -> None:
        self.is_string = is_string
        self.character_set = character_set

    def set_config(self, kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def generate_random_characters(self, num_chars):
        if self.is_string:
            return (
                '"'
                + "".join(
                    np.random.choice(list(self.character_set), num_chars).tolist()
                )
                + '"'
            )
        return np.random.choice(list(self.character_set), num_chars).tolist()

    def generate_random_characters_2d(self, num_rows, num_cols):
        if self.is_string:
            return [
                "".join(np.random.choice(list(self.character_set), num_cols).tolist())
                for _ in range(num_rows)
            ]
        return [
            np.random.choice(list(self.character_set), num_cols).tolist()
            for _ in range(num_rows)
        ]


def generate_characters():
    lower, upper, digits, special, is_string = char_sidebar_options()
    character_set = ""
    if lower:
        character_set += "abcdefghijklmnopqrstuvwxyz"
    if upper:
        character_set += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if digits:
        character_set += "0123456789"
    if special:
        character_set += "!@#$%^&*()"

    option, n = columize_options("characters")
    gen_chars = GenerateCharacters(is_string, character_set)

    if character_set == "":
        st.warning("Please select atleast one character set from the sidebar")
        return

    if option == "Random characters in 1D Array":
        num_chars = st.number_input(
            "Number of characters to generate:", min_value=1, step=1
        )
        if st.button("Generate"):
            for _ in range(n):
                st.code(gen_chars.generate_random_characters(num_chars))

        if digits and any((lower, upper, special)) is False:
            st.warning(
                "Instead of this option, you can use Integer option to generate random integers"
            )

    elif option == "Random characters in 2D Array":
        num_rows, num_cols = columize_grid(1)
        if st.button("Generate"):
            for _ in range(n):
                st.code(gen_chars.generate_random_characters_2d(num_rows, num_cols))
