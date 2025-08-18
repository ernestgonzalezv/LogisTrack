import pytest

from apps.order_processes.application.core.response import *


# -------------------
# Tests BaseResponse
# -------------------
def test_base_response_default():
    r = BaseResponse()
    assert r.success is False
    assert r.message == ""

def test_base_response_custom():
    r = BaseResponse(success=True, message="OK")
    assert r.success is True
    assert r.message == "OK"


# -------------------
# Tests Response
# -------------------
def test_response_default():
    r = Response()
    assert r.success is False
    assert r.message == ""
    assert r.action_code is None
    assert r.notification is None

def test_response_custom():
    r = Response(success=True, message="Done", action_code=200, notification={"type": "info"})
    assert r.success is True
    assert r.message == "Done"
    assert r.action_code == 200
    assert r.notification == {"type": "info"}


# -------------------
# Tests ResponseWithData
# -------------------
def test_response_with_data_default():
    r = ResponseWithData[int]()
    assert r.success is False
    assert r.message == ""
    assert r.data is None

def test_response_with_data_custom():
    r = ResponseWithData[int](success=True, message="OK", data=123)
    assert r.success is True
    assert r.message == "OK"
    assert r.data == 123


# -------------------
# Tests ConfigurationResponse
# -------------------
def test_configuration_response_default():
    r = ConfigurationResponse()
    assert r.success is False
    assert r.message == ""
    assert r.data is None
    assert r.configuration is None

def test_configuration_response_custom():
    r = ConfigurationResponse(success=True, message="OK", data={"key": "value"}, configuration={"mode": "test"})
    assert r.success is True
    assert r.message == "OK"
    assert r.data == {"key": "value"}
    assert r.configuration == {"mode": "test"}


# -------------------
# Tests ErrorResponse
# -------------------
def test_error_response_default():
    r = ErrorResponse()
    assert r.success is False
    assert r.message == "Unknown error"

def test_error_response_custom():
    r = ErrorResponse(message="Custom error")
    assert r.success is False
    assert r.message == "Custom error"


# -------------------
# Tests ErrorResponseWithData
# -------------------
def test_error_response_with_data_default_data():
    r = ErrorResponseWithData(message="Fail")
    assert r.success is False
    assert r.message == "Fail"
    assert r.data is None

def test_error_response_with_data_custom():
    r = ErrorResponseWithData(message="Fail", data={"info": 1})
    assert r.success is False
    assert r.message == "Fail"
    assert r.data == {"info": 1}
