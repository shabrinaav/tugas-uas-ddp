import streamlit as streamlit

st.title("Form Data Diri")
st.write("Hello World")
st.write("Made By Bina")

with st.form("form_data_diri"):
     nama = st.text_input("Nama")
     alamat = st.text_input("Alamat")
     usia = st.number_input("Usia")
     submit = st.form_submit_button("Submit")


