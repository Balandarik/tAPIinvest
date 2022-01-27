def ORDER_DIRECTION(check):
    if check.upper() == 'UNSPECIFIED' or check.upper()=='ORDER_DIRECTION_UNSPECIFIED':
        return 'ORDER_DIRECTION_UNSPECIFIED'
    elif check.upper() == 'BUY' or check.upper()=='ORDER_DIRECTION_BUY':
        return 'ORDER_DIRECTION_BUY'
    elif check.upper() == 'SELL' or check.upper() == 'ORDER_DIRECTION_SELL':
        return 'ORDER_DIRECTION_SELL'


