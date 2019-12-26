from .endpoints import (
    PushToPayEndpoint, CheckPaymentEndpoints, ReversalEndpoints
)
from .constants import Constants

class OVO(PushToPayEndpoint, CheckPaymentEndpoints, ReversalEndpoints, Constants):
    def __init__(self, env='staging', **kwargs):
        self.ovo_url = Constants.OVO_URL_PRODUCTION if env == 'production' else Constants.OVO_URL_STAGING
        self.ovo_tid = kwargs.get('tid')
        self.ovo_mid = kwargs.get('mid')
        self.ovo_merchant_id = kwargs.get('merchantId')
        self.ovo_store_code = kwargs.get('storeCode')
        self.ovo_app_id = kwargs.get('appId')
        self.ovo_app_key = kwargs.get('appKey')
        self.transactionType = Constants.TRANSACTION_TYPE
        super(OVO, self).__init__()