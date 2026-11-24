from decimal import Decimal

from checkout import quote_coupon_cart


def test_coupon_rounds_once_on_cart_subtotal():
    quote = quote_coupon_cart([Decimal("3.35")] * 3)

    assert quote == {
        "subtotal": Decimal("10.05"),
        "discount": Decimal("1.01"),
        "amount_due": Decimal("9.04"),
    }


def test_single_item_coupon_total():
    quote = quote_coupon_cart([Decimal("3.35")])

    assert quote == {
        "subtotal": Decimal("3.35"),
        "discount": Decimal("0.34"),
        "amount_due": Decimal("3.01"),
    }
