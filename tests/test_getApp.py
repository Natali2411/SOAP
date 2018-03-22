from models.soap import SoapMethods
test_set = SoapMethods().openConfig()["testSet"]["getApp"] # набор данных для теста с test_data.json
param = SoapMethods().openTestData()[test_set]
wsdl = SoapMethods().openConfig()["wsdl"]["getApp"]

def test_mandatory_params(obj):
    res = obj.connectToWebService(wsdl).service.createApplication(shopId=)