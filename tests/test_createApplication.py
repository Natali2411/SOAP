from models.soap import SoapMethods
from datetime import datetime
from zeep.xsd.elements.indicators import max_occurs_iter
from zeep import xsd
obj = SoapMethods()
#test_set = obj.openConfig()["testSet"]["getCards"] # набор данных для теста с test_data.json
#param = obj.openTestData()[test_set]
wsdl = obj.openConfig()["wsdl"]["createApplication"]


def test_createMassApps(obj):
    f = obj.openXlsFile('D:\Python\SOAP\delivery_2.xlsx')
    v_count = 0
    for t in f:
        if len(str(f[str(t)][0])) > 1:
            contragentId = str(f[str(t)][0]).split(".")[0].strip()
            shopId = str(f[str(t)][7]).split(".")[0].strip()
            cardId = int(str(f[str(t)][9]).split(".")[0])
            objectTypeId = int(str(f[str(t)][12]).split(".")[0])
            dateExp = datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(f[str(t)][16]) - 2).date()
            plannedDeliveryDate=datetime.fromordinal(datetime(1900, 1, 1).toordinal() + int(f[str(t)][19]) - 2).date()
            #listOfNecessaryDocuments = {"documentType": 1, "documentName": 'test', "documentDescription": 'test1'}
            #listOfNecessaryDocuments = (1, 'test', 'test1')
            xsd_type = xsd.ComplexType(
                xsd.Sequence([
                    xsd.Element('documentType', xsd.String()),
                    xsd.Element('documentName', xsd.String()),
                    xsd.Element('documentDescription', xsd.String())
                ]))
            listOfNecessaryDocuments = xsd_type(1, 2, 3)

            res = obj.connectToWebService(wsdl).service.createApplication(contragentId=contragentId, taxId=f[str(t)][1],
                                                                          phoneNumber=f[str(t)][2], clientName=str(f[str(t)][3]), deliveryAddress=str(f[str(t)][4]),
                                                                          productName=str(f[str(t)][6]), shopId=shopId, cardId=cardId,
                                                                          cardMask=str(f[str(t)][10]), channelDelivery=str(f[str(t)][11]),
                                                                          objectTypeId=objectTypeId, comment=str(f[str(t)][13]), #str(f[str(t)][11]),
                                                                          messageIdPrimaryProcess=str(f[str(t)][14]), primaryProcessCode=str(f[str(t)][15]),
                                                                          dateExp=dateExp, externalSystem=str(f[str(t)][17]),
                                                                          user=str(f[str(t)][18]), plannedDeliveryDate=plannedDeliveryDate,
                                                                          listOfNecessaryDocuments=list(listOfNecessaryDocuments))

            v_count += 1
            print(res)
    print("Rows created: " + str(v_count))

if __name__ == '__main__':
    test_createMassApps(SoapMethods())
