from client.common.INSTRUMENT_STATUS import *
from client.common.CANDLE_INTERVAL import *
from client.common.OPERATION_STATE import *
from client.common.ORDER_DIRECTION import *
from client.common.ORDER_TYPE import *
from client.common.STOP_ORDER_DIRECTION import *
from client.common.STOP_ORDER_EXPIRATION import *
from client.common.STOP_ORDER_TYPE import *

def schemas(name, *args, **kwargs):  # Выбор схемы для передачи данных
    
    user_service={'GetAccounts','GetInfo','GetUserTariff','GetSandboxAccounts','OpenSandboxAccount'}
    
    All_instruments={'futures','bonds','etfs','currencies','shares'}
    
    about_instrument={'shareby','futureBy','bondBy','etfBy','CurrencyBy','GetInstrumentBy'}
    
    With_figi_from_to={'GetAccuruedInterests','getdividends'}
    
    only_figi={'GetFuturesMargin','GetTradingStatus'}
    
    only_accountId={'GetPositions','GetPortfolio','GetWithdrawLimits','GetOrders','GetStopOrders','GetSandboxOrders','GetSandboxPortfolio','GetSandboxPositions','CloseSandboxAccount'}

    accountId_and_orderid={'CancelOrder','GetOrderState','CancelSandboxOrder','GetSandboxOrderState'}
    
    GetOperations={'GetOperations', 'GetSandboxOperations'}
    
    if name in All_instruments:
        return {"instrumentStatus": f"{INSTRUMENT_STATUS(kwargs['check'])}"}

    elif name in With_figi_from_to:
        return {"figi": kwargs['figi'],
                "from": kwargs['_from'],
                "to": kwargs['_to']
                }
    elif name in about_instrument:
        
        return {
            "idType": kwargs['instrument_id'],
            "id": str(kwargs['figi'])
        }
    
    elif name in only_figi:
        return {
            "figi": str(kwargs['figi'])
        }
    
    elif name in user_service:
        return {}
    
    elif name == 'GetCandles':
        return {
                  "figi": str(kwargs['figi']),
                   "from": kwargs['_from'],
                    "to": kwargs['_to'],
                  "interval": candle_interval(kwargs['interval'])
                }
    
    elif name=='GetLastPrice':
        return {
                  "figi": str(kwargs['figi'])
                  #"figi": ['BBG000C0HQ54']
                }
    
    elif name=='GetOrderBook':
        return {
                  "figi": str(kwargs['figi']),
                  "depth": int(kwargs['depth'])
                }
    
    elif name in only_accountId:
        return {
            "accountId": str(kwargs['accountId'])
            }
    
    elif name in GetOperations:
        return {
              "accountId": str(kwargs['accountId']),
              "from": kwargs['_from'],
              "to": kwargs['_to'],
              "state": OPERATION_STATE(kwargs['check']),
              "figi": str(kwargs['figi'])
            }
    elif name in accountId_and_orderid:
        return {
      "accountId": str(kwargs['accountId']),
      "orderId": str(kwargs['orderId'])
               }

    elif name == 'CancelStopOrder':
        return {
      "accountId": str(kwargs['accountId']),
      "stopOrderId": str(kwargs['orderId'])
               }




    elif name == 'PostOrder' or name == 'PostSandboxOrder':
        return {
                  "figi": str(kwargs['figi']),
                  "quantity": str(kwargs['quantity']),
                  "price": {
                    "nano": int(round(float(kwargs['price'])%1*1000000000,2)),
                    "units": str(int(float(kwargs['price'])//1))

                  },
                  "direction": ORDER_DIRECTION(kwargs['direction']),
                  "accountId": str(wargs['accountId']),
                  "orderType": ORDER_TYPE(kwargs['orderType']),
                  "orderId": str(kwargs['orderId'])
               }
    elif name == 'PostStopOrder':

        return {
                  "figi": str(kwargs['figi']),
                  "quantity": str(kwargs['quantity']),
                  "price": {
                    "nano": int(round(float(kwargs['price'])%1*1000000000,2)),
                    "units": str(int(float(kwargs['price'])//1))
                  },
                  "stopPrice": {
                    "nano": int(round(float(kwargs['stopPrice'])%1*1000000000,2)),
                    "units": str(int(float(kwargs['stopPrice'])//1))
                  },
                  "direction": STOP_ORDER_DIRECTION(kwargs['direction']),
                  "accountId": str(kwargs['accountId']),
                  "expirationType": STOP_ORDER_EXPIRATION_TYPE(kwargs['expirationType']),
                  "stopOrderType": STOP_ORDER_TYPE(kwargs['stoporderType']),
                  "expireDate": kwargs['expireDate']
                }

    elif name == 'SandboxPayIn':
        return {
                  "accountId": str(kwargs['accountId']),
                  "amount": {
                    "nano": int(round(float(kwargs['amount'])%1*1000000000,2)),
                    "currency": str(kwargs['currency']),
                    "units": str(int(float(kwargs['amount'])//1))
                  }
                }


