from models.soap import SoapMethods

class SQLActivateCard:

    def getCardForActivate(self):
        s = 'select c.cardnum as cardNumber, pr.cidentcode as taxid, pr.pnumber as passportNumber, pr.mobilephone as phoneNumber ' \
            'from IC.Cards c ' \
            'join IC.Agreements ag on ag.contractid = c.contractid ' \
            'join IC.Privateclients pr on ag.clientprivid = pr.clientprivid ' \
            'where c.cardstatusid = 1 and rownum = 1'
        return s

    def checkCardForActivateStatus(self, cardNumber):
        bind = {"cardNumber": str(cardNumber)}
        s = 'select c.cardstatusid ' \
            'from IC.Cards c ' \
            'where c.cardnum = :bind'  #+ str(cardNumber)
        cur = {"s": s, "bind": bind}
        return cur

if __name__ == '__main__':
    obj = SoapMethods()
    #print(obj.openXlsFile('D:\Python\SOAP\delivery12.xlsx'))
    print(obj.dbConnect(db='ISCARDT2_AIX').execute(SQLActivateCard().getCardForActivate()).fetchall())
    t = SQLActivateCard().checkCardForActivateStatus(4226051550023777)
    cur = obj.dbConnect(db='ISCARDT2_AIX').execute(t["s"], bind=str(t["bind"]["cardNumber"])).fetchall()
    print(cur)
