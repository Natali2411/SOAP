test_set = "getCards1" # набор данных для теста с test_data.json
def test_shopId(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"])
        assert res["countMessages"]

def test_cardHash(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardHash=param["cardHash"])
        assert res["countMessages"]

def test_cardId(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardId=int(param["cardId"]))
        assert res["countMessages"]

def test_cardDeliveryStatus(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardDeliveryStatus=param["cardDeliveryStatus"])
        assert res["countMessages"]

def test_embCardName(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], embCardName=param["embCardName"])
        assert res["countMessages"]

def test_cardPrefix(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardPrefix=param["cardPrefix"])
        assert res["countMessages"]

def test_cardSuffix(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardSuffix=param["cardSuffix"])
        assert res["countMessages"]

def test_cardProject(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], cardProject=param["cardProject"])
        assert res["countMessages"]

def test_dateCreateFrom(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateCreateFrom=param["dateCreateFrom"])
        assert res["countMessages"]

def test_dateCreateTo(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateCreateTo=param["dateCreateTo"])
        assert res["countMessages"]

def test_dateExpFrom(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateExpFrom=param["dateExpFrom"])
        assert res["countMessages"]

def test_dateExpTo(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateExpTo=param["dateExpTo"])
        assert res["countMessages"]

def test_dateLastChangeFrom(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateLastChangeFrom=param["dateLastChangeFrom"])
        assert res["countMessages"]

def test_dateLastChangeTo(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateLastChangeTo=param["dateLastChangeTo"])
        assert res["countMessages"]

def test_manufacturer(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], manufacturer=param["manufacturer"])
        assert res["countMessages"]

def test_deliveryRegionCode(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], deliveryRegionCode=param["deliveryRegionCode"])
        assert res["countMessages"]

def test_deliveryDistrictCode(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], deliveryDistrictCode=param["deliveryDistrictCode"])
        assert res["countMessages"]

def test_barcode(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], barcode=param["barcode"])
        assert res["countMessages"]

def test_dateOnPrintFrom(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateOnPrintFrom=param["dateOnPrintFrom"])
        assert res["countMessages"]

def test_dateOnPrintTo(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], dateOnPrintTo=param["dateOnPrintTo"])
        assert res["countMessages"]

def test_batchId(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], batchId=param["batchId"])
        assert res["countMessages"]

def test_orderId(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], orderId=param["orderId"])
        assert res["countMessages"]

def test_taxId(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], taxId=param["taxId"])
        assert res["countMessages"]

def test_limit(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], limit=int(param["limit"]))
        assert res["countMessages"]

def test_offset(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], offset=int(param["offset"]))
        assert res["countMessages"]

def test_actId(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], actId=param["actId"])
        assert res["countMessages"]

def test_fioReceiver(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], fioReceiver=param["fioReceiver"])
        assert res["countMessages"]

def test_typeTransfer(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], typeTransfer=param["typeTransfer"])
        assert res["countMessages"]

def test_deliveryChannel(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], deliveryChannel=param["deliveryChannel"])
        assert res["countMessages"]

def test_deliveryType(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], deliveryType=param["deliveryType"])
        assert res["countMessages"]

def test_messageIdPrimaryProcess(openTestData, obj):
        param = openTestData["getCards1"]
        res = obj.connectToWebService().service.getCards(shopId=param["shopId"], messageIdPrimaryProcess=param["messageIdPrimaryProcess"])
        assert res["countMessages"]

