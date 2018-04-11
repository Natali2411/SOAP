from models.soap import SoapMethods


obj = SoapMethods()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]

def test_getCardDealsByContragentId():
    res = obj.connectToWebService(wsdl).service.getCardDealsByContragentId(contragentId=3879014)
    print(res)
    assert res[0]["contragentId"] == '3879014'