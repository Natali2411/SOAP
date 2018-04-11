from models.soap import SoapMethods


obj = SoapMethods()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]

def test_getBalanceByAllParams():
    res = obj.connectToWebService(wsdl).service.getActualBalanceByCard(contractId=2440669, accountNumber='2625')
    print(type(res))
    print(res)

def test_getBalanceByContractId():
    res = obj.connectToWebService(wsdl).service.getActualBalanceByCard(contractId=2440669)
    print(type(res))
    print(res)
