from delivery import qualifies_for_free_delivery


def shipping_fee(order_total: int) -> int:
    return 0 if qualifies_for_free_delivery(order_total) else 7
