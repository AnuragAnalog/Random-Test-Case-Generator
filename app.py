#!/usr/bin/python3

import streamlit as st

from integer import generate_integers
from floats import generate_floats
from chars import generate_characters
from booleans import generate_booleans

st.set_page_config(page_title="Random Testcase Generator", layout="wide")
st.title("Random Testcase Generator")


def main():
    st.sidebar.title("Select the DataType")
    option = st.sidebar.selectbox(
        "Select the data type of testcase:",
        ("Integers", "Floats", "Characters", "Booleans"),
    )

    if option == "Integers":
        generate_integers()
    elif option == "Floats":
        generate_floats()
    elif option == "Characters":
        generate_characters()
    elif option == "Booleans":
        generate_booleans()


if __name__ == "__main__":
    main()
