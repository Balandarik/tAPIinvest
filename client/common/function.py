from client.common.connect import *
from client.common.method import *
from client.common.schemas import *
from client.common.INSTRUMENT_ID import *
import random
import string

def randomize():
    letters=string.ascii_lowercase
    rand_str=''.join(random.choice(letters) for i in range(35))
    return rand_str


class main_function(object):
    def __init__(self, token):
        self.token = token

    def getdividends(self,figi,_from,_to):
        return get_inform(method('getdividends'),
                          schemas('getdividends', figi=self.figi, _from=self._from,
                                  _to=self._to), token=self.token).get_inform()
    
    def futures(self):
        return get_inform(method('futures'), schemas('futures',check=1), self.token).get_inform()

    def bonds(self):
        return get_inform(method('bonds'), schemas('bonds',check=1), self.token).get_inform()

    def etfs(self):
        return get_inform(method('etfs'), schemas('etfs',check=1), self.token).get_inform()

    def currencies(self):
        return get_inform(method('currencies'), schemas('currencies',check=1), self.token).get_inform()

    def shares(self):
        return get_inform(method=method('shares'), schema=schemas('shares',check=1), token=self.token).get_inform()

    def shareBy(self,figi,check=2):  # Поиск акции. По умолчанию поиск по figi, параметр check=3 - поиск по тикеру
        return get_inform(method('shareBy'),
                          schemas('shareby', figi=figi, instrument_id=INSTRUMEN_ID(check)),
                          self.token).get_inform()

    def futureBy(self,figi,check=2):  # Поиск акции. По умолчанию поиск по figi, параметр check=3 - поиск по тикеру
        return get_inform(method('futureBy'),
                          schemas('futureBy', figi=figi, instrument_id=INSTRUMEN_ID(check)),
                          self.token).get_inform()

    def bondBy(self,figi,check=2):  # Поиск акции. По умолчанию поиск по figi, параметр check=3 - поиск по тикеру
        return get_inform(method('bondBy'),
                          schemas('bondBy', figi=figi, instrument_id=INSTRUMEN_ID(check)),
                          self.token).get_inform()

    def etfBy(self,figi,check=2):  # Поиск акции. По умолчанию поиск по figi, параметр check=3 - поиск по тикеру
        return get_inform(method('etfBy'),
                          schemas('etfBy', figi=figi, instrument_id=INSTRUMEN_ID(check)),
                          self.token).get_inform()

    def currencieBy(self,figi,check=2):  # Поиск акции. По умолчанию поиск по figi, параметр check=3 - поиск по тикеру
        return get_inform(method('CurrencyBy'),
                          schemas('CurrencyBy', figi=figi, instrument_id=INSTRUMEN_ID(check)),
                          self.token).get_inform()
    
    def GetAccruedInterests(self,figi,_from,_to):
        return get_inform(method('GetAccuruedInterests'),
                          schemas('GetAccuruedInterests', figi=figi, _from=_from,
                                  _to=_to), token=self.token).get_inform()
    
    def GetFuturesMargin(self,figi):
        return get_inform(method('GetFuturesMargin'),
                          schemas('GetFuturesMargin', figi=figi), token=self.token).get_inform()
    
    def GetInstrumentBy(self,figi,check=2):
        return get_inform(method('GetInstrumentBy'),
                          schemas('GetInstrumentBy', figi=figi, instrument_id=INSTRUMEN_ID(check)),
                          self.token).get_inform()
    def GetAccounts(self):
        return get_inform(method('GetAccounts'),
                          schemas('GetAccounts'), self.token).get_inform()
        
    def GetInfo(self):
        
        return get_inform(method('GetInfo'),
                          schemas('GetInfo'), self.token).get_inform()
    def GetUserTariff(self):
        return get_inform(method('GetUserTariff'),
                          schemas('GetUserTariff'), self.token).get_inform()

    def GetCandles(self,figi,_from,_to,interval='1min'):
        return get_inform(method('GetCandles'),
                          schemas('GetCandles', figi=figi, _from=_from,
                                  _to=_to,interval=interval), token=self.token).get_inform()
    def GetLastPrices(self, figi):
        if not isinstance(figi,list):
            figi=[figi]
        return get_inform(method('GetLastPrice'),
                          schemas('GetLastPrice', figi=figi),
                          self.token).get_inform()

    def GetOrderBook(self,figi,depth=1):
        return get_inform(method('GetOrderBook'),
                          schemas('GetOrderBook', figi=figi,depth=depth),
                          self.token).get_inform()

    def GetTradingStatus(self,figi):
        return get_inform(method('GetTradingStatus'),
                          schemas('GetTradingStatus', figi=figi),
                          self.token).get_inform()
            
    def GetPortfolio(self,accountId):
        return get_inform(method('GetPortfolio'),
                          schemas('GetPortfolio', accountId=accountId),
                          self.token).get_inform()
    
    def GetOperation(self,accountId,_from,_to,figi,operations='UNSPECIFIED'):
        return get_inform(method('GetOperations'),
                          schemas('GetOperations', accountId=accountId,_from=_from,_to=_to,figi=figi,check='UNSPECIFIED'),
                          self.token).get_inform()

    def GetPositions(self,accountId):
        return get_inform(method('GetPositions'),
                          schemas('GetPositions', accountId=accountId),
                          self.token).get_inform()

    def GetWithdrawLimits(self,accountId):
        return get_inform(method('GetWithdrawLimits'),
                          schemas('GetWithdrawLimits', accountId=accountId),
                          self.token).get_inform()

    def GetOrders(self,accountId):
        return get_inform(method('GetOrders'),
                          schemas('GetOrders', accountId=accountId),
                          self.token).get_inform()

    def CancelOrder(self,accountId,orderId):
        return get_inform(method('CancelOrder'),
                          schemas('CancelOrder', accountId=accountId, orderId=orderId),
                          self.token).get_inform()

    def GetOrderState(self,accountId,orderId):
        return get_inform(method('GetOrderState'),
                          schemas('GetOrderState', accountId=accountId, orderId=orderId),
                          self.token).get_inform()

    def PostOrder(self,figi,quantity,price,direction,accountId,orderType,orderId=randomize()):
        return get_inform(method('PostOrder'),
                          schemas('PostOrder', figi=figi,quantity=quantity,price=price,direction=direction,accountId=accountId,orderType=orderType, orderId=orderId),
                          self.token).get_inform()

    def CancelStopOrder(self,accountId,orderId):
        return get_inform(method('CancelStopOrder'),
                          schemas('CancelStopOrder', accountId=accountId, orderId=orderId),
                          self.token).get_inform()

    def GetStopOrders(self,accountId):
        return get_inform(method('GetStopOrders'),
                          schemas('GetStopOrders', accountId=accountId),
                          self.token).get_inform()

    def PostStopOrder(self,figi,quantity,price,stopPrice,direction,accountId,expirationType,stoporderType,expireDate):
        return get_inform(method('PostStopOrder'),
                          schemas('PostStopOrder', figi=figi,quantity=quantity,price=price,stopPrice=stopPrice,direction=direction,accountId=accountId,expirationType=expirationType,stoporderType=stoporderType, expireDate=expireDate),
                          self.token).get_inform()

