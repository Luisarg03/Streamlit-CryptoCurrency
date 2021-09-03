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

col1, col2, col3, col4, col5, col6 = st.columns([1,1,1,1,1,1])


if __name__ == '__main__':
    page_number = buttom(col1)
    df = get_data(page_number)
    box_cols =  col2.multiselect('', df.columns, help='Select columns...')
    box_coins =  col3.multiselect('', df['NAME'].unique(), help='Select coins...')

    if box_cols == []:
        pass
    else:
        df = df[box_cols]
    
    if box_coins == []:
        pass
    else:
        df = df.loc[df['NAME'].isin(box_coins)]

    if ping() == True:
        df = style_table(df)
        table(df)
    else:
        pass

