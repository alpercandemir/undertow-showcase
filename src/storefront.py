from flask import Flask, request

from checkout import shipping_fee
from policies import (
    accepts_backorders, accepts_return, allows_installments, can_retry_delivery,
    express_dispatch_days, refund_state, reward_points_per_dollar,
)

app = Flask(__name__)


@app.post("/bulk-quotes")
def bulk_quotes():
    return {"shipping": [shipping_fee(total) for total in request.json["totals"]]}


@app.get("/orders/<int:total>/quote")
def order_quote(total):
    return {
        "shipping": shipping_fee(total),
        "reward_points": total * reward_points_per_dollar(),
        "dispatch_days": express_dispatch_days(),
        "backorders": accepts_backorders(),
    }


@app.post("/refunds")
def request_refund():
    if not accepts_return(request.json["days_since_delivery"]):
        return {"state": "EXPIRED"}
    return {"state": refund_state(request.json["receipt_attached"])}


@app.get("/installments/<int:months>")
def installment_offer(months):
    return {"eligible": allows_installments(months)}


@app.get("/deliveries/<int:attempts>/retry")
def delivery_retry(attempts):
    return {"eligible": can_retry_delivery(attempts)}
