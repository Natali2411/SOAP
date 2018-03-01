import pytest
import os, json
from models.soap import SoapMethods


@pytest.fixture()
def obj():
    return SoapMethods()

