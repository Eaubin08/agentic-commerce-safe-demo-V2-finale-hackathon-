def evaluate(action):
    # Opaque safety gate (do NOT expose logic)
    if action.get("amount_usdc", 0) <= 5:
        return "ALLOW"
    return "BLOCK"
