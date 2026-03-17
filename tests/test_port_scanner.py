import pytest
from tools.port_scanner import check_port

def test_open_port():
    result = check_port("google.com", 80)
    assert result[0] == True

def test_closed_port():
    result = check_port("google.com", 9999)
    assert result[0] == False

def test_invalid_host():
    result = check_port("fakehost9999.com", 80)
    assert result[2] == "Host not found"