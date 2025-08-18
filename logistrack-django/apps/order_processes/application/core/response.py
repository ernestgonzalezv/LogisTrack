from typing import Generic, Optional, TypeVar
from django.utils.translation import gettext as _

T = TypeVar("T")

# Base Response
class BaseResponse:
    def __init__(self, success: bool = False, message: str = ""):
        self.success: bool = success
        self.message: str = message


# Response con ActionCode y Notification
class Response(BaseResponse):
    def __init__(self, success: bool = False, message: str = "", action_code: Optional[int] = None, notification: Optional[dict] = None):
        super().__init__(success, message)
        self.action_code: Optional[int] = action_code
        self.notification: Optional[dict] = notification


# Response con Data
class ResponseWithData(Response, Generic[T]):
    def __init__(self, success: bool = False, message: str = "", data: Optional[T] = None):
        super().__init__(success, message)
        self.data: Optional[T] = data


# Configuration Response
class ConfigurationResponse(ResponseWithData[T]):
    def __init__(self, success: bool = False, message: str = "", data: Optional[T] = None, configuration: Optional[dict] = None):
        super().__init__(success, message, data)
        self.configuration: Optional[dict] = configuration


# Error Response simple
class ErrorResponse(Response):
    def __init__(self, message: str = None):
        msg = message or _("Unknown error")
        super().__init__(success=False, message=msg)


# Error Response con Data
class ErrorResponseWithData(ResponseWithData[T]):
    def __init__(self, message: str, data: Optional[T] = None):
        super().__init__(success=False, message=message, data=data)
