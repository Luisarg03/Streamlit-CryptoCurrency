#!/usr/bin/env python
# -*- coding: utf-8 -*-
import streamlit as st


def buttom():
    
    start_button = st.empty()
    col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])

    page_number = col1.number_input(
        label=" ",
        min_value=1,
        max_value=200,
        step=1,
    )

    return page_number


def table(data):
    table = st.empty()
    table.write(data.to_html(), unsafe_allow_html=True)

    return None



