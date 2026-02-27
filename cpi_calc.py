import streamlit as st

def cpi_calc(final_cpi, current_cpi, current_creds, next_sem_creds):
    req_spi = (final_cpi * (current_creds + next_sem_creds) 
               - current_cpi * current_creds) / next_sem_creds
    return req_spi

st.title("CPI Target Calculator")

current_cpi = st.number_input("Current CPI", value=8.200, format="%.3f")
current_creds = st.number_input("Credits Completed", value=164)
next_sem_creds = st.number_input("Next Semester Credits", value=61)

# final_cpi = st.slider("Target Final CPI", 7.0, 10.0, 8.5, 0.01)
final_cpi = st.number_input(
    "Target Final CPI",
    min_value=7.000,
    max_value=10.000,
    value=8.500,
    step=0.001,
    format="%.3f"
)

required_spi = cpi_calc(final_cpi, current_cpi, current_creds, next_sem_creds)

st.subheader(f"Required SPI this semester: {required_spi:.3f}")
