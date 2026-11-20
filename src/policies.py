def accepts_return(days_since_delivery):
    return days_since_delivery <= 14


def allows_installments(months):
    return months <= 6


def refund_state(receipt_attached):
    if not receipt_attached:
        return "MANUAL_REVIEW"
    return "PENDING"


def express_dispatch_days():
    return 1


def reward_points_per_dollar():
    return 3


def can_retry_delivery(attempts):
    return attempts < 5


def accepts_backorders():
    return True
