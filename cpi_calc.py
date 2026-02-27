import streamlit as st

def cpi_calc(final_cpi, current_cpi, current_creds, next_sem_creds):
    req_spi = (final_cpi * (current_creds + next_sem_creds) 
               - current_cpi * current_creds) / next_sem_creds
    return req_spi

st.title("CPI Target Calculator")

current_cpi = st.number_input("Current CPI", value=8.2)
current_creds = st.number_input("Credits Completed", value=164)
next_sem_creds = st.number_input("Next Semester Credits", value=61)

final_cpi = st.slider("Target Final CPI", 7.0, 10.0, 8.5, 0.1)

required_spi = cpi_calc(final_cpi, current_cpi, current_creds, next_sem_creds)

st.subheader(f"Required SPI this semester: {required_spi:.2f}")