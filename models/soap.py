# pip install --trusted-host pypi.python.org pack_name
from zeep import Client
from zeep import xsd
from zeep.wsse.username import UsernameToken
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
import ssl

class SoapMethods():
    def __init__(self):
        pass

    def connectToWebService(self):
        session = Session()
        session.verify = False
        transport = Transport(session=session)
        client = Client('http://kwsesbapu06.alfa.bank.int:8280/services/CardLogisticsWF?wsdl',
                transport=transport, strict=False, wsse=UsernameToken("testuser", "testuser"))
        return client

if __name__ == '__main__':
    obj = SoapMethods()
    print(obj.connectToWebService())
