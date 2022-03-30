#!/usr/bin/env python3

from src.main import root

def test_root():
    expected = "User Information API please see the readme.md for details on how to interact with this service!"
    actual = root()
    assert expected == actual