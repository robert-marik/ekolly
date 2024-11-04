import streamlit as st

def Navbar():
    with st.sidebar:
        st.page_link('app.py', label='Menu', icon='🔥')
        st.page_link('pages/Model_ostrovní_biogeografie.py', label='Model ostrovní biogeografie')
        st.page_link('pages/Logistický_růst_s_lovem.py', label='Logistický růst s lovem')
        st.page_link('pages/Model_dravce_a_kořisti.py', label='Model dravce a kořisti')
