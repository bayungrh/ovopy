from ..exceptions import (
    OVOException, OVOBadRequest, OVOTimeoutException
)
import time
from datetime import datetime
from pytz import timezone
from ..util import (
    hasher, rc
)
import httpx

tzindo = timezone('Asia/Jakarta')

class PushToPayEndpoint(object):
    async def PushToPay(self, **kwargs):
        timestampStr = datetime.now(tzindo).strftime("%Y-%m-%d %H:%M:%S.%f")
        invoiceCode = kwargs.get('invoiceCode')
        batchNo = kwargs.get('batchNo')
        referenceNumber = kwargs.get('referenceNumber')
        amount = kwargs.get('amount')
        phone = kwargs.get('phone')
        is_void = kwargs.get('is_void', False)
        if is_void:
            processingCode = self.transactionType.get('void').get('code')
            transType = self.transactionType.get('void').get('type')
        else:
            processingCode = self.transactionType.get('ptp').get('code')
            transType = self.transactionType.get('ptp').get('type')

        body = {
            "type": transType,
            "processingCode": processingCode,
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
                "phone": str(phone)
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
        try:
            req = await httpx.post(self.ovo_url, json=body, headers=header, timeout=60000)
        except httpx.exceptions.TimeoutException as e:
            raise OVOTimeoutException("Payment Timeout")
        try:
            return req.json()
        except ValueError:
            raise OVOBadRequest("Bad Request", 400, req.text)

    def VoidPushToPay(self, **kwargs):
        kwargs.update({
            "is_void": True
        })
        return self.PushToPay(**kwargs)