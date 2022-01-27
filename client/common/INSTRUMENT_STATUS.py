
def INSTRUMENT_STATUS(check):  # Выбор статуса инструмента
    if check == 1:
        return 'INSTRUMENT_STATUS_UNSPECIFIED'
    elif check == 2:
        return 'INSTRUMENT_STATUS_BASE'
    elif check == 3:
        return 'INSTRUMENT_STATUS_ALL'
    else:
        return None