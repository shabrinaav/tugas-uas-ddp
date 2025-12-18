import streamlit as st

st.title("Form Data Diri")
st.write("Hello World")
st.write("Made By Bina")

with st.form("form_data_diri"):
     nama = st.text_input("Nama")
     alamat = st.text_input("Alamat")
     usia = st.number_input("Usia")
     submit = st.form_submit_button("Submit")

     if submit:
          st.success(f"Terima Kasih {nama} telah mengisi form data diri")
          st.write(f"Nama : {nama}")
          st.write(f"Alamat : {alamat}")
          st.write(f"Usia : {usia}")
          