from ..exceptions import (
    OVOBadRequest
)
import time
from datetime import datetime
from pytz import timezone
from ..util import (
    hasher, rc
)
import httpx

tzindo = timezone('Asia/Jakarta')

class ReversalEndpoints(object):
    async def Reversal(self, **kwargs):
        timestampStr = datetime.now(tzindo).strftime("%Y-%m-%d %H:%M:%S.%f")
        invoiceCode = kwargs.get('invoiceCode')
        batchNo = kwargs.get('batchNo')
        referenceNumber = kwargs.get('referenceNumber')
        amount = kwargs.get('amount')
        phone = kwargs.get('phone')

        body = {
            "type": self.transactionType.get('reversal').get('type'),
            "processingCode": self.transactionType.get('reversal').get('code'),
            "amount": amount,
            "date": timestampStr,
            "referenceNumber": referenceNumber,
            "tid": str(self.ovo_tid),
            "mid": str(self.ovo_mid),
            "merchantId": str(self.ovo_merchant_id),
            "storeCode": str(self.ovo_store_code),
            "appSource":"POS",
            "transactionRequestData":{
                "batchNo": batchNo,
                "merchantInvoice":str(invoiceCode),
            }
        }
        unix_random = int(time.time())
        hmac_data = "{}{}".format(self.ovo_app_id, unix_random)
        hmac = hasher.hmac_hash(self.ovo_app_key, hmac_data)
        header = {
            "app-id": self.ovo_app_id,
            "random": str(unix_random),
            "hmac": hmac
        }
        req = await httpx.post(OVO_URL, json=body, headers=header)
        try:
            return req.json()
        except ValueError:
            raise OVOBadRequest("Bad Request", 400, req.text)