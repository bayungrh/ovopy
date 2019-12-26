import os
try:
    from ovopy import (
        OVO, OVOException, OVOTimeoutException, InvalidPhoneNumberException, OVOBadRequest,
        __version__ as client_version)
except ImportError:
    import sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
    from ovopy import (
        OVO, OVOException, OVOTimeoutException, InvalidPhoneNumberException, OVOBadRequest,
        __version__ as client_version)
import json
import asyncio

async def start():
    config = {
        "tid": "",
        "mid": "",
        "storeCode": "",
        "merchantId": "",
        "appId": "",
        "appKey": ""
    }
    api = OVO('staging', **config)
    data = {
        "amount": 1000,
        "phone": "082113922xxx",
        "invoiceCode": "",
        "batchNo": 19122,
        "referenceNumber": 1
    }
    try:
        check_payment = await api.CheckPaymentStatus(**data)
        print(check_payment)
    except OVOBadRequest as e:
        print(e.error_response)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start())