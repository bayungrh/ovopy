def rc(RCcode):
    switcher = {
        "00": "SUCCESS",
        "14": "INVALID_MOBILE_NUMBER",
        "17": "TRANSACTION_DECLINE",
        "25": "TRANSACTION_NOT_FOUND",
        "26": "APPS_TRANSACTION_FAILED",
        "40": "TRANSACTION_FAILED",
        "54": "TRANSACTION_EXPIRED",
        "56": "CARD_BLOCKED",
        "58": "TRANSACTION_NOT_ALLOWED",
        "61": "EXCEED_TRANSACTION_LIMIT_BY_USER",
        "63": "SECURITY_VIOLATION",
        "64": "ACCOUNT_BLOCKED",
        "65": "EXCEED_TRANSACTION_LIMIT",
        "67": "BELOW_TRANSACTION_LIMIT",
        "68": "TRANSACTION_PENDING_OR_TIMEOUT",
        "73": "TRANSACTION_HAS_BEEN_REVERSED",
        "96": "INVALID_PROCESSING_CODE",
        "ER": "SYSTEM_FAILURE",
        "EB": "TERMINAL_BLOCKED"
    }
    return switcher.get(RCcode, None)