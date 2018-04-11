from models.soap import SoapMethods


obj = SoapMethods()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openConfig()["testSet"]["card"]
wsdl = obj.openConfig()["wsdl"][param]

def test_recreateCard():
    res = obj.connectToWebService(wsdl).service.recreateCard(cardHashNumber='$1$41023017$C89D9327F432D412238D42501C619C13', recreateType=2, branchId='175', oldCardStatus=0, chargeRenewFee=1, isPersonalized=0)
    print(type(res))
    print(res)
