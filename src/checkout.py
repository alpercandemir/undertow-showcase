from decimal import Decimal, ROUND_HALF_UP

from delivery import qualifies_for_free_delivery


CENT = Decimal("0.01")
COUPON_RATE = Decimal("0.10")


def shipping_fee(order_total: int) -> int:
    return 0 if qualifies_for_free_delivery(order_total) else 7


def quote_coupon_cart(item_prices: list[Decimal]) -> dict[str, Decimal]:
    """Quote the merchandise subtotal and amount due for a 10% coupon."""
    subtotal = sum(item_prices, Decimal("0.00"))
    discount = (subtotal * COUPON_RATE).quantize(CENT, rounding=ROUND_HALF_UP)
    return {"subtotal": subtotal, "discount": discount, "amount_due": subtotal - discount}
