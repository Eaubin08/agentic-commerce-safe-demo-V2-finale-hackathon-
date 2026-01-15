import os
import requests

ARC_API_URL = os.getenv("ARC_API_URL", "https://api.arc.example/pay")
ARC_API_KEY = os.getenv("ARC_API_KEY")

def pay_usdc(amount, recipient):
    if not ARC_API_KEY:
        raise RuntimeError("ARC_API_KEY not set")

    payload = {
        "asset": "USDC",
        "amount": amount,
        "recipient": recipient
    }

    headers = {
        "Authorization": f"Bearer {ARC_API_KEY}",
        "Content-Type": "application/json"
    }

    # Real call would be enabled during hackathon
    # response = requests.post(ARC_API_URL, json=payload, headers=headers)
    # return response.json()

    print(f"[ARC] Simulated USDC payment: {amount} → {recipient}")
    return {"status": "submitted", "amount": amount}
