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
        "invoiceCode": "",
        "batchNo": 19122,
        "referenceNumber": 1
    }
    try:
        reversal = await api.Reversal(**data)
        print(reversal)
    except OVOBadRequest as e:
        print(e.error_response)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start())