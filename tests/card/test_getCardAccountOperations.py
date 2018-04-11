from models.soap import SoapMethods


obj = SoapMethods()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]

def test_positive_params():
    res = obj.connectToWebService(wsdl).service.getCardAccountOperations(accountNo='26251002423467',
                                                                         periodBegin='2016-01-01', periodEnd='2016-01-01')
    print(res)