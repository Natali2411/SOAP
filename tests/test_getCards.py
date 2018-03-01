from models.soap import SoapMethods
test_set = SoapMethods().openConfig()["getCards_set"] # набор данных для теста с test_data.json
param = SoapMethods().openTestData()[test_set]

def test_shopId(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"])
        assert res["countMessages"]

def test_cardHash(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardHash=param["cardHash"])
        assert res["countMessages"]

def test_cardId(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardId=int(param["cardId"]))
        assert res["countMessages"]

def test_cardDeliveryStatus(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardDeliveryStatus=param["cardDeliveryStatus"])
        assert res["countMessages"]

def test_embCardName(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], embCardName=param["embCardName"])
        assert res["countMessages"]

def test_cardPrefix(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardPrefix=param["cardPrefix"])
        assert res["countMessages"]

def test_cardSuffix(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardSuffix=param["cardSuffix"])
        assert res["countMessages"]

def test_cardProject(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardProject=param["cardProject"])
        assert res["countMessages"]

def test_dateCreateFrom(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateCreateFrom=param["dateCreateFrom"])
        assert res["countMessages"]

def test_dateCreateTo(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateCreateTo=param["dateCreateTo"])
        assert res["countMessages"]

def test_dateExpFrom(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateExpFrom=param["dateExpFrom"])
        assert res["countMessages"]

def test_dateExpTo(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateExpTo=param["dateExpTo"])
        assert res["countMessages"]

def test_dateLastChangeFrom(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateLastChangeFrom=param["dateLastChangeFrom"])
        assert res["countMessages"]

def test_dateLastChangeTo(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateLastChangeTo=param["dateLastChangeTo"])
        assert res["countMessages"]

def test_manufacturer(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], manufacturer=param["manufacturer"])
        assert res["countMessages"]

def test_deliveryRegionCode(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], deliveryRegionCode=param["deliveryRegionCode"])
        assert res["countMessages"]

def test_deliveryDistrictCode(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], deliveryDistrictCode=param["deliveryDistrictCode"])
        assert res["countMessages"]

def test_barcode(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], barcode=param["barcode"])
        assert res["countMessages"]

def test_dateOnPrintFrom(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateOnPrintFrom=param["dateOnPrintFrom"])
        assert res["countMessages"]

def test_dateOnPrintTo(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateOnPrintTo=param["dateOnPrintTo"])
        assert res["countMessages"]

def test_batchId(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], batchId=param["batchId"])
        assert res["countMessages"]

def test_orderId(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], orderId=param["orderId"])
        assert res["countMessages"]

def test_taxId(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], taxId=param["taxId"])
        assert res["countMessages"]

def test_limit(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], limit=int(param["limit"]))
        assert res["countMessages"]

def test_offset(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], offset=int(param["offset"]))
        assert res["countMessages"]

def test_actId(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], actId=param["actId"])
        assert res["countMessages"]

def test_fioReceiver(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], fioReceiver=param["fioReceiver"])
        assert res["countMessages"]

def test_typeTransfer(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], typeTransfer=param["typeTransfer"])
        assert res["countMessages"]

def test_deliveryChannel(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], deliveryChannel=param["deliveryChannel"])
        assert res["countMessages"]

def test_deliveryType(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], deliveryType=param["deliveryType"])
        assert res["countMessages"]

def test_messageIdPrimaryProcess(obj):
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], messageIdPrimaryProcess=param["messageIdPrimaryProcess"])
        assert res["countMessages"]