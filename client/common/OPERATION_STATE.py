def OPERATION_STATE(check):
    if check.upper() == 'UNSPECIFIED':
        return 'OPERATION_STATE_UNSPECIFIED'
    elif check.upper() == 'EXECUTED':
        return 'OPERATION_STATE_EXECUTED'
    elif check.upper() == 'CANCELED':
        return 'OPERATION_STATE_CANCELED'