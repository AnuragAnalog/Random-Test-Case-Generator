# Utility functions

import streamlit as st


def char_sidebar_options():
    lower = st.sidebar.checkbox("Lowercase alphabets")
    upper = st.sidebar.checkbox("Uppercase alphabets")
    digits = st.sidebar.checkbox("Digits")
    special = st.sidebar.checkbox("Special characters")
    is_string = st.sidebar.checkbox("Generate as string")
    custom_characters = st.sidebar.text_input("Custom Characters", value="")
    is_panlindrome = st.sidebar.checkbox("Generate as Palindrome")

    options = {
        "lower": lower,
        "upper": upper,
        "digits": digits,
        "special": special,
        "is_string": is_string,
        "custom_characters": custom_characters,
        "is_panlindrome": is_panlindrome,
    }

    return options


def float_sidebar_options():
    round_val = st.sidebar.number_input("Round Value", min_value=1, max_value=6, step=1)

    return round_val


def boolean_sidebar_options():
    binarise = st.sidebar.checkbox("Binarise the boolean values")

    return binarise
