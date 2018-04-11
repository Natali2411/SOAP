from models.soap import SoapMethods


obj = SoapMethods()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]

def test_setCardDealCreditLimit():
    res = obj.connectToWebService(wsdl).service.setCardDealCreditLimit(dealId=16369, accountNo='26251000016133', newCreditLimit=100, startDate='2018-03-01', endDate='2018-03-16', noSMS=1)
    print(res)
    assert len(res) == 0