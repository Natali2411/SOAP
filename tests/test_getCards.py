from models.soap import SoapMethods

def test_method_status_code():
    obj = SoapMethods()
    res = obj.connectToWebService().service.getCards(shopId='8344', cardHash='$1$53553298$8139C5264DDE92403A6695638F9A20CB')
    assert res['countMessages']