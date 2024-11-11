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
        return np.random.choice(list(self.character_set), num_chars).tolist()
    
    def make_string(self, chars):
        return "".join(chars)

    def format_characters(self, chars):
        if self.is_string:
            return (
                '"'
                + self.make_string(chars)
                + '"'
            )

    def generate_1d_test_case(self, num_chars):
        chars = self.generate_random_characters(num_chars)

        if self.is_string:
            return self.format_characters(chars)
        return chars

    def generate_2d_test_case(self, num_rows, num_cols):
        if self.is_string:
            return [
                self.make_string(self.generate_random_characters(num_cols))
                for _ in range(num_rows)
            ]
        return [
            self.generate_random_characters(num_cols)
            for _ in range(num_rows)
        ]
    
    def generate_palindrome_test_case(self, num_chars):
        mid = []

        if num_chars % 2:
            mid = self.generate_random_characters(1)
        half = self.generate_random_characters(num_chars // 2)

        palindrome = half + mid + half[::-1]

        if self.is_string:
            return self.format_characters(palindrome)
        return palindrome

def generate_characters():
    options = char_sidebar_options()
    character_set = ""
    if options["lower"]:
        character_set += "abcdefghijklmnopqrstuvwxyz"
    if options["upper"]:
        character_set += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if options["digits"]:
        character_set += "0123456789"
    if options["special"]:
        character_set += "!@#$%^&*()"

    if options["custom_characters"] != "":
        character_set = options["custom_characters"]

    option, n = columize_options("characters")
    gen_chars = GenerateCharacters(options["is_string"], character_set)

    if character_set == "":
        st.warning("Please select atleast one character set from the sidebar")
        return

    if option == "Random characters in 1D Array": # Generate a 1D array of random characters
        num_chars = st.number_input(
            "Number of characters to generate:", min_value=1, step=1
        )
        if st.button("Generate"):
            for _ in range(n):
                if options["is_panlindrome"]:
                    st.code(gen_chars.generate_palindrome_test_case(num_chars))
                else:
                    st.code(gen_chars.generate_1d_test_case(num_chars))

        if options["digits"] and any((options["lower"], options["upper"], options["special"])) is False:
            st.warning(
                "Instead of this option, you can use Integer option to generate random integers"
            )

    elif option == "Random characters in 2D Array": # Generate a 2D array of random characters
        num_rows, num_cols = columize_grid(1)
        if st.button("Generate"):
            for _ in range(n):
                st.code(gen_chars.generate_2d_test_case(num_rows, num_cols))
