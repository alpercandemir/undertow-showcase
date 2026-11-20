from checkout import shipping_fee


def gift_checkout_total(order_total: int) -> int:
    return order_total + shipping_fee(order_total)
