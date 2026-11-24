from decimal import Decimal

from checkout import quote_coupon_cart


def observe_quote(record_property, prices):
    quote = quote_coupon_cart(prices)
    record_property("undertow.Items", ", ".join(f"${price}" for price in prices))
    record_property("undertow.Subtotal", f"${quote['subtotal']}")
    record_property("undertow.Coupon discount", f"${quote['discount']}")
    record_property("undertow.Amount due", f"${quote['amount_due']}")
    return quote


def test_coupon_rounds_once_on_cart_subtotal(record_property):
    quote = observe_quote(record_property, [Decimal("3.35")] * 3)

    assert quote == {
        "subtotal": Decimal("10.05"),
        "discount": Decimal("1.01"),
        "amount_due": Decimal("9.04"),
    }


def test_single_item_coupon_total(record_property):
    quote = observe_quote(record_property, [Decimal("3.35")])

    assert quote == {
        "subtotal": Decimal("3.35"),
        "discount": Decimal("0.34"),
        "amount_due": Decimal("3.01"),
    }
