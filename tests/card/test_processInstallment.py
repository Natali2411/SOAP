from models.soap import SoapMethods


obj = SoapMethods()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]

def test_processInstallmentByAllParams():
    res = obj.connectToWebService(wsdl).service.processInstallment(adviceId="94109633")
    print(type(res))
    print(res)

def test_processInstallmentByEmptyAdviceId():
    res = obj.connectToWebService(wsdl).service.processInstallment(adviceId="", phoneNumber="+380983294154")
    print(res)
    assert res[0]["errorCode"] == 97