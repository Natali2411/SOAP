from models.soap import SoapMethods
test_set = SoapMethods().openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = SoapMethods().openTestData()[test_set]
wsdl = SoapMethods().openConfig()["wsdl"]["createApplication"]


def createMassApps(obj):
    f = obj.openXlsFile('D:\Python\SOAP\delivery13.xlsx')
    v_count = 0
    for t in f:
        if len(str(f[str(t)][0])) > 1:
            contragentId = int(f[str(t)][0])
            shopId = int(f[str(t)][7])
            cardId = int(f[str(t)][9])
            objectTypeId = int(f[str(t)][12])

            res = obj.connectToWebService(wsdl).service.createApplication(contragentId=contragentId, taxId=f[str(t)][1],
                                                                          phoneNumber=f[str(t)][2], clientName=str(f[str(t)][3]), deliveryAddress=str(f[str(t)][4]),
                                                                          productName=str(f[str(t)][6]), shopId=shopId, cardId=cardId,
                                                                          cardMask=str(f[str(t)][10]), channelDelivery=str(f[str(t)][11]),
                                                                          objectTypeId=objectTypeId, comment="test", #str(f[str(t)][11]),
                                                                          messageIdPrimaryProcess=str(f[str(t)][14]), primaryProcessCode=str(f[str(t)][15]),
                                                                          dateExp='31.03.2018', externalSystem=str(f[str(t)][17]),
                                                                          user=str(f[str(t)][18]))

            v_count += 1
    print("Rows created: " + str(v_count))
    return v_count

if __name__ == '__main__':
    print(createMassApps(SoapMethods()))
