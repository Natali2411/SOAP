# pip install --trusted-host pypi.python.org pack_name
# python -m pip install --trusted-host pypi.python.org --upgrade lib_name (for example, cx_Oracle)
# pip install --trusted-host pypi.python.org -r requirements.txt   install all libraries from requirements.txt
from zeep import Client
from zeep import xsd
from zeep.wsse.username import UsernameToken
from requests import Session
from requests.auth import HTTPBasicAuth
from zeep.transports import Transport
import ssl, os, json
import xlrd, time, datetime
import cx_Oracle
from zeep.plugins import HistoryPlugin

class SoapMethods():
    def __init__(self):
        pass

    def getCurrentDateTime(self):
        return datetime.datetime.now()

    def connectToWebService(self, wsdl):
        session = Session()
        session.verify = False
        transport = Transport(session=session)
        client = Client(wsdl, plugins=[HistoryPlugin()], transport=transport, strict=False, wsse=UsernameToken("testuser", "testuser"))
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

    def dbConnect(self, db):

        dbType = self.openConfig()["db"][db]
        connection = cx_Oracle.connect(dbType["user"], dbType["password"], dbType["server"])
        #connection = cx_Oracle.connect('IC', 'vjcrdf4', 'ISCARDT4.WORLD')
        cursor = connection.cursor()
        return cursor


    def closeDBConnect(self, cursor):
        return cursor.close()



if __name__ == '__main__':
    obj = SoapMethods()
    #print(obj.openXlsFile('D:\Python\SOAP\delivery12.xlsx'))
    print(obj.dbConnect(db='ISCARDT2aix'))
