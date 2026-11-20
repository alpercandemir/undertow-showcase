def qualifies_for_free_delivery(order_total: int) -> bool:
    """Return whether an order total in dollars qualifies for free delivery."""
    if order_total > 50:
        return True
    return False
