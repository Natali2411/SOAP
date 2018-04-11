from models.soap import SoapMethods


obj = SoapMethods()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]

def test_getInstallmentProduct():
    res = obj.connectToWebService(wsdl).service.identifyCard(contragentId=3673576, card4Last=2450, docNo='')
    print(type(res))
    print(res)