class Sandbox(object):
    def __init__(self,token):
        self.token=token

    def CancelSandboxOrder(self,accountId,orderId):
        return get_inform(method('CancelSandboxOrder'),
                          schemas('CancelSandboxOrder', accountId=accountId, orderId=orderId),
                          self.token).get_inform()
    
    def GetSandboxAccounts(self):
        return get_inform(method('GetSandboxAccounts'),
                          schemas('GetSandboxAccounts'), self.token).get_inform()
    
    def GetSandboxOperations(self,accountId,_from,_to,figi,operations='UNSPECIFIED'):
        return get_inform(method('GetSandboxOperations'),
                          schemas('GetSandboxOperations', accountId=accountId,_from=_from,_to=_to,figi=figi,check='UNSPECIFIED'),
                          self.token).get_inform()

    def GetSandboxOrderState(self,accountId,orderId):
        return get_inform(method('GetSandboxOrderState'),
                          schemas('GetSandboxOrderState', accountId=accountId, orderId=orderId),
                          self.token).get_inform()

    def GetSandboxOrders(self,accountId):
        return get_inform(method('GetSandboxOrders'),
                          schemas('GetSandboxOrders', accountId=accountId),
                          self.token).get_inform()

    def GetSandboxPortfolio(self,accountId):
        return get_inform(method('GetSandboxPortfolio'),
                          schemas('GetSandboxPortfolio', accountId=accountId),
                          self.token).get_inform()

    def GetSandboxPositions(self,accountId):
        return get_inform(method('GetSandboxPositions'),
                          schemas('GetSandboxPositions', accountId=accountId),
                          self.token).get_inform()

    def PostSandboxOrder(self,figi,quantity,price,direction,accountId,orderType,orderId=randomize()):
        return get_inform(method('PostSandboxOrder'),
                          schemas('PostSandboxOrder', figi=figi,quantity=quantity,price=price,direction=direction,accountId=accountId,orderType=orderType, orderId=orderId),
                          self.token).get_inform()

    def SandboxPayIn(self,accountId,amount,currency):
        return get_inform(method('SandboxPayIn'),
                          schemas('SandboxPayIn', accountId,amount,currency),
                          self.token).get_inform()

    def OpenSandboxAccount(self):
        return get_inform(method('OpenSandboxAccount'),
                          schemas('OpenSandboxAccount'),
                          self.token).get_inform()

    def CloseSandboxAccount(self,accountId,amount,currency):
        return get_inform(method('CloseSandboxAccount'),
                          schemas('CloseSandboxAccount', accountId,amount,currency),
                          self.token).get_inform()
    
    