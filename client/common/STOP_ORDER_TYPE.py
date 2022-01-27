def STOP_ORDER_TYPE(check):
    if check.upper() == 'UNSPECIFIED' or check.upper()=='STOP_ORDER_TYPE_UNSPECIFIED':
        return 'STOP_ORDER_TYPE_UNSPECIFIED'
    elif check.upper() == 'PROFIT' or check.upper()=='STOP_ORDER_TYPE_TAKE_PROFIT':
        return 'STOP_ORDER_TYPE_TAKE_PROFIT'
    elif check.upper() == 'LOSS' or check.upper() == 'STOP_ORDER_TYPE_STOP_LOSS':
        return 'STOP_ORDER_TYPE_STOP_LOSS'
    elif check.upper() == 'LIMIT' or check.upper() == 'STOP_ORDER_TYPE_STOP_LIMIT':
        return 'STOP_ORDER_TYPE_STOP_LIMIT'


