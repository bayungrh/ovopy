class Constants(object):
    OVO_URL_PRODUCTION = "https://api.ovo.id/pos"
    OVO_URL_STAGING = "https://api.byte-stack.net/pos"

    TRANSACTION_TYPE = {
        "ptp": {
            "type": "0200",
            "code": "040000"
        },
        "reversal": {
            "type": "0400",
            "code": "040000"
        },
        "void": {
            "type": "0200",
            "code": "020040"
        },
        "checkPaymentPTP": {
            "type": "0100",
            "code": "040000"
        },
        "checkPaymentVoid": {
            "type": "0100",
            "code": "020040"
        }
    }