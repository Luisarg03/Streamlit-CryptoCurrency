#!/usr/bin/env python
# -*- coding: utf-8 -*-
import streamlit as st
from modules.data import get_data
from modules.styles import style_table
from modules.views import table, buttom
from modules.funtions import ping


st.set_page_config(
    page_title='Cryptocurrncy',
    page_icon='coin',
    layout="wide")
    
st.write('# Cryptocurrency view')


if __name__ == '__main__':
    page_number = buttom()
    if ping() == True:
        df = get_data(page_number)
        df = style_table(df)
        table(df)
    else:
        pass

