def INSTRUMEN_ID(check):  # Выбор принадлежности instrument id
    if check == 1:
        return 'INSTRUMENT_ID_UNSPECIFIED'
    if check == 2:
        return 'INSTRUMENT_ID_TYPE_FIGI'
    elif check == 3:
        return 'INSTRUMENT_ID_TYPE_TICKER'