#!/usr/bin/env python3

from src.main import (
    delete, 
    root, 
    create, 
    read, 
    read_all, 
    update,  
)

def test_root():
    expected = "User Information API please see the readme.md for details on how to interact with this service!"
    actual = root()
    assert expected == actual