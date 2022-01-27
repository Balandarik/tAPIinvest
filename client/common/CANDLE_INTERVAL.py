def candle_interval(interval):
    interval=interval.upper()
    if interval=="1MIN":
        return 'CANDLE_INTERVAL_1_MIN'
    elif interval=='5MIN':
        return 'CANDLE_INTERVAL_5_MIN'
    elif interval == '15MIN':
        return 'CANDLE_INTERVAL_15_MIN'
    elif inteval =='HOUR':
        return 'CANDLE_INTERVAL_HOUR'
    elif interval == 'DAY':
        return 'CANDLE_INTERVAL_DAY'
        #CANDLE_INTERVAL_UNSPECIFIED, CANDLE_INTERVAL_1_MIN, CANDLE_INTERVAL_5_MIN, CANDLE_INTERVAL_15_MIN, CANDLE_INTERVAL_HOUR, CANDLE_INTERVAL_DAY