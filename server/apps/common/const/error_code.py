from enum import Enum


class ErrorCode(Enum):
    ServerError = 50000
    ParamsValidateFail = 40001
    AuthenticationFailed = 40003
