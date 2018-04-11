from models.soap import SoapMethods

class SQLActivateDeal:

    def getDealForActivate(self):
        s = 'SELECT ar.extclientid, ag.legalcontractnum, ag.charactseller, ag.statusagrid ' \
            'FROM alf_registercontractlog ar ' \
            'JOIN privateclients pc on pc.extclientprivid = ar.extclientid ' \
            'JOIN agreements ag on ag.clientprivid = pc.clientprivid ' \
            'WHERE ar.activate = 0 ' \
            'AND ar.errorcode = 0 AND ag.statusagrid = 1 and ag.charactseller is not null ' \
            'AND ag.legalcontractnum = ag.charactseller ' \
            'AND ROWNUM = 1'
        return s

    def checkDealForActivateStatus(self, charactseller):
        bind = {"charactseller": str(charactseller)}
        s = 'select ag.statusagrid ' \
            'from IC.Agreements ag ' \
            'where ag.legalcontractnum = :bind'  #+ str(cardNumber)
        cur = {"s": s, "bind": bind}
        return cur

if __name__ == '__main__':
    obj = SoapMethods()
    #print(obj.openXlsFile('D:\Python\SOAP\delivery12.xlsx'))
    print(obj.dbConnect(db='ISCARDT2_AIX').execute(SQLActivateDeal().getDealForActivate()).fetchall())
    t = SQLActivateDeal().checkDealForActivateStatus(630007040)
    cur = obj.dbConnect(db='ISCARDT2_AIX').execute(t["s"], bind=str(t["bind"]["charactseller"])).fetchall()
    print(cur)