from models.soap import SoapMethods
from sql.sql_activateCard import SQLActivateCard

#class Test_activateCard():
obj = SoapMethods()
sql = SQLActivateCard()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]
connect = obj.dbConnect("ISCARDT2_AIX")


def test_fullParamsPositive():
    sql_res = connect.execute(sql.getCardForActivate()).fetchall()
    res = obj.connectToWebService(wsdl).service.activateCard(cardNumber=sql_res[0][0], taxId=sql_res[0][1],
                                                                           passportNumber=sql_res[0][2], phoneNumber=sql_res[0][3])
    t = sql.checkCardForActivateStatus(sql_res[0][0])
    r = connect.execute(t["s"], bind=str(t["bind"]["cardNumber"])).fetchall()[0]
    assert str(r[0]) == '0'
    obj.closeDBConnect(connect)
    

if __name__ == '__main__':
    pass