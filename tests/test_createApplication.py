from models.soap import SoapMethods
test_set = SoapMethods().openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = SoapMethods().openTestData()[test_set]
wsdl = SoapMethods().openConfig()["wsdl"]["createApplication"]
from datetime import datetime

def createMassApps(obj):
    f = obj.openXlsFile('D:\Python\SOAP\delivery14.xlsx')
    print(str(f['1'][0]).split(".")[0])

    for t in f:
        res = obj.connectToWebService(wsdl).service.createApplication(contragentId=str(f[str(t)][0]).split(".")[0], taxId=str(f[str(t)][1]).split(".")[0],
                                                                      phoneNumber=f[str(t)][2], clientName=str(f[str(t)][3]), deliveryAddress=str(f[str(t)][4]),
                                                                      productName=str(f[str(t)][6]), shopId=str(f[str(t)][7]).split(".")[0], cardId=str(f[str(t)][9]).split(".")[0],
                                                                      cardMask=str(f[str(t)][10]), channelDelivery=str(f[str(t)][11]),
                                                                      objectTypeId=str(f[str(t)][12]).split(".")[0], comment="test", #str(f[str(t)][11]),
                                                                      messageIdPrimaryProcess=str(f[str(t)][14]), primaryProcessCode=str(f[str(t)][15]),
                                                                      dateExp='31.03.2018', externalSystem=str(f[str(t)][17]),
                                                                      user=str(f[str(t)][18]))



if __name__ == '__main__':
    print(createMassApps(SoapMethods()))
