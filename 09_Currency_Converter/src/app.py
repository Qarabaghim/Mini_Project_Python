import streamlit as st
from constants import CURRENCIES
from currency_convertor import get_exchange_rate, convert_currency


st.title(":dollar: Currency Converter")

st.markdown("""
This app converts currency from one currency to another.

Enter a currency and a target currency.
""")

base_currency = st.selectbox("from currency:", CURRENCIES)
target_currency = st.selectbox("to currency:", CURRENCIES, index=1)
amount = st.number_input("amount", value=100)

amount = st.number_input("amount to convert to", min_value=0, value=1)


if amount > 0 and base_currency and target_currency:
    exchange_rate = get_exchange_rate(base_currency, target_currency)

    if exchange_rate:
        converted_amount = convert_currency(amount, exchange_rate)
        st.success(f"exchange rate: {exchange_rate:.4f}")
        col1, col2, col3 = st.columns(3)
        col1.metric(label="Base Currency", value=f"{amount:.2f} {base_currency}")
        col2.markdown("<h1 style='text-align: center; margin: 0; color: green;'>&#8594;</h1>", unsafe_allow_html=True)
        col3.metric(label="Target Currency", value=f"{converted_amount:.2f} {target_currency}")
    else:
        st.error("no exchange rate")


st.markdown("---")
st.markdown("### ℹ️ About This Tool")
st.markdown("""
This currency converter uses real-time exchange rates provided by the ExchangeRate-API.
- The conversion updates automatically as you input the amount or change the currency.
- Enjoy seamless currency conversion without the need to press a button!
""")