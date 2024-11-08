import streamlit as st

# import logfire
# logfire.configure()
# logfire.info("The computation starts.")

st.set_page_config(
   page_title="Modely v ekologii",
   layout="wide",
)

pg = st.navigation([
   st.Page('models/Main.py', title='Menu', icon='🚀'),
   st.Page('models/liska_ostrovni.py', title='Model lišky ostrovní', icon="🦊"),
   st.Page('models/Model_ostrovní_biogeografie.py', title='Model ostrovní biogeografie', icon="🐜"),
   st.Page('models/Logistický_růst_s_lovem.py', title='Logistický růst s lovem', icon="🕵️"),
   st.Page('models/Model_dravce_a_kořisti.py', title='Model dravce a kořisti', icon="🦈"),
])
pg.run()


