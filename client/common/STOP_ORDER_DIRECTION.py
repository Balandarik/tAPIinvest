def STOP_ORDER_DIRECTION(check):
    if check.upper() == 'UNSPECIFIED' or check.upper()=='STOP_ORDER_DIRECTION_UNSPECIFIED':
        return 'STOP_ORDER_DIRECTION_UNSPECIFIED'
    elif check.upper() == 'BUY' or check.upper()=='STOP_ORDER_DIRECTION_BUY':
        return 'STOP_ORDER_DIRECTION_BUY'
    elif check.upper() == 'SELL' or check.upper() == 'STOP_ORDER_DIRECTION_SELL':
        return 'STOP_ORDER_DIRECTION_SELL'


