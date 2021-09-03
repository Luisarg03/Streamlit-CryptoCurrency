#!/usr/bin/env python
# -*- coding: utf-8 -*-
import streamlit as st


def buttom(col):
    
    start_button = st.empty()

    page_number = col.number_input(
        label=" ",
        min_value=1,
        max_value=200,
        step=1,
    )

    return page_number


@st.cache(suppress_st_warning=True)
def table(data):
    table = st.empty()
    table.write(data.to_html(), unsafe_allow_html=True)

    return None



