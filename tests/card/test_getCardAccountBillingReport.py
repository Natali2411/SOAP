from models.soap import SoapMethods


obj = SoapMethods()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]

def test_getCardAccountBillingReport():
    res = obj.connectToWebService(wsdl).service.getCardAccountBillingReport(accountNo="26251002423467", periodBegin="2015-01-01", periodEnd="2018-03-31", reportType="")
    print(res)
    assert res[5]["text"] == "Номер карткового рахунку:  26251002423467"