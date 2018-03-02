# pip install --trusted-host pypi.python.org pack_name
from zeep import Client
from zeep import xsd
from zeep.wsse.username import UsernameToken
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
import ssl, os, json
import xlrd

class SoapMethods():
    def __init__(self):
        pass

    def connectToWebService(self, wsdl):
        session = Session()
        session.verify = False
        transport = Transport(session=session)
        client = Client(wsdl, transport=transport, strict=False, wsse=UsernameToken("testuser", "testuser"))
        return client

    def openConfig(self):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'config.json'))
        with open(filename)as f:
            return json.load(f)

    def openTestData(self):
        filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'test_data.json'))
        with open(filename)as f:
            return json.load(f)

    def openXlsFile(self, file):
        vCount = 0
        res = {}
        rb = xlrd.open_workbook(file)
        sheet = rb.sheet_by_index(0)
        for rownum in range(sheet.nrows):
            row = sheet.row_values(rownum)
            res.update({str(vCount): row})
            vCount += 1
        return res #rb.nsheets


if __name__ == '__main__':
    obj = SoapMethods()
    print(obj.openXlsFile('D:\Python\SOAP\delivery12.xlsx'))
