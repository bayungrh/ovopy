import logging

logger = logging.getLogger(__name__)

class OVOException(Exception):
    """Generic error class, catch-all for most client issues.
    """
    def __init__(self, msg, code=None, error_response={}):
        self.code = code or 0
        self.error_response = error_response
        super(OVOException, self).__init__(msg)

class OVOTimeoutException(OVOException):
    """Raised when login fails."""
    pass

class OVOBadRequest(OVOException):
    """Raised when login fails."""
    pass

class InvalidPhoneNumberException(OVOException):
    """Raised when login fails."""
    pass