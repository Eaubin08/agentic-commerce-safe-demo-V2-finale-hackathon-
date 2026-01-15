def agent_request(action_context):
    return {
        "intent": "buy_api_access",
        "amount_usdc": action_context.get("amount", 1),
        "recipient": action_context.get("recipient", "merchant_demo")
    }
