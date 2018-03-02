from models.soap import SoapMethods
test_set = SoapMethods().openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = SoapMethods().openTestData()[test_set]
wsdl = SoapMethods().openConfig()["wsdl"]["createApplication"]


def createMassApps(obj):
    '''
    f = obj.openXlsFile('D:\Python\SOAP\delivery12.xlsx')
    print(f)
    res = obj.connectToWebService(wsdl).service.createApplication(contragentId=f["2"][0], taxId=f["2"][1], phoneNumber=f["2"][2],
    сlientName=f["2"][3], deliveryAddress=f["2"][4], productName=f["2"][5], shopId=f["2"][6], cardId=f["2"][7], cardMask=f["2"][8],
    channelDelivery=f["2"][9], objectTypeId=f["2"][10], comment=f["2"][11], messageIdPrimaryProcess=f["2"][12], primaryProcessCode=f["2"][13],
    dateExp=f["2"][14], externalSystem=f["2"][15], user=f["2"][16])'''
    res = obj.connectToWebService(wsdl).service.createApplication()
    return res