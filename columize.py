import streamlit as st


def columize_options(dtype):
    col1, col2 = st.columns([0.65, 0.35])

    if dtype in ["integers", "floats"]:
        options = (
            f"Random {dtype}",
            f"Random {dtype} within a range",
            f"2D Random {dtype} within a range",
        )
    elif dtype in ["characters", "booleans"]:
        options = (f"Random {dtype} in 1D Array", f"Random {dtype} in 2D Array")

    with col1:
        option_widget = st.selectbox(
            "Choose the type of testcase to generate:", options
        )
    with col2:
        n = st.number_input("Number of Test Cases of generate", min_value=1, step=1)

    return option_widget, n


def columize_range(step):
    col1, col2 = st.columns(2)
    with col1:
        start_range = st.number_input("Start of range:", step=step)
    with col2:
        end_range = st.number_input("End of range:", step=step)

    return start_range, end_range


def columize_grid(step):
    col1, col2 = st.columns(2)
    with col1:
        num_rows = st.number_input("Number of rows:", min_value=1, step=step)
    with col2:
        num_cols = st.number_input("Number of columns:", min_value=1, step=step)

    return num_rows, num_cols


def columize_min_max(min, max, step):
    col1, col2 = st.columns(2)
    with col1:
        min_val = st.number_input("Minimum value:", step=step, value=min)
    with col2:
        max_val = st.number_input("Maximum value:", step=step, value=max)

    return min_val, max_val


def columize_range_and_grid(range_step, grid_step):
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        start_range = st.number_input("Start of range:", step=range_step)
    with col2:
        end_range = st.number_input("End of range:", step=range_step)
    with col3:
        num_rows = st.number_input("Number of rows:", min_value=1, step=grid_step)
    with col4:
        num_cols = st.number_input("Number of columns:", min_value=1, step=grid_step)

    return start_range, end_range, num_rows, num_cols
