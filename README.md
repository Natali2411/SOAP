    '''
    #d = datetime.strptime(str(f["1"][16]), '%dd.%md.%YYYY')
    res = obj.connectToWebService(wsdl).service.createApplication(contragentId=f["1"][0], taxId=f["1"][1], phoneNumber=f["1"][2],
                                                                  clientName=str(f["1"][3]), deliveryAddress=str(f["1"][4]), productName=str(f["1"][6]), shopId=str(f["1"][7]), cardId=f["1"][9],
                                                                  cardMask=str(f["1"][10]), channelDelivery=str(f["1"][11]), objectTypeId=f["1"][12], comment="test", #str(f["1"][11]),
                                                                  messageIdPrimaryProcess=str(f["1"][14]), primaryProcessCode=str(f["1"][15]), dateExp=str(f["1"][16]), externalSystem=str(f["1"][17]),
                                                                  user=str(f["1"][18]))
    
'''
    #res = obj.connectToWebService(wsdl).service.createApplication()