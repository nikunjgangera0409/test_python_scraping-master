import pytest
from src.py import http_request

def test_http_request(params, expected_response):
    response = http_request(params)
    assert response == expected_response

def test_http_request_exception():
    response = http_request({"invalid params": 1})
    assert response is None