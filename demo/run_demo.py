from agent import agent_request
from guard_lite import evaluate
from pay_usdc import pay_usdc

action = agent_request({"amount": 3, "recipient": "api_provider"})
decision = evaluate(action)

if decision == "ALLOW":
    pay_usdc(action["amount_usdc"], action["recipient"])
    print("Payment executed")
else:
    print("Payment blocked for safety reasons")
