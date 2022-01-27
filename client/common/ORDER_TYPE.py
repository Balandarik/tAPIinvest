def ORDER_TYPE(check):
    if check.upper() == 'UNSPECIFIED' or check.upper()=='ORDER_TYPE_UNSPECIFIED':
        return 'ORDER_TYPE_UNSPECIFIED'
    elif check.upper() == 'LIMIT' or check.upper()=='ORDER_TYPE_LIMIT':
        return 'ORDER_TYPE_LIMIT'
    elif check.upper() == 'MARKET' or check.upper() == 'ORDER_TYPE_MARKET':
        return 'ORDER_TYPE_MARKET'
