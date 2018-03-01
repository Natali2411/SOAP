import pytest
import os, json
from models.soap import SoapMethods

@pytest.fixture()
def openConfig():
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'config.json'))
    with open(filename)as f:
        return json.load(f)

@pytest.fixture()
def openTestData():
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_data.json'))
    with open(filename)as f:
        return json.load(f)

@pytest.fixture()
def obj():
    return SoapMethods()

