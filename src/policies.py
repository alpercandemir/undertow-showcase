def accepts_return(days_since_delivery):
    return days_since_delivery <= 30


def allows_installments(months):
    return months <= 12


def refund_state(receipt_attached):
    if not receipt_attached:
        return "REJECTED"
    return "PENDING"


def express_dispatch_days():
    return 2


def reward_points_per_dollar():
    return 1


def can_retry_delivery(attempts):
    return attempts < 3


def accepts_backorders():
    return False
