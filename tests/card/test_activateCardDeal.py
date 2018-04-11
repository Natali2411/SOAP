from models.soap import SoapMethods
from sql.sql_activateCardDeal import SQLActivateDeal

obj = SoapMethods()
sql = SQLActivateDeal()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]
connect = obj.dbConnect("ISCARDT2_AIX")

def test_activateCardDeal():
    #res = obj.connectToWebService(wsdl).service.activateCardDeal(contragentId='2942575', dealNo='650121251')

    sql_res = connect.execute(sql.getDealForActivate()).fetchall()
    res = obj.connectToWebService(wsdl).service.activateCardDeal(contragentId=sql_res[0][0], dealNo=sql_res[0][1])
    t = sql.checkDealForActivateStatus(sql_res[0][1])
    r = connect.execute(t["s"], bind=str(t["bind"]["charactseller"])).fetchall()[0]
    assert str(r[0]) == '0'
    obj.closeDBConnect(connect)


    print(res)
    #assert len(res) == 0