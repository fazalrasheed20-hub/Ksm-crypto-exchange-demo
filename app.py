import streamlit as st

st.set_page_config(
    page_title="KSM Crypto Exchange",
    page_icon="🚀"
)

st.title("🚀 KSM Crypto Exchange")

st.subheader("Demo Trading Platform")

st.success("Welcome to KSM Crypto Exchange!")

st.metric("Demo Balance", "1000 USDT")

st.info("This is an educational demo only.")

st.divider()

st.subheader("BTC / USDT")

price = 65000

st.write("BTC Price:", price, "USDT")

amount = st.number_input(
    "Enter USDT Amount",
    min_value=1,
    value=100
)

if st.button("BUY BTC"):
    btc = amount / price
    st.success(f"You bought {btc:.8f} BTC (Demo)")
