import streamlit as st

def get_result(array, sort):
    if sort:
        return sorted(array)
    return array