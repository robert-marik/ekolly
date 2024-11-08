import streamlit as st

def Navbar():
    with st.sidebar:
        st.page_link('app.py', label='Menu', icon='🚀')
        st.page_link('pages/liska_ostrovni.py', label='Model lišky ostrovní', icon="🦊")
        st.page_link('pages/Model_ostrovní_biogeografie.py', label='Model ostrovní biogeografie', icon="🐜")
        st.page_link('pages/Logistický_růst_s_lovem.py', label='Logistický růst s lovem', icon="🕵️")
        st.page_link('pages/Model_dravce_a_kořisti.py', label='Model dravce a kořisti', icon="🦈")
