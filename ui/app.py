import streamlit as st
from demo.agent import agent_request
from demo.guard_lite import evaluate
from demo.pay_usdc import pay_usdc

st.title("Agentic Commerce — Safe USDC Payment")

amount = st.slider("USDC amount", 1, 10, 3)

if st.button("Agent tries to pay"):
    action = agent_request({"amount": amount, "recipient": "merchant_demo"})
    decision = evaluate(action)

    if decision == "ALLOW":
        pay_usdc(action["amount_usdc"], action["recipient"])
        st.success("Payment allowed and sent")
    else:
        st.error("Payment blocked (unsafe / ambiguous)")
