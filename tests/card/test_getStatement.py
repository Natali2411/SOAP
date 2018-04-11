from models.soap import SoapMethods


obj = SoapMethods()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]

def test_getStatement():
    res = obj.connectToWebService(wsdl).service.getStatement(taskId="", contractId=973230, templateId=1, statementFrom="2016-08-20", statementTo="2018-08-30")
    print(res)
    #assert res[5]["text"] == "Номер карткового рахунку:  26251002423467"