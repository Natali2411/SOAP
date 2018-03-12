from models.soap import SoapMethods
obj = SoapMethods()
test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
param = obj.openTestData()[test_set]
wsdl = obj.openConfig()["wsdl"]["createApplication"]


def test_createMassApps(obj):
    f = obj.openXlsFile('D:\Python\SOAP\delivery14.xlsx')
    v_count = 0
    for t in f:
        if len(str(f[str(t)][0])) > 1:
            contragentId = str(f[str(t)][0]).split(".")[0].strip()
            shopId = str(f[str(t)][7]).split(".")[0].strip()
            cardId = int(str(f[str(t)][9]).split(".")[0])
            objectTypeId = int(str(f[str(t)][12]).split(".")[0])

            res = obj.connectToWebService(wsdl).service.createApplication(contragentId=contragentId, taxId=f[str(t)][1],
                                                                          phoneNumber=f[str(t)][2], clientName=str(f[str(t)][3]), deliveryAddress=str(f[str(t)][4]),
                                                                          productName=str(f[str(t)][6]), shopId=shopId, cardId=cardId,
                                                                          cardMask=str(f[str(t)][10]), channelDelivery=str(f[str(t)][11]),
                                                                          objectTypeId=objectTypeId, comment="test", #str(f[str(t)][11]),
                                                                          messageIdPrimaryProcess=str(f[str(t)][14]), primaryProcessCode=str(f[str(t)][15]),
                                                                          dateExp='31.03.2018', externalSystem=str(f[str(t)][17]),
                                                                          user=str(f[str(t)][18]), plannedDeliveryDate=str(SoapMethods().getCurrentDateTime()))

            v_count += 1
    print("Rows created: " + str(v_count))
    return v_count

if __name__ == '__main__':
    test_createMassApps(SoapMethods())
