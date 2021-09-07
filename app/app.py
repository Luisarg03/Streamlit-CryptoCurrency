#!/usr/bin/env python
# -*- coding: utf-8 -*-
import streamlit as st
from modules.data import get_data
from modules.styles import style_table
from modules.views import table, buttom, box_select_coin, sidebar
from modules.funtions import ping


st.set_page_config(
    page_title='Cryptocurrency',
    page_icon='coin',
    layout="wide")

col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])


if __name__ == '__main__':
    sidebar()
    col1.write('### NumberPage')
    page_number = buttom(col1)
    col3.write('### Select your coin')
    box_coins = box_select_coin(col3)

    df = get_data(page_number, box_coins)

    col2.write('### Select columns view')
    box_cols =  col2.multiselect('', df.columns, help='Select columns...')
    
    if box_cols == []:
        pass
    else:
        box_cols.insert(0, 'LOGO')
        box_cols.insert(1, 'NAME')
        df = df[box_cols]

    if ping() == True:
        df = style_table(df)
        table(df)
    else:
        pass
    

