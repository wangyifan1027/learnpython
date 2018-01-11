# -*-coding:utf-8-*-
from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
    resp = app.request("/")
    assert_response(resp, status="404")
    
    resp = app.request("/hello")
    assert_response(resp)
    
    resp = app.request("/hello", method="POST")
    assert_response(resp, contains="<br/>")                  # 检查hello_form_laid_out.html中是否包含该值。
    
    resp = app.request("/hello")
    assert_response(resp, contains="A Greeting:")

    data = {'name': 'Evan Wong', 'greet': 'Joey Wong'}
    resp = app.request("/hello", method="POST", data=data)
    assert_response(resp, contains="Evan Wong")    